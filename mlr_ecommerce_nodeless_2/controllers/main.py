# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import pprint
import requests
import json

from odoo.http import Controller, request, route

_logger = logging.getLogger(__name__)


# TODO
# auth should be public or something else for create invoice?

class CustomController(Controller):
    _return_url = '/payment/nodeless/return'
    _create_invoice = '/payment/nodeless/createInvoice'

    def nodelessApiCall(self, payload, api, method):
        try:
            _logger.info(f"Called Nodeless nodelessApiCall. Passed args are {payload}")
            crypto_details = request.env['payment.provider'].sudo().search([('code', '=', 'nodeless')])
            base_url = crypto_details.mapped('crypto_server_url')[0]
            api_key = crypto_details.mapped('crypto_api_key')[0]
            store_id = crypto_details.mapped('nodeless_store_id')[0]
            server_url = f"{base_url}{api.format(store_id=store_id)}"
            headers = {"Authorization": "Bearer %s" % (api_key), "Content-Type": "application/json", "Accept": "application/json"}
            _logger.info(f"value of server_url is {server_url}, method is {method}, and payload is {payload}")
            if method == "GET":
                apiRes = requests.get(server_url, headers=headers)
            elif method == "POST":
                apiRes = requests.post(server_url, data=json.dumps(payload), headers=headers)
            _logger.info(f"Completed Nodeless nodelessApiCall. Passing back {apiRes.json()}")
            return apiRes
        except:
            _logger.info(f"An exception occurred with Nodeless nodelessApiCall.")
            return

    @route(_return_url, type='http', auth='public', methods=['GET', 'POST'], csrf=False)
    def custom_process_transaction(self, **post):
        try:
            _logger.info(f"Called Nodeless custom_process_transaction. Passed args are {post}")
            trn = request.env['payment.transaction'].sudo().search([('reference', '=', post['ref']),('provider_code', '=', 'nodeless')])
            crypto_invoice_id = trn.mapped('crypto_invoice_id')[0]
            trn_amount = trn.mapped('amount')[0]
            apiRes = self.nodelessApiCall({}, '/api/v1/store/{store_id}/invoice/' + crypto_invoice_id, 'GET')
            _logger.info(f"api response from return is {apiRes.json()}")
            if apiRes.status_code == 200:
                resJson = apiRes.json()['data']
                if resJson.get('status') == "paid":
                    sats = float(resJson.get('satsAmount'))
                    btc = sats/100000000
                    conversion_rate = trn_amount/btc
                    trn.write({
                        'crypto_payment': 'true',
                        'crypto_payment_type': 'BTC',
                        'crypto_conversion_rate': conversion_rate,
                        'crypto_payment_link': resJson.get('checkoutLink'),
                        'crypto_invoiced_crypto_amount': btc,
                        'nodeless_invoiced_sat_amount': sats,})
                    trn._set_done()
                else:
                    _logger.info(f"Issue Nodeless custom_process_transaction, status is  Passing back {resJson['status']}")
                    trn._set_error(f"Payment failed!, Nodeless Invoice status: {resJson['status']}")
            else:
                _logger.info(f"Issue while checking Nodeless invoice, retry after sometime, if issue persits, please contact support or write to us. Issue response code {apiRes.status_code}")
                trn._set_error(f"Issue while checking Nodeless invoice, retry after sometime, if issue persits, please contact support or write to us. Issue response code {apiRes.status_code}")
            _logger.info(f"Completed Nodeless custom_process_transaction. Passing back {apiRes.json()}")
            return request.redirect('/payment/status')
        except:
            _logger.info(f"An exception occurred with Nodeless custom_process_transaction.")
            trn._set_error(f"Issue while checking Nodeless invoice, retry after sometime, if issue persits, please contact support. An exception occurred in Nodeless custom_process_transaction,")
            return request.redirect('/payment/status')

    @route(_create_invoice, type='http', auth='public', methods=['POST'], csrf=False)
    def create_invoice(self, **post):
        try:
            _logger.info(f"Called Nodeless create_invoice. Passed args are {post}")
            trn = request.env['payment.transaction'].sudo().search([('reference', '=', post['ref']), ('provider_code', '=', 'nodeless')])
            crypto_details = request.env['payment.provider'].sudo().search([('code', '=', 'nodeless')])
            crypto_min_amount = crypto_details.mapped('crypto_min_amount')[0]
            crypto_max_amount = crypto_details.mapped('crypto_max_amount')[0]
            if float(post['amount']) <= crypto_min_amount or float(post['amount']) >= crypto_max_amount:
                #return {"type": "ir.actions.client","tag": "display_notification","params": {"title": "below min","message": "below amount","sticky": False,"type": "danger"}
                return request.redirect('/shop/payment')
            web_base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
            checkout = f"{web_base_url}/payment/nodeless/return?ref={post['ref']}"
            payload = {
                "amount": post['amount'],
                "redirectUrl": checkout,
                "currency": post['currency'],
                "metadata": [post['ref']]}
            apiRes = self.nodelessApiCall(payload, '/api/v1/store/{store_id}/invoice', 'POST')
            apiRes_json = apiRes.json()['data']
            if apiRes.status_code == 201:
                trn.write({'crypto_invoice_id': apiRes_json.get('id')})
                _logger.info(f"Completed Nodeless create_invoice. Passing back {apiRes_json.get('checkoutLink')}")
                return request.redirect(apiRes_json.get('checkoutLink'), local=False)
            else:
                trn = request.env['payment.transaction'].sudo().search([('reference', '=', post['ref']), ('provider_code', '=', 'nodeless')])
                _logger.info("Issue while creating Nodeless invoice, retry after sometime, if issue persists, please contact support or write to us")
                trn._set_error("Issue while creating Nodeless invoice, retry after sometime, if issue persists, please contact support or write to us")
                return request.redirect('/payment/status')
        except:
            _logger.info("Issue while creating Nodeless invoice, retry after sometime, if issue persits, please contact support. An exception occurred in Nodeless create_invoice")
            trn._set_error("Issue while creating Nodeless invoice, retry after sometime, if issue persits, please contact support. An exception occurred in Nodeless create_invoice")
            return request.redirect('/payment/status')
