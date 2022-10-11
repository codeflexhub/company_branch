from odoo import models, fields

class ResCompany(models.Model):
    _inherit = 'res.company'
    branch_ids = fields.One2many(
        comodel_name='branch.branch',
        inverse_name='company_id',
        string='Branches',
        required=False)
