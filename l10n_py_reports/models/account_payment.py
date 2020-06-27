# For copyright and license notices, see __manifest__.py file in module root

from num2words import num2words
from odoo import fields, models, _
from odoo.exceptions import UserError, ValidationError


class AccountPayment(models.Model):
    _inherit = "account.payment"

    receiptbook_id = fields.Many2one(
        'account.payment.receiptbook',
    )
    amount_in_words = fields.Char(
        compute="_compute_amount_in_words"
    )
    next_receipt_number = fields.Integer(
        related='receiptbook_id.next_number'
    )

    def _compute_amount_in_words(self):
        for rec in self:
            lang = self.env.user.lang[:2]
            _ = u'GUARANIES %s' % num2words(rec.amount, lang=lang)
            rec.amount_in_words = _.upper()

    def post(self):
        """  Este metodo sobreescribe el original de odoo para poder usar los
            talonarios de recibo solo si el pais es Paraguay.

            Create the journal items for the payment and update the payment's
            state to 'posted'.
            A journal entry is created containing an item in the source
            liquidity account (selected journal's default_debit or
            default_credit) and another in the destination reconcilable account
            (see _compute_destination_account_id).
            If invoice_ids is not empty, there will be one reconcilable move
            line per invoice to reconcile with.
            If the payment is a transfer, a second journal entry is created in
            the destination journal to receive money from the transfer account.
        """
        if self.env.user.company_id.country_id != self.env.ref('base.py'):
            return super().post()

        account_move = self.env['account.move']\
            .with_context(default_type='entry')

        for rec in self:
            if rec.state != 'draft':
                raise UserError(_("Only a draft payment can be posted."))

            if any(inv.state != 'posted' for inv in rec.invoice_ids):
                raise ValidationError(_('The payment cannot be processed '
                                        'because the invoice is not open!'))

            # keep the name in case of a payment reset to draft
            if not rec.name:
                # Use the right sequence to set the name
                # TODO Revisar la transferencia
                if rec.payment_type == 'transfer':
                    sequence_code = 'account.payment.transfer'
                else:
                    # if there is no receiptbook, then it is a payment order,
                    # then put the default payment order.
                    if not rec.receiptbook_id:
                        receipt = 'l10n_py_reports.default_payment_order'
                        rec.receiptbook_id = self.env.ref(receipt)

                rec.name = rec.receiptbook_id.sequence_id.next_by_id(
                    sequence_date=rec.payment_date)

                if not rec.name and rec.payment_type != 'transfer':
                    raise UserError(_("You have to define a sequence for %s "
                                      "in your company.") % (sequence_code,))

            moves = account_move.create(rec._prepare_payment_moves())
            moves.filtered(lambda move:
                           move.journal_id.post_at != 'bank_rec').post()

            # Update the state / move before performing any reconciliation.
            move_name = self._get_move_name_transfer_separator()\
                .join(moves.mapped('name'))
            rec.write({'state': 'posted', 'move_name': move_name})

            if rec.payment_type in ('inbound', 'outbound'):
                # ==== 'inbound' / 'outbound' ====
                if rec.invoice_ids:
                    (moves[0] + rec.invoice_ids).line_ids \
                        .filtered(lambda line: not line.reconciled and line
                                  .account_id == rec.destination_account_id)\
                        .reconcile()
            elif rec.payment_type == 'transfer':
                # ==== 'transfer' ====
                moves.mapped('line_ids')\
                    .filtered(lambda line: line.account_id == rec.company_id
                              .transfer_account_id)\
                    .reconcile()

        return True
