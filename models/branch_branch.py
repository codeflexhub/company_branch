from odoo import models, fields


class BranchBranch(models.Model):
    _name = 'branch.branch'
    _description = 'company branch'
    name = fields.Char(
        string='Name',
        required=False,
    )
    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        required=False,
    )
    latitude_coordinates = fields.Float(
        string='Latitude Coordinates',
        required=False,
    )
    longitude_coordinates = fields.Float(
        string='Longitude Coordinates',
        required=False,
    )

    tolerance_area = fields.Float(
        string='Tolerance Area',
        required=False,
    )

    employee_ids = fields.One2many(
        comodel_name='hr.employee',
        inverse_name='branch_id',
        string='Employees',
        required=False)

    _sql_constraints = [
        ('check_valid_min_lat', 'check(latitude_coordinates >= -90 )',
         'Range from -90 to 90 for latitude'),
        ('check_valid_max_lat', 'check(latitude_coordinates <= 90 )',
         'Range from -90 to 90 for latitude'),
        ('check_valid_min_long', 'check(longitude_coordinates >= -180 )',
         'Range from -180 to 180 for latitude'),
        ('check_valid_max_long', 'check(longitude_coordinates <= 180 )',
         'Range from -180 to 180 for longitude'),
    ]
