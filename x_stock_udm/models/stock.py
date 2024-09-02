# -*-coding: utf-8 -*-

from odoo import models, api, fields, _  # type: ignore

class ProductProduct(models.Model):
    
    _inherit = "product.template"
    
    x_qty_in_kg = fields.Float(string="Unite de mesure en Kg", compute="_compute_udm_in_kg")
    
    @api.depends('qty_available')
    def _compute_udm_in_kg(self):
        for product in self:
            # If UDM == g
            if product.uom_id.name == 'g':
                product.x_qty_in_kg = product.qty_available / 1000 # Convert in Kg
            else:
                product.x_qty_in_kg = product.qty_available  # Otherwise we keep the initial value

                
    

