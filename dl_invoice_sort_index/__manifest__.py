# __manifest__.py
{
    'name': 'Invoice Sort Index & Sequence Order',
    'version': '15.0.1.0.3',
    'summary': 'Fast Invoice Sorting, Chronological Sequence Organization & Angola SAFT Alignment',
    'description': """
📑 DL Invoice Sort Index (Free Community Edition)
==================================================

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

--------------------------------------------------
⭐ Conheça as Soluções Oficiais da DIGITALUB ANGOLA:
- 📑 Facturação Electrónica AGT Angola & SAF-T AO Oficial
- 📦 Stock Barcode Scanner (Controlo de Inventário em Tempo Real)
- 🏨 Digitalub Gestão Hoteleira Completa (PMS)
- 💰 Retenção na Fonte Angola (Withholding Tax)
- 🌐 Demonstração Online: https://demo.digitalub.ao
- 🏢 Website Oficial: https://www.digitalub.ao
--------------------------------------------------
""",
    'author': 'DIGITALUB ANGOLA',
    'website': 'https://digitalub.ao',
    'category': 'Accounting',
    'depends': ['account'],
    'data': [],
    'license': 'LGPL-3',
    'images': [
        'static/description/banner.png',
        'static/description/screenshot1.png',
        'static/description/screenshot2.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,    'price': 0.0,
    'currency': 'EUR',

}
