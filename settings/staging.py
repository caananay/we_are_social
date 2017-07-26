from base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_rGZJw1qEwDxms3NDLas0v8V3')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_hjx1XiGxWexYlRtisHu1Z0dM')

#PayPal Settings
SITE_URL= 'https://pure-spire-93905.herokuapp.com/'
PAYPAL_NOTIFY_URL = 'https://pure-spire-93905.herokuapp.com/'
PAYPAL_RECEIVER_EMAIL ='doncanny-facilitator@yahoo.com'