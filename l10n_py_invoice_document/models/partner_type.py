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
        ('foreign_customer', 'Proveedore del Exterior'),
    ],
        help='Tipo de cliente'
    )
    ruc_required_person = fields.Boolean()
    ruc_required_company = fields.Boolean()
    consolidated_ruc = fields.Char()
    default_account = fields.Many2one(
        'account.account',
        string='Cuenta Predeterminada',
    )