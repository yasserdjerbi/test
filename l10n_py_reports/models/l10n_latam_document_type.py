# For copyright and license notices, see __manifest__.py file in module root

from odoo import models, _
from odoo.exceptions import UserError


class L10nLatamDocumentType(models.Model):
    _inherit = 'l10n_latam.document.type'

    def next_sequence(self):
        """ Obtener el siguiente numero de secuencia para aquellos documentos
            que requieren secuencia en vetas.
            Si es la primera vez que se usa esto, crear la secuencia
        """
        self.ensure_one()
        assert self.purchase_seq is True

        if not self.sequence_id:
            self.sequence_id = self._create_sequence()

        return self.sequence_id.next_by_id()

    def _create_sequence(self):
        """ Generar una secuencia
        """
        self.ensure_one()
        vals = {
            'name': self.report_name,
            'implementation': 'no_gap',
            'padding': 7,
            'l10n_latam_document_type_id': self.id,
            'number_next_actual': 0,
            'code': self.name
        }
        return self.env['ir.sequence'].create(vals)

    def _format_document_number(self, document_number):
        """ Make validation of Import Dispatch Number
          * making validations on the document_number. If it is wrong it
            should raise an exception
          * format the document_number against a pattern and return it
        """

        # si es otro pais retornar al super
        self.ensure_one()
        if self.country_id != self.env.ref('base.py'):
            return super()._format_document_number(document_number)

        # si esta habilitada secuencia de compras el campo esta invisible
        # terminar
        if self.compra and self.purchase_seq:
            return

        # no lo dejo pasar si no tengo algun numero
        if not document_number:
            return False

        # si el documento no require timbrado, no formateo el numero
        if not self.req_timbrado:
            return document_number

        msg = "'%s' " + _("no es un valor valido para el "
                          "documento") + " '%s'.\n%s"

        # Invoice Number Validator (.i.e: 3-4-123)
        failed = False
        args = document_number.split('-')
        if len(args) != 3:
            failed = True
        else:
            suc, exp, number = args
            if len(suc) > 3 or not suc.isdigit():
                failed = True
            elif len(exp) > 3 or not number.isdigit():
                failed = True
            elif len(number) > 7 or not number.isdigit():
                failed = True

            mask = '{:>03s}-{:>03s}-{:>07s}'
            document_number = mask.format(suc, exp, number)
        if failed:
            raise UserError(msg % (document_number, self.name, _(
                'El numero de documento debe ser ingresado separando con '
                'el signo menos (-) cada parte, debe tener un maximo de 3 '
                'digitos para Codigo de Establecimiento y Punto de '
                'Expedicion y un maximo de 7 digitos para el numero de '
                'documento. Los siguientes son ejemplos de numeros '
                'validos:\n\n'
                '* 1-1-1\n'
                '* 003-001-0000087\n'
                '* 25-45-885')))

        return document_number
