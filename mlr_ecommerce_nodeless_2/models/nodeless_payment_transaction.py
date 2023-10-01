# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import pprint

from odoo import api, models, fields
from odoo.exceptions import UserError, ValidationError

from odoo.addons.payment import utils as payment_utils

_logger = logging.getLogger(__name__)

class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    nodeless_invoice_id = fields.Char('nodeless Invoice ID')
    nodeless_conversion_rate = fields.Float('Conversion rate')
    nodeless_invoiced_sat_amount = fields.Float('Invoiced Satoshi Amount', digits=(12, 8))
    nodeless_payment_link = fields.Char('nodeless Payment Link')
    nodeless_payment_link_qr_code = fields.Binary('QR Code', compute="_generate_qr")


    def _get_specific_rendering_values(self, processing_values):
        """ Override of payment to return Paypal-specific rendering values.

        Note: self.ensure_one() from `_get_processing_values`

        :param dict processing_values: The generic and specific processing values of the transaction
        :return: The dict of provider-specific processing values
        :rtype: dict
        """
        res = super()._get_specific_rendering_values(processing_values)
        if self.provider_code != 'nodeless':
            return res

        base_url = self.provider_id.get_base_url()
        return {
            'reference': self.reference,
            'amount': self.amount,
            'currency_code': self.currency_id.name,
        }

