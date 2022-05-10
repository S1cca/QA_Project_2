from flask_testing import TestCase
from flask import url_for
from requests_mock import mock
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    classes = "Slayer"
    gender = "Male"
    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        # self.assertIn("You have made a Slayer", response.data.decode())
        # self.assertIn("Born in Unkown", response.data.decode())

