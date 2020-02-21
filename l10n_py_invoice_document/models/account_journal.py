# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.exceptions import ValidationError
from odoo import fields, models, api, _


class AccountJournal(models.Model):
    _inherit = "account.journal"

    l10n_py_shipping_point = fields.Char(
        'Esablecimiento',
        help='Numero de sucursal que representa este diario',
        copy=False
    )
    l10n_py_trade_code = fields.Char(
        'Expedición',
        help='Punto de expedición que representa este diario',
        copy=False
    )
    _sql_constraints = [
        ('diario-unico-sucursal-expedicion-type',
         'unique(l10n_py_shipping_point,l10n_py_trade_code,type)',
         "Otro diario ya tiene los mismos codigos de sucursal y expedicion!!")
    ]

    @staticmethod
    def _format(value):
        """ Formatea los numeros de sucursal y expedicion
        """
        try:
            intvalue = int(value)
        except ValueError:
            raise ValidationError(_('Esperabamos un numero'))
        return '{0:03}'.format(intvalue)

    @api.onchange('l10n_py_shipping_point')
    def onchange_point(self):
        self.ensure_one()
        self.l10n_py_shipping_point = self._format(self.l10n_py_shipping_point)

    @api.onchange('l10n_py_trade_code')
    def onchange_code(self):
        self.ensure_one()
        self.l10n_py_trade_code = self._format(self.l10n_py_trade_code)

    def _get_journal_codes(self):
        self.ensure_one()
        usual_codes = ['FAC', 'ND', 'NC']
        internal_codes = ['AF', 'PLS', 'CING', 'VUI', 'CUI', 'NCI', 'SUEL']
        expo_codes = ['DESP', 'INV', 'FEXP']
        if self.type != 'sale':
            return []
        return usual_codes + internal_codes + expo_codes

    @api.constrains('type', 'l10n_py_shipping_point',
                    'l10n_py_trade_code', 'l10n_latam_use_documents')
    def _check_configurations(self):
        """ Do not let to update journal if already have confirmed invoices
        """
        self.ensure_one()
        if self.company_id.country_id != self.env.ref('base.py'):
            return True
        if self.type != 'sale' and self._origin.type != 'sale':
            return True
        invoices = self.env['account.move'].search(
            [('journal_id', '=', self.id),
             ('state', '!=', 'draft')])
        if invoices:
            inv = invoices[:5]
            raise ValidationError(_(
                'No puede cambiar la configuracion de un diario que ya tiene'
                'facturas validadas, mostramos algunas:\n' +
                '- %s' % ('\n- '.join(inv.mapped('display_name')))))
