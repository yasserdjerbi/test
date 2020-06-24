# For copyright and license notices, see __manifest__.py file in module root

from odoo import models, fields, api


class L10nLatamDocumentType(models.Model):
    _inherit = 'l10n_latam.document.type'

    internal_type = fields.Selection(
        selection_add=[
            ('customer_payment', 'Customer Payment'),
            ('supplier_payment', 'Supplier Payment')
        ]
    )
    purchase_seq = fields.Boolean(
        string='Autosecuencia',
        help='Si esta tildado al usarlo para compra tomara un numero de '
             'secuencia unico y no dejara introducir numero de documento',
        default=False
    )
    req_timbrado = fields.Boolean(
        help='Si esta tildado el documento requiere timbrado y ademas, en una '
             'compra se valida el numero ingresado contra una mascara.',
        default=False
    )
    compra = fields.Boolean(
        help='si esta tildado el documento aplica para compras',
        required=True,
        default=False
    )
    venta = fields.Boolean(
        help='si esta tildado el documento aplica para ventas',
        required=True,
        default=False
    )
    vat_enabled = fields.Boolean(
        string='Libro IVA',
        help='Si esta tildado el documento aparece en el libro de IVA',
        default=False
    )
    sequence_id = fields.Many2one(
        'ir.sequence',
        ondelete='cascade',
        help='Secuencia habilitada para este documento',
        string='Secuencia'
    )

    @api.onchange('req_timbrado', 'vat_enabled')
    def _onchange_req_timbrado(self):
        """ si se habilita req_timbrado, vat_enabled debe ser True
        """
        if self.req_timbrado:
            self.vat_enabled = True

    @api.onchange('purchase_seq', 'compra', 'venta')
    def _onchange_req_purchase_seq(self):
        """ si se habilita purchase_seq, compra = True, venta = False,
            req_timbrado = False
        """
        if self.purchase_seq:
            self.compra = True
            self.venta = False
            self.req_timbrado = False

    def name_get(self):
        result = []
        for rec in self:
            name = rec.name
            if rec.code:
                name = '(%s) %s' % (rec.doc_code_prefix, name)
            result.append((rec.id, name))
        return result
