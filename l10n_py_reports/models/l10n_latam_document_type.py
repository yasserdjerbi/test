# For copyright and license notices, see __manifest__.py file in module root

from odoo import models, fields, _
from odoo.exceptions import UserError


class L10nLatamDocumentType(models.Model):
    _inherit = 'l10n_latam.document.type'

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

        if not document_number:
            return False

        # recibos
        if self.code in ['CC', 'CR']:
            return document_number

        # factura
        if self.code in ['FAC']:
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
