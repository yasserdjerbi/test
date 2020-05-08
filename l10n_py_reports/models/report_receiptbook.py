# For copyright and license notices, see __manifest__.py file in module root


from odoo import fields, models


class AccountPayment(models.Model):
    _name = "report.receiptbook"
    _order = 'sequence'
    _description = 'Talonarios de Recibo'

    name = fields.Char(
        string='Nombre',
        help='Nombre del talonario',
        required=True
    )
    partner_type = fields.Selection(
        [('customer', 'Cliente'),
         ('supplier', 'Proveedor')],
        help='Tipo de cliente al que se le hace el recibo',
        default='customer',
        required=True
    )
    sequence_id = fields.Many2one(
        'ir.sequence',
        help='Secuencia que define el numero de recibo',
    )
    company_id = fields.Many2one(
        'res.company',
        'Company',
        default=lambda self: self.env.company,
        required=True
    )
    sequence = fields.Integer(
        string='Orden',
        default=10,
        required=True
    )
