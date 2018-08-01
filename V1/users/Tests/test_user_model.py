from django.test import TestCase
from django.db import IntegrityError
from V1.users.models import User
from IPython import embed

# python manage.py test V1/users/tests
class UserModelTestCase(TestCase):

    def test_user_saves_to_db(self):
        user = User.objects.create(username='Thrasher',
                            phone_number='+17196639883')
        count = User.objects.count()
        self.assertEqual(user.username, 'Thrasher')
        self.assertEqual(user.phone_number, '+17196639883')
        self.assertEqual(count, 1)

    def test_additional_user_saves(self):
        User.objects.create(username='Thrasher',
                            phone_number='+17196639883',)
        first_count = User.objects.count()

        User.objects.create(username='Fluffy',
                            phone_number='+17198839888',)
        second_count = User.objects.count()
        last_user = User.objects.last()
        self.assertEqual(last_user.username, 'Fluffy')
        self.assertEqual(last_user.phone_number, '+17198839888')
        self.assertEqual(second_count, 2)


    def test_uniqueness_of_username(self):
        user_1 = User.objects.create(username='Thrasher',
                            phone_number='+17196639883',)

        with self.assertRaises(IntegrityError):
            User.objects.create(username='Thrasher',
                                phone_number='+17196639883',)
