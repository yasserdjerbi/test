# For copyright and license notices, see __manifest__.py file in module root

from odoo import models


class AccountMoveReversal(models.TransientModel):
    _inherit = "account.move.reversal"

    def reverse_moves(self):
        """ Cuando se crea la nota de credito desde la factura hay que
            recalcular las cuentas de las lineas de factura.
            Para que tome las cuentas correspondientes a NC
        """
        # crea la nc normalmente
        ret = super().reverse_moves()

        # obtenemos el objeto
        _nc = self.env['account.move'].browse(ret['res_id'])

        # revisamos todas las lineas de factura y le recalculamos la cuenta
        for line in _nc.invoice_line_ids:
            if not line.product_id or line.display_type in ('line_section',
                                                            'line_note'):
                continue
            line.account_id = line._get_computed_account()
        return ret
