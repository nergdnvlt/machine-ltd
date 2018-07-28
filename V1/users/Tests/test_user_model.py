from django.test import TestCase
from V1.users.models import User

# python manage.py test V1/users/tests

class UserModelTestCase(TestCase):

    def test_user_saves_to_db(self):
        User.objects.create(username='Thrasher',
                            phone_number='+17196639883')
        user = User.objects.get(username='Thrasher')
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

    def test_update_username_saves(self):
        User.objects.create(username='Thrasher',
                            phone_number='+17196639883',)
        user = User.objects.last()
        user.update_user({'username': 'papaWar'})

        self.assertEqual(user.username, 'papaWar')
        self.assertEqual(user.phone_number, '+17196639883')

    def test_update_phone_num_saves(self):
        User.objects.create(username='Thrasher',
                            phone_number='+17196639883',)
        user = User.objects.last()
        user.update_user({'phone_number': '+17196851210'})

        self.assertEqual(user.username, 'Thrasher')
        self.assertEqual(user.phone_number, '+17196851210')
