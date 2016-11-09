DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'postgres',
        'USER': 'postgres',
        'CONN_MAX_AGE': 600,
        'HOST': 'db',
        'PORT': 5432,
        'ATOMIC_REQUESTS': True,
    }
}

DEBUG = True

STATIC_ROOT = '/respa/static'
MEDIA_ROOT = '/respa/media'
STATIC_URL = '/respa/static/'
MEDIA_URL = '/respa/media/'

LOGIN_REDIRECT_URL = 'https://api.hel.fi/respa/admin/'
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DEFAULT_FROM_EMAIL = 'Varaamo <noreply@hel.ninja>'
EMAIL_BACKEND = 'anymail.backends.mailgun.MailgunBackend'
RESPA_MAILS_FROM_ADDRESS = DEFAULT_FROM_EMAIL
RESPA_MAILS_ENABLED = True
