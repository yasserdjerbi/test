# For copyright and license notices, see __manifest__.py file in module root

from odoo import fields, models


class ChangeSequenceNumber(models.AbstractModel):
    _name = 'adjust.sequence.number'
    _description = 'Adjust sequence number Wizard'

    sequence_id = fields.Many2one(
        'ir.sequence'
    )
    next_number = fields.Integer(
    )

    def do_change(self):
        self.sequence_id.write({'number_next_actual': self.next_number})
