from odoo import models, fields, _
from odoo.exceptions import UserError, ValidationError


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
        help='Secuencia habilitada para este diario'
    )

    def next_sequence_number(self, timbrado_id):
        """ Devuelve el proximo numero de secuencia para este documento
        """
        self.ensure_one()

        if not self.sequence_id:
            raise ValueError('Este docuento no tiene secuencia, verifique la '
                             'configuracion')
        next_number = self.sequence_id.number_next

        # chequear numero a validar es mayor que el maximo
        if next_number > timbrado_id.end_number:
            raise ValidationError(
                _('El timbrado ya no es valido, el numero de documento '
                  'que quiere validar esta mas alla del rango.\n'
                  'El proximo numero es %s mientras que el '
                  'rango de validez del timbrado es [%s - %s]') %
                (next_number, timbrado_id.start_number,
                 timbrado_id.end_number))

        # chequear numero a validar es menor que el minimo
        if next_number < timbrado_id.start_number:
            raise ValidationError(
                _('El timbrado no es valido. Intenta validar un numero de '
                  'documento que es menor al minimo valido para este '
                  'timbrado.\n'
                  'El proximo numero es %s mientras que el '
                  'rango de validez del timbrado es [%s - %s]') %
                (next_number, timbrado_id.start_number,
                 timbrado_id.end_number))

        # numero a validar es igual al maximo, invalidar timbrado
        if next_number == timbrado_id.end_number:
            timbrado_id.deactivate()

        return self.sequence_id.next_by_id()

    def _format_document_number(self, document_number):
        """ Make validation of Import Dispatch Number
          * making validations on the document_number. If it is wrong it
            should raise an exception
          * format the document_number against a pattern and return it
        """
        self.ensure_one()
        if self.country_id != self.env.ref('base.py'):
            return super()._format_document_number(document_number)

        if not document_number:
            return False

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
                'El numero de documento debe ser ingresado separando con el '
                'signo menos (-) cada parte, debe tener un maximo de 3 '
                'digitos para Codigo de Establecimiento y Punto de Expedicion '
                'y un maximo de 7 digitos para el numero de documento. '
                'Los siguientes son ejemplos de numeros validos:\n'
                '* 1-1-1\n'
                '* 003-001-0000087\n'
                '* 25-45-885')))

        return document_number
