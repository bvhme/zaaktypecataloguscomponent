from .base import *

#
# Standard Django settings.
#
DEBUG = False
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'secret-key'

# Which hosts are allowed to access the project.
ALLOWED_HOSTS = ['localhost', '127.0.0.1',]

# Redis cache backend
# NOTE: If you do not use a cache backend, do not use a session backend or
# cached template loaders that rely on a backend.
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",  # NOTE: watch out for multiple projects using the same cache!
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "IGNORE_EXCEPTIONS": True,
        }
    }
}

# Caching sessions.
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = "default"

# Caching templates.
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', RAW_TEMPLATE_LOADERS),
]

LOGGING['loggers'].update({
    '': {
        'handlers': ['project'],
        'level': 'WARNING',
        'propagate': False,
    },
    'django': {
        'handlers': ['django'],
        'level': 'WARNING',
        'propagate': True,
    },
    'django.security.DisallowedHost': {
        'handlers': ['django'],
        'level': 'CRITICAL',
        'propagate': False,
    },
})

# Set these to True if you are using HTTPS.
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = False
X_FRAME_OPTIONS = 'DENY'
# Only set this when we're behind Nginx and this header is set.
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#
# Custom settings
#
# Show active environment in admin.
ENVIRONMENT = 'development'
SHOW_ALERT = True

# Override settings with local settings.
try:
    from .local import *
except ImportError:
    pass
