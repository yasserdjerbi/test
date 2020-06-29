# For copyright and license notices, see __manifest__.py file in module root
from odoo import _, api, models
from odoo.exceptions import ValidationError
from odoo.tools import config


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.constrains('ci')
    def _check_ci_unique(self):
        for record in self:
            # verificar si la ci ya existe
            results = self.env['res.partner'].search_count([
                ('parent_id', '=', False),
                ('ci', '=', record.ci),
                ('id', '!=', record.id)
            ])
            if results:
                raise ValidationError(_(
                    "The CI %s already exists in another "
                    "partner.") % record.ci)

    @api.constrains('ruc')
    def _check_ruc_unique(self):

        # obtener una lista de los ruc consolidados
        consolidated_rucs = []
        partner_types = self.env['partner.type'].search(
            [('consolidated_ruc', '!=', False)])
        for partner_type in partner_types:
            consolidated_rucs.append(partner_type.consolidated_ruc)

        for record in self:
            if record.parent_id or not record.ruc:
                continue

            test_condition = (config['test_enable'] and
                              not self.env.context.get('test_ruc'))

            if test_condition:
                continue

            if record.ruc in consolidated_rucs:
                continue

            # si el ruc no es consolidado entonces verificar si hay otro igual
            results = self.env['res.partner'].search_count([
                ('parent_id', '=', False),
                ('ruc', '=', record.ruc),
                ('id', '!=', record.id)
            ])
            if results:
                raise ValidationError(_(
                    "The RUC %s already exists in another "
                    "partner.") % record.ruc)
