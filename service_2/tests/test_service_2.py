from flask import url_for
from flask_testing import TestCase
from app import app, classes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_get_classes(self):
        response = self.client.get(url_for('get_classes'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.data.decode(), classes)

        
