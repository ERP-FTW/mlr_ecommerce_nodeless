{
    "name": "MLR ecommerce Nodeless 2",
    "summary": "MLR ecommerce Nodeless 2",
    "author": "ERP",
    "website": "https://www.milightningrod.com",
    "category": "Ecommerce",
    "version": "1.0",
    "depends": ["website", "mlr_ecommerce_cryptopayments"],
    "data": [
        "views/nodeless_payment_template.xml",
        "data/nodeless_payment_provider_data.xml",
        "views/nodeless_payment_form.xml",
        "data/nodeless_payment_icons.xml",
        "views/nodeless_payment_provider.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    "license": "OPL-1",
}
