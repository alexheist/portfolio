from django.core.management.base import BaseCommand
from django.conf import settings
from pygit2 import clone_repository

class Command(BaseCommand):
	help = 'Adds a repository into the system'

	def add_arguments(self, parser):
		parser.add_argument('urls', nargs='+', type=str)

	def handle(self, *args, **options):
		for url in options['urls']:
			try:
				path = '{}/{}'.format(settings.REPOSITORY_DIR, url.split('/')[-1])
				clone_repository(url, path)
				self.stdout.write(self.style.SUCCESS('Success'))
			except Exception as e:
				self.stdout.write(e)
				self.stdout.write(self.style.ERROR('Something went wrong'))
