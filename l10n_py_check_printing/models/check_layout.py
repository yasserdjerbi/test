# For copyright and license notices, see __manifest__.py file in module root


from odoo import fields, models


class CheckLayout(models.Model):
    _name = 'check.layout'
    _description = "Check Layout Definition"

    name = fields.Char(
        string='Nombre del diseño de cheques'
    )
    valor1 = fields.Integer(    )
    valor2 = fields.Integer(    )
    valor3 = fields.Integer(    )
    valor4 = fields.Integer(    )
    valor5 = fields.Integer(    )
    valor6 = fields.Integer(    )
