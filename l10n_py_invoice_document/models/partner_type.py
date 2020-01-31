# For copyright and license notices, see __manifest__.py file in module root


from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class PartnerType(models.Model):
    _name = 'partner.type'

    type = fields.Selection([
        ('local_customer', 'Clientes Locales'),
        ('foreign', 'Extranjeros'),
        ('Export', 'Exportacion'),
        ('diplomats', 'Diplomaticos'),
        ('state_client', 'Clientes del Estado'),
        ('local_vendor', 'Proveedores Locales'),
        ('local_creditor', 'Acreedores Locales'),
        ('foreign_customer', 'Proveedore del Exterior')],
        help='Tipo de cliente',
        required=True
    )
    ruc_required_person = fields.Boolean(
        string='Obligatorio para individuos',
        required=True
    )
    ruc_required_company = fields.Boolean(
        string='Obligatorio para empresas',
        required=True
    )
    consolidated_ruc = fields.Char(
        string='RUC Consolidado',
        required=True
    )
    default_account = fields.Many2one(
        'account.account',
        string='Cuenta Predeterminada',
    )
    applied_to = fields.Selection([
        ('sale', 'Ventas'),
        ('purchase', 'Compras')],
        string='Aplicacion',
        required=True
    )
