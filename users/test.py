from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class RegisterTest(TestCase):
    def test_register_success(self):
        response = self.client.post(
            reverse('users:register'),
            data={
                'username': "hasanboy",
                'first_name': "Hasanboy",
                'last_name': "Mamatkarimov",
                'email': "hasanboysalom@gmail.com",
                'password': "1234",
                'password_config': "1234"
            }
        )

        user_count = User.objects.count()
        self.assertEqual(user_count, 1)
        print(user_count)

        user = User.objects.get(username="hasanboy")
        self.assertEqual(user.username, "hasanboy")
        self.assertEqual(user.first_name, "Hasanboy")
        self.assertEqual(user.email, "hasanboysalom@gmail.com")
        self.assertNotEqual(user.password, "1234")  # Checking password hash

# class LoginTest(TestCase):
#     def test_login(self):
#         response = self.client.post(
#             reverse('users:login'),
#             data={
#                 'username': "hasanboy",
#                 'password': "1234",
#             }
#         )
#         user_count = User.objects.count()
#         print("User count:", user_count)
#         self.assertEqual(user_count, 1)
#
#         user = User.objects.get(username="hasanboy")
#
#         self.assertEqual(user.username, "hasanboy")
#
#         self.assertTrue(user.check_password("1234"))

    def test_username_fields(self):
        response = self.client.post(
            reverse('users:login'),
            data={
                'username': "root",
                'first_name': "Hasanboy",
                'last_name': "Mamatkarimov",
                'email': "hasanboysalom@gmail.com",
                'password': "1234",
                'password_config': "1234"
            }
        )
        form=response.context['form']

        user_count = User.objects.count()
        self.assertEqual(user_count,0)
        self.assertTrue(form.errors)
        self.assertIn("username",form.errors.keys())
        self.assertEqual(form.errors['username'],["Usernamegiz 5-30 oraligida bo'lish kerak"])



    def test_password_fields(self):
        response = self.client.post(
            reverse('users:register'),
            data={
                'username': "hasanboy",
                'first_name': "Hasanboy",
                'last_name': "Mamatkarimov",
                'email': "hasanboysalom@gmail.com",
                'password': "1234",
                'password_config': "12341211"
            }
        )
        form = response.context['form']

        user_count = User.objects.count()
        self.assertEqual(user_count, 0)
        self.assertTrue(form.errors)
        self.assertIn("password_config", form.errors.keys())
        self.assertEqual(form.errors['password_config'],["Parrolaringizni qayta solishtiring"])


    def test_email_fields(self):
        response = self.client.post(
            reverse('users:register'),
            data={
                'username': "hasanboy",
                'first_name': "Hasanboy",
                'last_name': "Mamatkarimov",
                'email': "hasanboysalom",
                'password': "1234",
                'password_config': "1234"
            }
        )
        form = response.context['form']

        user_count = User.objects.count()
        self.assertEqual(user_count, 0)
        self.assertTrue(form.errors)
        self.assertIn("email", form.errors.keys())
        self.assertEqual(form.errors['email'],["Enter a valid email address."])


class Login(TestCase):
    def test_login_success(self):
        user=User.objects.create(username="hasanboy",first_name='Hasanboy',last_name='Mamatkarimov')
        user.set_password('root')
        user.save()
        self.client.post(
            reverse('users:login'),
            date={
                'username':'hasanboy',
                'password':"12345"
            }
        )
        user_count=User.objects.count()
        self.assertEqual(user.is_authenticated)