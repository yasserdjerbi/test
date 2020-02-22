# odoo-paraguay

[![Build Status](https://travis-ci.com/jobiols/odoo-paraguay.svg?token=77F3WzCbdXWpLDSsuTxX&branch=13.0)](https://travis-ci.com/jobiols/odoo-paraguay)

Localizacion de Odoo - Paraguay

## El repositorio tiene los siguientes branch que trabajan de la siguiente manera;

- **13.0** Version estable de produccion para la version 13.0
- **master** desarrollos inestables para la siguiente version de odoo.
- **13.0.nombre-branch#nro-issue** branch donde se esta desarrollando / corrigiendo un issue

## Sobre los modulos

- **l10n_py** : Plantillado de las cuentas contables impuestos etc de la localizacion
- **l10n_py_invoice_document** : Definicion de tipos de documento facturas, notas de credito, recibos, etc
- **l10n_py_reports** : Reportes para facturas y recibos
- **l10n_py_vat_book** : Libros de IVA
- **partner_ruc_unique** : adicional, evita la duplicacion de RUC que no son consolidados.

## Testing Server

http://ec2-54-233-138-43.sa-east-1.compute.amazonaws.com:8069

- Documentacion de timbrado:
https://drive.google.com/drive/folders/1gIXyOiICRADUTDMV43tNosxwJwEz_292?usp=sharing
