
import logging
import uuid

import requests
from werkzeug.urls import url_encode, url_join, url_parse

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('nodeless', "nodeless")], ondelete={'nodeless': 'set default'})
    nodeless_store_id = fields.Char(string='Store ID')

    def test_nodeless_server_connection(self):
        try:
            _logger.info(f"Called Nodeless test_nodeless_server_connection.")
            server_url = self.crypto_server_url + "/api/v1/status"
            headers = {"Authorization": "Bearer %s" % (self.crypto_api_key), "Content-Type": "application/json",
                       "Accept": "application/json"}
            response = requests.request(method="GET", url=server_url, headers=headers)
            #_logger.info(f"Response of Nodeless test_nodeless_server_connection.{response}{response.json()}")
            is_success = True if response.status_code == 200 else False
            return is_success
        except Exception as e:
            raise UserError(_("Test Connection Error: %s", e.args))

    def nodeless_action_test_connection(self):
        _logger.info(f"Called Nodeless nodeless_action_test_connection.")
        is_success = self.test_nodeless_server_connection()
        type = (
            "success"
            if is_success
            else "danger"
        )
        messages = (
            "Everything seems properly set up!"
            if is_success
            else "Server credential is wrong. Please check credential."
        )
        title = _("Connection Testing")

        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": title,
                "message": messages,
                "sticky": False,
                "type": type
            },
        }


