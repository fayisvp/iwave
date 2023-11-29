
from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patients"
    _description = "hospital Patients"

    name = fields.Char(string="Name:")
    age = fields.Integer(string="Age:")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    phone = fields.Char(string="Phone Number:")
    address = fields.Char(string="Address")
