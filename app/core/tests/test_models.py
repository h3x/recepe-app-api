from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    
    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful """
        email = "test@test.com"
        password = 'TheAdministrator1'

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalised(self):
        """ Test the email for a new user is normalised """
        email = "test90@TEST.com"
        password = 'TheAdministrator1'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises error """
        password = 'TheAdministrator1'
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password=password,
            )

    def test_super_user_is_created_with_correct_settings(self):
        """ Test creating a new super user"""
        user = get_user_model().objects.create_superuser(
            email="test123@test.com",
            password="test123",
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)