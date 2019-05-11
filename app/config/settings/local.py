from .base import *

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = int(os.environ.get('DJANGO_DEBUG', default=0))

ALLOWED_HOSTS = ['*']

DATABASES = {
	'default': {
		'ENGINE': os.environ.get('DB_ENGINE'),
		'NAME': os.environ.get('DB_NAME'),
		'USER': os.environ.get('DB_USER'),
		'PASSWORD': os.environ.get('DB_PASSWORD'),
		'HOST': os.environ.get('DB_HOST'),
		'PORT': os.environ.get('DB_PORT'),
	}
}

RECAPTCHA_PUBLIC_KEY = '6Lf676IUAAAAADMzDrQ0Quakf2KPsrHyDWT15snH'
RECAPTCHA_PRIVATE_KEY = '6Lf676IUAAAAACJvc9iEgJP3UKjRIcgIdDmY_BUz'
