from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, User
from django.db import models


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    telegram_id = models.CharField(max_length=1000)
    alexa_id = models.CharField(max_length=1000)
    moodle_id = models.CharField(max_length=1000)
    birth_date = models.CharField(max_length=50, default='01-01-1901')
    faculty = models.CharField(default="", max_length=200)

    # REQUIRED_FIELDS = ('user', )
    # USERNAME_FIELD = 'username'

    def __str__(self):
        return self.user.username