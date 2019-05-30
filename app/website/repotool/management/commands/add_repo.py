from django.core.management.base import BaseCommand
from django.conf import settings
import pygit2

class Command(BaseCommand):
	help = 'Adds a repository into the system'
	credentials = pygit2.UserPass(os.environ.get('GIT_USER'), os.environ.get('GIT_PASS'))

	def add_arguments(self, parser):
		parser.add_argument('urls', nargs='+', type=str)

	def handle(self, *args, **options):
		for url in options['urls']:
			try:
				path = '{}/{}'.format(settings.REPOSITORY_DIR, url.split('/')[-1])
				callbacks = pygit2.RemoteCallbacks(self.credentials)
				pygit2.clone_repository(url, path, callbacks=callbacks)
				self.stdout.write(self.style.SUCCESS('Success'))
			except Exception as e:
				self.stdout.write(e)
				self.stdout.write(self.style.ERROR('Something went wrong'))
