#!/usr/bin/env bash
# run test suite for odoo-paraguay

CLIENT="tatakua"

echo $CLIENT"_test"

oe -Q l10n_py_invoice_document -c $CLIENT -d $CLIENT"_test"
oe -Q l10n_py_reports -c $CLIENT -d $CLIENT"_test"
oe -Q l10n_py_vat_book -c $CLIENT -d $CLIENT"_test"
oe -Q partner_ruc_unique -c $CLIENT -d $CLIENT"_test"
