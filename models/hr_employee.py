from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    branch_id = fields.Many2one(
        comodel_name='branch.branch',
        string='Company Branch',
        required=False)