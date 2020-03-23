# For copyright and license notices, see __manifest__.py file in module root


from odoo import fields, models


class CheckLayout(models.Model):
    _name = 'check.layout'
    _description = 'Check Layout Definition'

    name = fields.Char(
        string='Nombre del diseño',
        required=True
    )
    amount_top = fields.Integer()
    amount_left = fields.Integer()

    issue_date_top = fields.Integer()
    issue_date_left = fields.Integer()

    payment_date_top = fields.Integer()
    payment_date_left = fields.Integer()

    partner_name_top = fields.Integer()
    partner_name_left = fields.Integer()

    amount_words_top = fields.Integer()
    amount_words_left = fields.Integer()

    check_no_top = fields.Integer()
    check_no_left = fields.Integer()

