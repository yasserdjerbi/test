#!/usr/bin/env bash
# run test suite for odoo-paraguay

# exit inmediately if a command exits with a non-zero status.
set -e

CLIENT="tatakua"

function do_test() {
    module="$1"
    oe -Q $module -c $CLIENT -d $CLIENT"_test"
}

do_test "l10n_py_invoice_document"
do_test "l10n_py_reports"
do_test "l10n_py_vat_book"
do_test "partner_ruc_unique"
