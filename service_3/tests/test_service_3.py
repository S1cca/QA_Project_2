from flask import url_for
from flask_testing import TestCase
from application import app, gender

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_get_gender(self):
        response = self.client.get(url_for('get_gender'))
        self.assertEqual(response.status_code, 200)
        for i in range(50):
            self.assertIn(response.data.decode(), gender)

        
