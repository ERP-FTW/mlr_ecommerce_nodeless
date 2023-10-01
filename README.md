# mlr_ecommerce_nodeless_2
Lightning Rod Ecommcerce BTCpay Readme

Overview
This custom module for Odoo 16+ adds Nodeless.io as a payment provider to the Ecommerce application. Nodeless.io is a Bitcoin payment gateway/provider which is queried by API calls from Odoo. Nodeless.io account access by API is provided to Odoo and a Bitcoin onchain/lightning option is added to the customer by checkout portal link. If the Bitcoin payment option is selected by a customer, they are forwarded to a BTCpay site with a created invoice and QR code for payment. After the payment is confirmed the customer can be redirected back to the Odoo online store receipt page and the order is registered and queued.

Prerequisites (versions)
<br>Compatible with Odoo 16
<br>Postgres 14+
<br>Nodeless.io account
<br>mlr_ecommerce_cryptopayments custom module

Installation (see this video for tutorial on Odoo module installation)
1. Download repository and place extracted folder in the Odoo addons folder.
2. Login to Odoo database to upgrade and enable developer mode under settings.
3. Under apps Update the App list.
4. Search for the module (MLR) and install.

Setup

1. In Odoo navigate to Website-> Ecommerce -> Payment Providers.
![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless_2/assets/124227412/c4f16673-99d1-4dac-b7b0-e731e2336a33)
2. Click on Nodeless to open the record.
4. Enter a Name for the Instance. 
5. Login into Nodeless.io and navigate to Account -> API Key. Create a key for use with Odoo.
6. From Nodeless copy the following information and paste in the Odoo Instance record: the server base URL, API key, and store ID.
7. Click Connect to Nodeless to verify the information is correct. If it is correct a green popup will affirm so, if it is incorrect a red popup will appear.
![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless_2/assets/124227412/6a1311bf-4d92-4bff-abbb-0f67b73ab3b5)
9. In Configuration -> Payment Form select the icon for lightning, in Configuration -> Payment Followup select the Payment Journal.
![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless_2/assets/124227412/11649f36-85e7-4c24-9eb1-766edd1a49f7)
10. Select Enable to make BTCpay instance a current method and save (the first time a new Accounting Journal BTCpay will be created and used for recording transactions).
   

Operation
1. A customer will navigate to the Shop section of the website and add items to the cart. After initiating the checkout and filling in customer information the available payment methods will be displayed.
![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless_2/assets/124227412/cb6a9f7b-85d8-4e37-b522-53015a4d0328)
3. The customer can select the Bitcoin Lightning option and directions will appear below.
![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless_2/assets/124227412/a4ef4c09-b5b9-4253-8bad-15655cd225d0)
4. After clicking Pay Now  the customer will be taken to a Nodeless page with the invoice and QR code to be paid.
![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless_2/assets/124227412/4be87cc5-7d7e-4e48-922c-99992659ba0c)
5. The customer scans the QR code or pastes the invoice text as a send from their lightning wallet.
6. Upon Nodeless confirmation of the order the customer will be returned automatically to the receipt page of the Odoo site.
8. Odoo will process the order and create a sales order for fulfillment.
![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless_2/assets/124227412/ea135de5-f370-4b6f-8aca-8193588e80b1)

