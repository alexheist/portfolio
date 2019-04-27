from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='m+^qxi90bpl_ptp1o(iuv_-%9o_gzb8f-yovz^9(2i!1s19-#a')

DEBUG = env.bool('DJANGO_DEBUG', default=True)

ALLOWED_HOSTS = ['*']

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': str(ROOT_DIR.path('db.sqlite3')),
	}
}
