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

# Containers are assumed to be test environments by default
DEBUG = True

STATIC_ROOT = '/respa/static'
MEDIA_ROOT = '/respa/media'
STATIC_URL = '/respa/static/'
MEDIA_URL = '/respa/media/'

LOGIN_REDIRECT_URL = 'https://example.com/respa/admin/'
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

RESPA_MAILS_ENABLED = False
