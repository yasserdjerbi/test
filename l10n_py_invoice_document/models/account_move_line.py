# For copyright and license notices, see __manifest__.py file in module root

from odoo import models


class AccountJournal(models.Model):
    _inherit = "account.move.line"

    def _get_computed_account(self):
        """ solo para el caso nota de credito al cliente, cambiar el
            tipo de cuenta para la factura
        """
        self.ensure_one()

        if not self.product_id:
            return False

        # Si no es el caso, llamamos al super
        if self.move_id.type != 'out_refund':
            return super()._get_computed_account()

        # Si es el caso devolvemos la cuenta altermantiva
        prod = self.product_id
        prod_account = prod.property_account_income_return_id
        categ_account = prod.categ_id.property_account_income_categ_return_id
        return prod_account or categ_account
