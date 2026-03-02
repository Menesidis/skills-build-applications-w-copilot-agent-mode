from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass', team=team)
        self.assertEqual(str(user), 'testuser')

    def test_activity_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=10, distance=2.5)
        self.assertEqual(str(activity), 'testuser - run')

    def test_workout_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass', team=team)
        workout = Workout.objects.create(user=user, name='Pushups', reps=10)
        self.assertEqual(str(workout), 'testuser - Pushups')

    def test_leaderboard_create(self):
        team = Team.objects.create(name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, points=50)
        self.assertEqual(str(leaderboard), 'Test Team - 50')
