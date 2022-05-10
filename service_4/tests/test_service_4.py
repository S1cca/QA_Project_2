from flask import url_for
from flask_testing import TestCase
from service_2.app import app, classes
from service_3.app import app, gender
from service_4.app import app, Birth_Place, post_status
from requests_mock import mock

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_get_status(self):
        for i in classes:
            for j in range(50):
                content = {'classes': i,'gender':j}
                response = self.client.post(url_for('post_status'), json=content)
                self.assertEqual(response.status_code, 200)

                ##need full test here

        


        
