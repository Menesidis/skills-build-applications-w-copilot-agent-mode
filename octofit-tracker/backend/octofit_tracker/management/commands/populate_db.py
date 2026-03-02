from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as octo_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        self.stdout.write(self.style.WARNING('Deleting existing data...'))
        octo_models.Team.objects.all().delete()
        octo_models.Activity.objects.all().delete()
        octo_models.Leaderboard.objects.all().delete()
        octo_models.Workout.objects.all().delete()
        get_user_model().objects.all().delete()

        # Create teams
        marvel = octo_models.Team.objects.create(name='Team Marvel')
        dc = octo_models.Team.objects.create(name='Team DC')

        # Create users
        User = get_user_model()
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc),
            User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc),
        ]

        # Create activities
        for user in users:
            octo_models.Activity.objects.create(user=user, type='run', duration=30, distance=5)
            octo_models.Activity.objects.create(user=user, type='cycle', duration=60, distance=20)

        # Create workouts
        for user in users:
            octo_models.Workout.objects.create(user=user, name='Pushups', reps=20)
            octo_models.Workout.objects.create(user=user, name='Situps', reps=30)

        # Create leaderboard
        for team in [marvel, dc]:
            octo_models.Leaderboard.objects.create(team=team, points=100)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
