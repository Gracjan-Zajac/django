from django.test import TestCase
from decouple import config
from django.contrib.auth.password_validation import validate_password


class TryDjangoConfigTests(TestCase):
    def test_secret_key_strength(self):
        SECRET_KEY = config("SECRET_KEY")
        try:
            validate_password(SECRET_KEY)
        except Exception as e:
            msg = f"Weak SECRET KEY {e.messages}"
            self.fail(msg)
