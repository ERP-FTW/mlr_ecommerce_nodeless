# mlr_ecommerce_nodeless_2
Lightning Rod Ecommerce Nodeless Readme

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
![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless/assets/124227412/80353de9-a89e-4ae9-a1a8-0128c14efdac)
2. Click on Nodeless to open the record.
3. Enter a Name for the Instance. 
4. Login into Nodeless.io and navigate to Account -> API Key. Create a key for use with Odoo.
5. From Nodeless copy the following information and paste in the Odoo Instance record: the server base URL, API key, and store ID. Enter a minimum ($0.30) and maximum ($1000) fiat amount.
6. Click Connect to Nodeless to verify the information is correct. If it is correct a green popup will affirm so, if it is incorrect a red popup will appear.
![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless/assets/124227412/22873a92-9913-472b-b3d4-a0e4b541ac64)
7. In Configuration -> Payment Form select the icon for lightning, in Configuration -> Payment Followup select the Payment Journal.
![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless/assets/124227412/003928a1-4092-4d5e-b104-dd33842ee86f)
8. Select Enable to make Nodeless instance a current method and save.
9. To have an invoice automatically created which will show the payment was post go to Website -> Configuration -> Settings -> Invoicing -> Automatic Invoicing.
10. Activate the Sales application if wishing to use online payment links for Invoices. Enable Sales -> Configuration -> Settings -> Quotations & Orders -> Online Payment.
   

Operation
Online Shop
1. A customer will navigate to the Shop section of the website and add items to the cart. After initiating the checkout and filling in customer information the available payment methods will be displayed.
![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless/assets/124227412/8940bde0-abb2-47a5-82a5-80a68b0d9d78)
2. The customer can select the Nodeless option and directions will appear below.
![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless/assets/124227412/579b9870-b956-48f8-a735-c108909e4ec7)
3. After clicking Pay Now  the customer will be taken to a Nodeless page with the invoice and QR code to be paid.
![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless/assets/124227412/cf8ff84f-3075-4e8e-9ba4-58de30291aad)
4. The customer scans the QR code or pastes the invoice text as a send from their lightning wallet.
 ![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless/assets/124227412/0ecea196-3365-489a-9b3d-4c2e37fae502)
5. Upon Nodeless confirmation of the order the customer will be returned automatically to the receipt page of the Odoo site.
   ![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless/assets/124227412/8b79428d-dfd2-4849-b905-d1f2e97a9804)
6. Odoo will process the order and create a sales order for fulfillment.
![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless/assets/124227412/26aa78d4-45e9-4189-8138-595b6c0bd53d)

Invoicing
1. Create a quote from Sales -> Orders -> Quotes -> New. Enter the customer, timeframe, and product information. Create the quote and send to a customer.
![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless/assets/124227412/8532224e-5803-44d3-aad8-a5d893dad793)
2. Confirm the quote once accepted to change status to a Sales Order.
![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless/assets/124227412/41604fbd-fe42-4bb4-b788-660fc864f93b)
3. Click Create Invoice to make the invoice for Billing. Select your preferred options. Confirm the Draft Invoice to finalize it.
![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless/assets/124227412/f4c92e96-4ce8-42fa-ad65-6121f783c052)
4. Create the payment link to send to the customer for online payment with Action > Generate a Payment Link.
![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless/assets/124227412/dcb4a615-a6ac-42b8-9c13-981d70b424dd)
5. Copy the payment link and use the Send & Print button to convey to the customer.
![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless/assets/124227412/779fe05e-cbc3-4c85-87a6-6f9f6efc0d4f)
6. Visiting the payment link will show the enabled online payment providers.
![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless/assets/124227412/6894bbb8-dea7-42b7-8809-67649c351d11)
7. The customer will be taken to the third-party site and returned upon payment.
   ![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless/assets/124227412/4e050325-1be2-477b-b58e-f331022d7327)
8.The customer will be taken to a payment confirmation page and have access to a customer account history portal if they have an account.
![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless/assets/124227412/4b266382-cfdc-483d-9ccf-1909a9ac62c9)
9. Viewing the invoice will show that it is paid.
![image](https://github.com/ERP-FTW/mlr_ecommerce_nodeless/assets/124227412/c0ff4dba-12d3-429e-a7f4-3ce295eebc76)
