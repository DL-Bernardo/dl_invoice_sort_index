# -*- coding: utf-8 -*-
{
    'name': 'Invoice Sort Index & Sequence Order',
    'version': '18.0.1.0.7',
    'summary': 'Fast Invoice Sorting, Chronological Sequence Organization & Angola SAFT Alignment',
    'description': """
DL Invoice Sort Index & Sequence Order
======================================

This module improves the sorting of invoices and quotations in Odoo, ensuring they are ordered **numerically**
by sequential number instead of string-based lexicographical sorting.

Key Features:
-------------
- Adds an indexed field `name_sort_index` to `account.move` and `sale.order`.
- Ensures invoices, vendor bills, and quotations are ordered sequentially in list views.
- Optional `Número (Ordem)` column available in Invoices and Quotations list views.
- Guarantees that invoices are properly ordered in SAFT-AO export (legal requirement in Angola).
- 100% compatible with Odoo 15, 16, 17, 18, 19 & 20 (Community, Enterprise & Odoo.sh).
""",
    'author': 'DIGITALUB ANGOLA, LDA',
    'website': 'https://www.digitalub.ao',
    'support': 'suporte@digitalub.ao',
    'category': 'Accounting',
    'depends': ['account', 'sale'],
    'data': [
        'views/invoice_sort_views.xml',
    ],
    'license': 'LGPL-3',
    'images': [
        'static/description/banner.png',
        'static/description/screenshot1.png',
        'static/description/screenshot_step2.png',
        'static/description/screenshot2.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 0.0,
    'currency': 'USD',
}
