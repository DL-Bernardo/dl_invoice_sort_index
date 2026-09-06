# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase

class TestInvoiceSort(TransactionCase):

    def test_invoice_sort_index(self):
        """Test that the sort index is computed correctly."""
        # Create some sample invoices with different name formats
        invoice1 = self.env['account.move'].create({'name': 'INV/2024/0001', 'move_type': 'out_invoice'})
        invoice2 = self.env['account.move'].create({'name': 'F-2024-0002', 'move_type': 'out_invoice'})
        invoice3 = self.env['account.move'].create({'name': 'R/2024/3', 'move_type': 'out_invoice'})
        invoice_invalid = self.env['account.move'].create({'name': 'InvalidName', 'move_type': 'out_invoice'})

        # Check if the name_sort_index is computed as expected
        self.assertEqual(invoice1.name_sort_index, 1)
        self.assertEqual(invoice2.name_sort_index, 2)
        self.assertEqual(invoice3.name_sort_index, 3)
        self.assertEqual(invoice_invalid.name_sort_index, 0)

        # Search for invoices and check the order
        invoices = self.env['account.move'].search([], order='name_sort_index asc')
        
        # Ensure the invalid name is first (or handle as needed)
        self.assertIn(invoice_invalid, invoices)
        self.assertIn(invoice1, invoices)
        self.assertIn(invoice2, invoices)
        self.assertIn(invoice3, invoices)
