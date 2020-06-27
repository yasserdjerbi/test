# For copyright and license notices, see __manifest__.py file in module root

import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):

    _logger.info('Migration -> disable old receipts')
    cr.execute("""
    UPDATE account_payment
    SET receiptbook_id = null;
    """)
