# For copyright and license notices, see __manifest__.py file in module root


from odoo import fields, models

STYLE = 'position:absolute;left:%spx;top:%spx;'
SCALE = 4


class CheckLayout(models.Model):
    _name = 'check.layout'
    _description = 'Check Layout Definition'

    name = fields.Char(
        string='Nombre del diseño',
        required=True
    )

    amount = fields.Boolean(
        string="Total a pagar"
    )
    amount_top = fields.Integer()
    amount_left = fields.Integer()
    style_amount = fields.Char(
        compute="_compute_style_amount"
    )

    issue_date = fields.Boolean(
        string="Fecha de emision"
    )
    issue_date_top = fields.Integer()
    issue_date_left = fields.Integer()
    style_issue_date = fields.Char(
        compute="_compute_issue_date"
    )

    payment_date = fields.Boolean(
        string="Fecha de pago"
    )
    payment_date_top = fields.Integer()
    payment_date_left = fields.Integer()
    style_payment_date = fields.Char(
        compute="_compute_payment_date"
    )

    partner_name = fields.Boolean(
        string="Destinatario"
    )
    partner_name_top = fields.Integer()
    partner_name_left = fields.Integer()
    style_name = fields.Char(
        compute="_compute_name"
    )

    amount_words = fields.Boolean(
        string="Total en letras"
    )
    amount_words_top = fields.Integer()
    amount_words_left = fields.Integer()
    style_amount_words = fields.Char(
        compute="_compute_amount_words"
    )

    check_no = fields.Boolean(
        string="Numero de cheque"
    )
    check_no_top = fields.Integer()
    check_no_left = fields.Integer()
    style_check_no = fields.Char(
        compute="_compute_check_no"
    )

    @staticmethod
    def scale(left, top):
        return SCALE * left, SCALE * top

    def _compute_style_amount(self):
        left, top = self.scale(self.amount_left, self.amount_top)
        self.style_amount = STYLE % (left, top)
        print(STYLE % (left, top))

    def _compute_issue_date(self):
        left, top = self.scale(self.issue_date_left, self.issue_date_top)
        self.style_issue_date = STYLE % (left, top)
        print(STYLE % (left, top))

    def _compute_payment_date(self):
        left, top = self.scale(self.payment_date_left, self.payment_date_top)
        self.style_payment_date = STYLE % (left, top)
        print(STYLE % (left, top))

    def _compute_name(self):
        left, top = self.scale(self.partner_name_left, self.partner_name_top)
        self.style_name = STYLE % (left, top)
        print(STYLE % (left, top))

    def _compute_amount_words(self):
        left, top = self.scale(self.amount_words_left, self.amount_words_top)
        self.style_amount_words = STYLE % (left, top)
        print(STYLE % (left, top))

    def _compute_check_no(self):
        left, top = self.scale(self.check_no_left, self.check_no_top)
        self.style_check_no = STYLE % (left, top)
        print(STYLE % (left, top))
