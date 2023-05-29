from odoo import models, fields

class Customer(models.Model):
    _name = 'customer'
    _description = 'Khách hàng'

    name = fields.Char(string='Họ và tên', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Số điện thoại')
    address = fields.Text(string='Địa chỉ')
