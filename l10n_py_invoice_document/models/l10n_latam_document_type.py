# For copyright and license notices, see __manifest__.py file in module root

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class L10nLatamDocumentType(models.Model):
    _inherit = 'l10n_latam.document.type'

    # TODO hay que quitar este campo
    purchase_seq = fields.Boolean(
        string='Autosecuencia',
        help='Si esta tildado al usarlo para compra tomara un numero de '
             'secuencia unico y no dejara introducir numero de documento'
    )
    req_timbrado = fields.Boolean(
        help='Si esta tildado el documento requiere timbrado y ademas, en una '
             'compra se valida el numero ingresado contra una mascara.'
    )
    compra = fields.Boolean(
        help='si esta tildado el documento aplica para compras'
    )
    venta = fields.Boolean(
        help='si esta tildado el documento aplica para ventas'
    )
    vat_enabled = fields.Boolean(
        string='Libro IVA',
        help='Si esta tildado el documento aparece en el libro de IVA'
    )
    sequence_id = fields.Many2one(
        'ir.sequence',
        ondelete='cascade',
        help='Secuencia habilitada para este documento',
        string='Secuencia'
    )

    # TODO este constrains anda raro en la vista de lista. mejorarlo
    @api.constrains('compra', 'purchase_seq')
    def check_purchase_seq(self):
        if self.purchase_seq and not self.compra:
            raise UserError(_('Autosecuencia y compra deben estar tildados '
                             'juntos'))

    def name_get(self):
        result = []
        for rec in self:
            name = rec.name
            if rec.code:
                name = '(%s) %s' % (rec.doc_code_prefix, name)
            result.append((rec.id, name))
        return result
