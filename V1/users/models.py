from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def update_user(self, user_attrs):
        if 'username' in user_attrs.keys():
            self.username = user_attrs['username']
        if 'phone_number' in user_attrs.keys():
            self.phone_number = user_attrs['phone_number']
        self.save()
        return self

    class Meta:
        db_table = 'users'
