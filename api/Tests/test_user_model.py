from django.test import TestCase
from api.models import User

class UserModelTestCase(TestCase):

    def test_user_saves_to_db(self):
        User.objects.create(username='Thrasher',
                            phone_number='7196639883')
        user = User.objects.get(username='Thrasher')
        count = User.objects.count()
        self.assertEqual(user.username, 'Thrasher')
        self.assertEqual(user.phone_number, '7196639883')
        self.assertEqual(count, 1)

    def test_additional_user_saves(self):
        User.objects.create(username='Thrasher',
                            phone_number='7196639883',)
        first_count = User.objects.count()

        User.objects.create(username='Fluffy',
                            phone_number='7198839888',)
        second_count = User.objects.count()
        last_user = User.objects.last()
        self.assertEqual(last_user.username, 'Fluffy')
        self.assertEqual(last_user.phone_number, '7198839888')
        self.assertEqual(second_count, 2)
