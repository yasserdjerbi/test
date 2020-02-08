# For copyright and license notices, see __manifest__.py file in module root

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Partner(models.Model):
    _inherit = 'res.partner'

    ci = fields.Char(
        help='Cedula de Identidad',
        string='CI'
    )
    ruc = fields.Char(
        help="Registro Unico de Contribuyentes",
        string='RUC',
        copy=False
    )
    partner_type_sale_id = fields.Many2one(
        'partner.type',
        string='Tipo de cliente',
        ondelete='restrict',
        domain=[('applied_to', '=', 'sale')]
    )
    partner_type_purchase_id = fields.Many2one(
        'partner.type',
        string='Tipo de proveedor',
        ondelete='restrict',
        domain=[('applied_to', '=', 'purchase')]
    )

    @api.constrains('ruc')
    def check_ruc(self):
        for rec in self:
            if not rec._check_ruc(rec.ruc):
                raise ValidationError(_("El RUC es invalido"))

    def _check_ruc(self, ruc):
        """ Chequea validez de RUC calculando el digito verificador
        """
        if not ruc:
            return True

        if ruc.find('-') < 0:
            # no tiene guion, ya es invalido.
            return False

        # obtengo el numero antes del guion y el dv despues del guion
        numero = ruc[:ruc.find('-')]
        dv = ruc[ruc.find('-') + 1:]

        # verifico que los dos sean numeros, sino ya es invalido
        try:
            numero = int(numero)
            dv = int(dv)
        except ValueError:
            return False

        # verifico que el dv sea igual al calculado
        return dv == self._calc_dv(numero)

    @staticmethod
    def _calc_dv(ruc):
        """ Función que calcula el dígito verificador en Python
            autor: Blas Isaias Fernández Cáceres
            https://github.com/BlasFerna/py-ruc-calc
        """
        # Convierte el argumento en string
        # luego invierte los valores
        ruc_str = str(ruc)[::-1]

        # variable total que almacena el resultado
        v_total = 0

        basemax = 11

        # el factor de chequeo actual,
        # inicializa en 2
        k = 2

        for i in range(0, len(ruc_str)):
            if k > basemax:
                k = 2
            # multiplicación de cada valor por el factor de chequeo actual(k)
            v_total += int(ruc_str[i]) * k
            # se incrementa el valor de la variable k
            k += 1

        # resto de la división entre el resultado y el valor de la
        # variable basemax
        resto = v_total % basemax

        if resto > 1:
            # si el resto es mayor que uno, entonces el valor de basemax
            # es restado por el resultado de la operación anterior
            return basemax - resto
        else:
            return 0

    @api.onchange('partner_type_sale_id')
    def onchange_partner_type_sale_id(self):
        """ Cuando cambia el tipo de partner en ventas, corregir las cuentas
            contables.
        """
        for rec in self:
            partner_type = rec.partner_type_sale_id

            # poner la cuenta por defecto si esta definida
            if partner_type.default_account:
                if partner_type.applied_to == 'sale':
                    rec.property_account_receivable_id = \
                        partner_type.default_account

    @api.onchange('partner_type_purchase_id')
    def onchange_partner_type_purchase_id(self):
        """ Cuando cambia el tipo de partner en compras, corregir las cuentas
            contables.
        """
        for rec in self:
            partner_type = rec.partner_type_purchase_id

            # poner la cuenta por defecto si esta definida
            if partner_type.default_account:
                if partner_type.applied_to == 'purchase':
                    rec.property_account_payable_id = \
                        partner_type.default_account

    def _name_search(self, name, args=None, operator='ilike', limit=100,
        name_get_uid=None):
        if not args:
            args = []
        if name:
            positive_operators = ['=', 'ilike', '=ilike', 'like', '=like']
            partner_ids = []
            if operator in positive_operators:
                partner_ids = self._search(
                    [('ruc', 'ilike', name)] + args, limit=limit,
                    access_rights_uid=name_get_uid)
                if not partner_ids:
                    partner_ids = self._search(
                        [('ci', 'ilike', name)] + args, limit=limit,
                        access_rights_uid=name_get_uid)
                    if not partner_ids:
                        partner_ids = self._search(
                            [('name', 'ilike', name)] + args, limit=limit,
                            access_rights_uid=name_get_uid)
        else:
            partner_ids = self._search(args, limit=limit,
                                       access_rights_uid=name_get_uid)

        return models.lazy_name_get(self.browse(partner_ids).with_user(
            name_get_uid))
