from flask_testing import TestCase
from flask import url_for
from requests_mock import mock
from application import app
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_home(self):
        classes = 'Slayer'
        gender = 'Male'
        status = {'birth_place': 'Arad', 'subclass': 'Blade Master'}

        with requests_mock.Mocker() as m:
            m.get('http://service_2:5000/get_classes',text = classes)
            m.get('http://service_3:5000/get_gender',text = gender)
            m.post('http://service_4:5000/post_status',json = status)
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code,200)



