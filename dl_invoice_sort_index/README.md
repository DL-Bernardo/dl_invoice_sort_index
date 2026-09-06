# 🔢 DL Invoice Sort Index

This module improves the sorting of invoices in Odoo by using the **sequential invoice number** instead of the default string-based sorting.

---

## ✨ Features
- Fixes incorrect ordering (e.g. `INV/2024/10` before `INV/2024/2`).
- Adds a numeric index field `name_sort_index`.
- Ensures invoices are listed and exported in **proper sequential order**.

---

## 📑 SAFT Compliance
Proper invoice sequencing is **mandatory for SAFT validation**.  
With this module, your invoices are exported in the correct order, ensuring compliance.

---

## 📸 Screenshots
1️⃣ Without the module → wrong order  
2️⃣ With the module → correct sequential order  

---

## ⚙️ Installation
1. Copy the folder `dl_invoice_sort_index` into your Odoo addons path.  
2. Restart your Odoo service.  
3. Activate Developer Mode.  
4. Go to **Apps** → Update Apps List.  
5. Search for **DL Invoice Sort Index** and click **Install**.  

---

## 👤 Author
**DIGITALUB ANGOLA, LDA** 🌍  
📧 geral@digitalub.ao  
🌐 [https://digitalub.ao](https://digitalub.ao)

