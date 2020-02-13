# For copyright and license notices, see __manifest__.py file in module root

from odoo.exceptions import ValidationError
from odoo import fields, models, api, _


class TimbradoData(models.Model):
    _name = "timbrado.data"
    _description = 'Timbrado que habilita las factura'

    name = fields.Char(
        string='Número de Timbrado',
        required=True
    )
    validity_start = fields.Date(
        help='Fecha a partir de la cual esta vigente el timbrado',
        string='Inicio Vigencia',
        required=True
    )
    validity_end = fields.Date(
        help='Fecha hasta la cual es válido el timbrado',
        string='Fin Vigencia',
        required=True
    )
    shipping_point = fields.Char(
        required=True,
        string='Establecimiento',
        default='001'
    )
    trade_code = fields.Char(
        required=True,
        string='Expedición',
        default='001'
    )
    document_type_id = fields.Many2one(
        'l10n_latam.document.type',
        domain=[('req_timbrado', '=', True)],
        help='Indica el tipo de comprobante para el que aplica el timbrado',
        required=True,
        string='Tipo de Comprobante'
    )
    code = fields.Char(
        related='document_type_id.code',
        help='Campo técnico para seleccionar el timbrado'
    )
    qty = fields.Integer(
        help='Cantidad de comprobantes autorizados en este timbrado',
        compute="_compute_qty",
        string="Cantidad"
    )
    start_number = fields.Integer(
        required=True,
        string='Comprobante Inicial'
    )
    end_number = fields.Integer(
        required=True,
        string='Comprobante Final'
    )
    range = fields.Char(
        compute="_compute_range",
        string="Rango"
    )
    print_system = fields.Selection(
        selection=[('pre_printed', 'Pre Impreso'),
                   ('auto_printer', 'Auto Impresor')],
        string='Sistema de impresión',
        required=True
    )
    state = fields.Selection(
        [('draft', 'Borrador'),
         ('active', 'Activo'),
         ('no_active', 'No Activo')],
        default='draft',
        string="Estado"
    )
    next_number = fields.Integer(
        related='document_type_id.sequence_id.number_next'
    )
    sequence_id = fields.Many2one(
        'ir.sequence',
        related='document_type_id.sequence_id'
    )

    _sql_constraints = [
        ('name_unique', 'unique (name)', 'El timbrado ya existe...!')
    ]

    @staticmethod
    def _format(value):
        try:
            intvalue = int(value)
        except ValueError:
            raise ValidationError('Esperabamos un numero')
        return '{0:03}'.format(intvalue)

    @api.onchange('shipping_point')
    def onchange_point(self):
        self.ensure_one()
        self.shipping_point = self._format(self.shipping_point)

    @api.onchange('trade_code')
    def onchange_code(self):
        self.ensure_one()
        self.trade_code = self._format(self.trade_code)

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            try:
                int(rec.name)
            except ValueError:
                raise ValidationError('Se esperaba un numero')

            if len(rec.name) != 8:
                raise ValidationError(_('El Timbrado debe tener 8 digitos'))

    @api.depends('start_number', 'end_number')
    def _compute_range(self):
        for rec in self:
            r = '[%s - %s]' % (rec.start_number, rec.end_number)
            rec.range = r

    @api.depends('start_number', 'end_number')
    def _compute_qty(self):
        for rec in self:
            rec.qty = rec.end_number - rec.start_number + 1

    def button_activate(self):
        """ Activar el timbrado,
            Hay que verificar que no haya otro activo
        """
        for rec in self:
            # verificar la vigencia del timbrado
            if not rec.validity_start < fields.Date.today() < rec.validity_end:
                raise ValidationError('El timbrando no se puede activar '
                                      'porque las fechas no son validas')

            # verificar que no haya otro timbrado activo para el mismo
            # shiping_point / trade_code / document_type_id
            duplicate = self.search([
                ('shipping_point', '=', rec.shipping_point),
                ('trade_code', '=', rec.trade_code),
                ('document_type_id', '=', rec.document_type_id.id),
                ('state', '=', 'active')
            ])
            if duplicate:
                raise ValidationError('Ya existe un timbrado activo para el '
                                      'mismo Establecimiento / Expedicion y '
                                      'Tipo de documento')

            # verificar que el documento asociado a este timbrado tiene una
            # secuencia, si no la tiene la crea.
            rec.document_type_id.check_sequence(rec.shipping_point,
                                                rec.trade_code)

            rec.state = 'active'

    def name_get(self):
        ret_list = list()
        for rec in self:
            compose_name = (rec.code, rec.name, rec.range)
            ret_list.append((rec.id, '%s %s %s' % compose_name))
        return ret_list

    def validate_timbrado_all(self, today=False):
        """ Chequear la validez de todos los timbrados
            el parametro today=False es para los tests
        """
        if not today:
            today = fields.Date.today()
        for rec in self:
            if rec.validity_start <= today <= rec.validity_end:
                rec.button_activate()
            else:
                rec.deactivate()

    def deactivate(self):
        """ Desactivar el timbrado
        """
        # desacoplar la secuencia del documento
        self.document_type_id.sequence_id = False
        self.state = 'no_active'
