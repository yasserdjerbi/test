# For copyright and license notices, see __manifest__.py file in module root

from odoo import models, _
from odoo.exceptions import UserError


class AccountMoveLine(models.Model):
    _inherit = "account.move"

    def action_post(self):
        """ Verificar las lineas de factura por el IVA
            si el documento tiene vat_enabled todas las lineas deben tener IVA
            si no lo tiene, ninguna linea debe tener IVA

            Aca hay que tener en cuenta que el unico tipo de impuesto que va
            ahi es el IVA por lo tanto no nos preocupamos por verificar que
            imuesto es, si hay algo en tax_ids eso sera IVA.
        """
        doc_type_id = self.l10n_latam_document_type_id
        vat_enabled = doc_type_id.vat_enabled
        if self.type in ['out_invoice', 'out_refund',
                         'in_invoice', 'in_refund']:
            lines = self.invoice_line_ids
            if vat_enabled:
                # si va a salir en el libro de iva
                if lines.filtered(lambda x: not x.tax_ids):
                    raise UserError(_('Para el documento %s, todas las lineas '
                                      'deben tener al menos un impuesto IVA')
                                    % doc_type_id.name)
            else:
                # si  no va a salir en el libro de iva
                if lines.filtered(lambda x: x.tax_ids):
                    raise UserError(_('Para el documento %s, no puede haber '
                                      'ninguna linea con impuesto IVA')
                                    % doc_type_id.name)

        # llamar al metodo original
        return super().action_post()
