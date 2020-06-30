#!/bin/sh
# correr localmente todos los tests de la localizacion
# ----------------------------------------------------

# restaurar la base de test vacia
cp /odoo_ar/odoo-13.0e/tatakua/backup_dir/test_bkp/tatakua_test.zip /odoo_ar/odoo-13.0e/tatakua/backup_dir/
oe --restore -d tatakua_test -c tatakua -f tatakua_test.zip

#  -i  l10n_py,l10n_py_invoice_document,partner_ruc_unique,l10n_py_reports,l10n_py_vat_book \

# correr los tests
sudo docker run --rm -it \
    -v /odoo_ar/odoo-13.0e/tatakua/config:/opt/odoo/etc/ \
    -v /odoo_ar/odoo-13.0e/tatakua/data_dir:/opt/odoo/data \
    -v /odoo_ar/odoo-13.0e/tatakua/sources:/opt/odoo/custom-addons \
    --link pg-tatakua:db \
    jobiols/odoo-ent:13.0e -- \
       -i  l10n_py_vat_book \
   --stop-after-init -d tatakua_test #--test-enable

# br falla
# bo falla