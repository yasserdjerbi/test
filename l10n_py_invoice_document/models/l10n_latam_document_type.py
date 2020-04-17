# For copyright and license notices, see __manifest__.py file in module root

from odoo import models, fields


class L10nLatamDocumentType(models.Model):
    _inherit = 'l10n_latam.document.type'

    cod_doc_set = fields.Integer(
        help='codigo que tiene que ver con la generacion del libro de iva o '
             'como se llame en paraguay'
    )
    req_timbrado = fields.Boolean(
        help='si esta tildado el documento requiere timbrado'
    )
    compra = fields.Boolean(
        help='si esta tildado el documento aplica para compras'
    )
    venta = fields.Boolean(
        help='si esta tildado el documento aplica para ventas'
    )
    sequence_id = fields.Many2one(
        'ir.sequence',
        ondelete='set null',
        help='Secuencia habilitada para este diario',
        string='Secuencia'
    )
