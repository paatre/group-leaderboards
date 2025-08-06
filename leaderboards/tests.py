from datetime import timedelta
from django.contrib.auth.models import User
from django.test import TestCase
from .models import RunningActivity


class RunningActivityTestCase(TestCase):
    def test_pace_can_be_calculated_from_distance_and_duration(self):
        user = User.objects.create_user(
            username="testuser",
            password="testpassword",
        )
        activity = RunningActivity(
            activity_date="2023-10-01",
            distance=10.0,
            duration=timedelta(minutes=52),
            user=user,
        )
        activity.save()
        self.assertEqual(activity.pace, timedelta(minutes=5, seconds=12))
