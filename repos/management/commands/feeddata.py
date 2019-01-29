
# https://docs.djangoproject.com/en/2.1/howto/custom-management-commands/

import requests
import json

from django.core.management.base import BaseCommand, CommandError
from repos.models import Repo
from projects.models import Project

from operator import add


class Command(BaseCommand):
    help = 'Retrieves data from github'

#    def add_arguments(self, parser):
#        parser.add_argument('poll_id', nargs='+', type=int)


    def handle(self, *args, **options):
        repos = Repo.objects.all()
        for repo in repos:
            print(len(repo.values))
            if len(repo.values) < 50:
                print( 'Retrieveing ' + repo.name )
                r = requests.get('https://api.github.com/repos/' + repo.name + '/stats/commit_activity')
                repo.values = json.dumps( list( map( lambda w : w['total'], json.loads(r.text) )) )
                repo.save()
                self.stdout.write(self.style.SUCCESS('Retrieving "%s"' % repo.name ))
            else:
                self.stdout.write(('Skipping "%s"' % repo.name ))

        self.update_projects()

    def update_projects(self):
        projects = Project.objects.all()
        for project in projects:
            self.stdout.write( project.name )
            vals = [0] * 52
            repos = project.repo_set.all()
            for repo in repos:
                self.stdout.write( repo.name )
                vals = list( map(add, vals, json.loads(repo.values) )  )
            print(vals)
            project.values = json.dumps(vals)
            project.save()