import random
import string

from django.test import TestCase
from django.contrib.auth import get_user_model


class StudentsManagerTests(TestCase):

    def test_create_student(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='foo', username=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5)))


    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser('super@user.com', 'foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)