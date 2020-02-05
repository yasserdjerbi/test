# For copyright and license notices, see __manifest__.py file in module root

import logging

_logger = logging.getLogger(__name__)

from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):

    _logger.info('Migration -> poner partner type en clientes locales')
    env.cr.execute("""
    UPDATE res_partner
    SET partner_type_id = 1;
    """)

    _logger.info('Migration -> mover los datos vat - ruc')
    env.cr.execute("""
    UPDATE res_partner
    SET ruc = vat;
    """)
