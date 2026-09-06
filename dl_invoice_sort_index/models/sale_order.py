# models/sale_order.py
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _order = 'name_sort_index asc, id desc'

    name_sort_index = fields.Integer(string="Número (Ordem)", compute="_compute_name_sort_index", store=True)

    @api.depends('name')
    def _compute_name_sort_index(self):
        for order in self:
            try:
                # Extrai o número da proforma, mesmo com prefixos diferentes
                number_part = order.name.split('/')[-1]
                order.name_sort_index = int(number_part)
            except (ValueError, TypeError):
                order.name_sort_index = 0