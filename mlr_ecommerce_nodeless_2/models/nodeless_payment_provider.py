
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
    nodeless_server_url = fields.Char(string='Server URL')
    nodeless_api_key = fields.Char(string='API Key')
    nodeless_store_id = fields.Char(string='Store ID')
    nodeless_expiration_minutes = fields.Integer('Expiration Minutes')
    nodeless_monitoring_minutes = fields.Integer('Monitoring Minutes')
    nodeless_speed_policy = fields.Selection(
        [("HighSpeed", "HighSpeed"), ("MediumSpeed", "MediumSpeed"), ("LowMediumSpeed", "LowMediumSpeed"),
         ("LowSpeed", "LowSpeed")],
        default="HighSpeed",
        string="Speed Policy",
    )

    def test_nodeless_server_connection(self):
        try:
            server_url = self.nodeless_server_url + "/api/v1/status"
            headers = {"Authorization": "Bearer %s" % (self.nodeless_api_key), "Content-Type": "application/json",
                       "Accept": "application/json"}
            response = requests.request(method="GET", url=server_url, headers=headers)
            is_success = True if response.status_code == 200 else False
            return is_success
        except Exception as e:
            raise UserError(_("Test Connection Error: %s", e.args))

    def action_test_connection(self):
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


