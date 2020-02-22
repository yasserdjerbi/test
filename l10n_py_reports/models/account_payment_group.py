# For copyright and license notices, see __manifest__.py file in module root

from odoo import models


class AccountPaymentGroup(models.Model):
    _inherit = "account.payment.group"

    def payment_print(self):
        action = 'l10n_py_reports.action_report_payment_group_receipt'
        return self.env.ref(action).report_action(self)

        # ############################################################################# # noqa
        # Falta migrar el modulo account_withholding, account_withholding_automatic
        checks = self.mapped('payment_ids.check_ids')
        # withholdings = self.payment_ids.filtered(lambda x: x.tax_withholding_id)   # noqa
        payments = self.payment_ids.filtered(lambda x: not x.check_ids)
        if checks or payments:
            print('medios de pago')

            # Cheques <for each="line in o.mapped('payment_ids.check_ids')">
            for check in checks:
                print('Cheque nro %s - %s - Venc. %s' % (
                check.name, check.bank_id.name or check.journal_id.name,
                check.payment_date))  # noqa

            # Retenciones <for each="line in (o.payment_ids.filtered(lambda x: x.tax_withholding_id))"> # noqa
            # for ret in withholdings:
            #    print("%s - %s" % (ret.tax_withholding_id.name, ret.withholding_number or ret.name)) # noqa

            # Otros pagos <for each="line in o.payment_ids.filtered(lambda x: not x.tax_withholding_id and not x.check_ids)"> # noqa
            for pay in payments:
                print('%s%s' % (pay.journal_id.name,
                                pay.other_currency and ' (%s %s)' % (
                                pay.signed_amount,
                                pay.currency_id.name) or ''))  # noqa

            # #############################################################################
        documents = self.with_context(
            payment_group_id=self.id).matched_move_line_ids  # noqa
        unmatched_amount = self.unmatched_amount
        if documents or unmatched_amount:
            print('Comprobantes imputados')
            for doc in documents:
                print(doc.move_id.display_name)
                print(doc.date_maturity)
                print(doc.balance)
                print(doc.payment_group_matched_amount)
                print(doc.currency_id)

            if unmatched_amount:
                print('A cuenta', unmatched_amount)

            # #############################################################################
            # Falta migrar el modulo account_debt_management
            #       if self.partner_type == 'customer':
            #           documents = (self.partner_type=='customer' and self.partner_id.commercial_partner_id.receivable_debt_ids or self.partner_id.commercial_partner_id.payable_debt_ids).filtered(lambda x: x.company_id == self.company_id) # noqa
            #           for doc in documents:
            #               print(doc.document_number)

        return
