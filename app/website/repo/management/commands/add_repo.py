from django.core.management.base import BaseCommand
from django.conf import settings
import pygit2

class Command(BaseCommand):
	help = 'Adds a repository into the system'

	def add_arguments(self, parser):
		parser.add_argument('--urls', nargs='+', type=str)
		parser.add_argument('--user', type=str)
		parser.add_argument('--password', type=str)

	def handle(self, *args, **options):
		try:
			user = options['user']
			password = options['password']
			credentials = pygit2.UserPass(user, password)
		except Exception as e:
			self.stdout.write(e)
			self.stdout.write(self.style.ERROR('Something went wrong'))

		for url in options['urls']:
			try:
				path = '{}/{}'.format(settings.REPOSITORY_DIR, url.split('/')[-1])
				callbacks = pygit2.RemoteCallbacks(credentials)
				pygit2.clone_repository(url, path[:-4], callbacks=callbacks)
				self.stdout.write(self.style.SUCCESS('Success'))
			except Exception as e:
				self.stdout.write(e)
				self.stdout.write(self.style.ERROR('Something went wrong'))
