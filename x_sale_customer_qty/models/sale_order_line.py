# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    customer_qty = fields.Float(string='Quantité du client', default="0.0")