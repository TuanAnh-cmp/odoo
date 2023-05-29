from odoo import models, fields

class Employee(models.Model):
    _name = 'employee'
    _description = 'Nhân viên'

    name = fields.Char(string='Họ và tên', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Số điện thoại')
    address = fields.Text(string='Địa chỉ')
    position = fields.Char(string='Chức vụ')
