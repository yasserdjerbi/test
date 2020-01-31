# For copyright and license notices, see __manifest__.py file in module root


from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class PartnerType(models.Model):
    _name = 'partner.type'

    type = fields.Char()
    ruc_required_person = fields.Boolean()
    ruc_required_company = fields.Boolean()



