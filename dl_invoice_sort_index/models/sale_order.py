# -*- coding: utf-8 -*-
import re
from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _order = 'name_sort_index asc, id desc'

    name_sort_index = fields.Integer(
        string="Número (Ordem)",
        compute="_compute_name_sort_index",
        store=True,
        index=True,
    )

    @api.depends('name')
    def _compute_name_sort_index(self):
        for order in self:
            val = 0
            if order.name and order.name != '/':
                parts = re.split(r'[/-]', order.name.strip())
                for part in reversed(parts):
                    digits = re.sub(r'\D', '', part)
                    if digits:
                        try:
                            val = int(digits)
                            break
                        except ValueError:
                            pass
            order.name_sort_index = val
