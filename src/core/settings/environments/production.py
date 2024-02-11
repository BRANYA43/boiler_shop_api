"""
Production setting file
"""

from core.settings import env

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': env.get('POSTGRES_HOST'),
        'PORT': env.get('POSTGRES_PORT'),
        'NAME': env.get('POSTGRES_DB'),
        'USER': env.get('POSTGRES_USER'),
        'PASSWORD': env.get('POSTGRES_PASSWORD'),
    }
}
