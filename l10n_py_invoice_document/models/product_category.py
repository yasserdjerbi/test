# For copyright and license notices, see __manifest__.py file in module root


from odoo import models, fields


class ProductCategory(models.Model):
    _inherit = 'product.category'

    property_account_income_categ_return_id = fields.Many2one(
        'account.account',
        company_dependent=True,
        string="Cuenta de Ingresos (devolución)",
        domain="[('deprecated', '=', False), "
               " ('company_id', '=', current_company_id)]",
        help="Mantenga este campo vacio para usar el valor predeterminado de "
             "la categoria del producto.")
