# __manifest__.py
{
    'name': 'DL Invoice Sort Index',
    'version': '17.0.1.0.1',
    'summary': 'Correctly sorts invoices by sequential number for Angola SAFT compliance',
    'description': """
📑 DL Invoice Sort Index
=========================

This module improves the sorting of invoices in Odoo, ensuring they are ordered **numerically** 
by sequential number instead of string-based sorting.

✨ Features:
------------
- Adds a new technical field `name_sort_index` to `account.move`.
- Ensures invoices are ordered sequentially in the list view.
- Helps guarantee that invoices are properly ordered in the SAFT export, 
  a legal requirement in Angola.

⚙️ Installation:
----------------
- Copy the module to your Odoo addons folder.
- Update the Apps list and install.

🚀 Usage:
---------
- Invoices will automatically be displayed in the correct sequential order.
- SAFT validation will succeed thanks to proper ordering.
""",
    'author': 'DIGITALUB ANGOLA, LDA',
    'website': 'https://www.digitalub.ao',
    'category': 'Accounting',
    'depends': ['account', 'sale'],
    'data': [],
    'license': 'LGPL-3',
    'images': [
        'static/description/banner.png',
        'static/description/screenshot1.png',
        'static/description/screenshot2.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
