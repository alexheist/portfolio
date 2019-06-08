import os
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from pygit2 import Repository

# Create your views here.
class LandingView(TemplateView):
	template_name = 'repo/pages/landing.html'

	# TODO: Add functionality so that I can grab every repository in the directory
	def get_context_data(self, **kwargs):
		context = super(LandingView, self).get_context_data(**kwargs)
		repos = {}

		repo_names = [d for d in os.listdir(settings.REPOSITORY_DIR) if os.path.isdir(os.path.join(settings.REPOSITORY_DIR, d))] # Gets names of repos in the repository directory

		for repo in repo_names:
			data = Repository('{}/{}/.git'.format(settings.REPOSITORY_DIR, repo))
			repos['dir'] = dir(data)
			repos[repo] = data

		context['repositories'] = repos

		return context
