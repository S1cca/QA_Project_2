from flask import url_for
from flask_testing import TestCase
from service_2.app import classes
from service_3.app import gender
from app import app, post_status, Male_Slayer, Female_Slayer, Male_Fighter, Female_Fighter, Male_Mage, Female_Mage, Birth_Place

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_get_status(self):
        for i in classes:
            for j in gender:
                content = {'classes': i,'gender':j}
                response = self.client.post(url_for('post_status'), json=content)
                self.assertEqual(response.status_code, 200)

    def test_subclass(self):
        for i in classes:
            for j in gender:
                content = {'classes': i,'gender':j}
                response = self.client.post(url_for('post_status'), json=content)
                if gender == "Male" and classes =="Slayer":
                    self.assertIn(response.data.decode(), Male_Slayer)

                elif gender == "Female" and classes =="Slayer":
                    self.assertIn(response.data.decode(), Female_Slayer)

                elif gender == "Male" and classes =="Fighter":
                    self.assertIn(response.data.decode(), Male_Fighter)

                elif gender == "Female" and classes =="Fighter":
                    self.assertIn(response.data.decode(), Female_Fighter)
                
                elif gender == "Male" and classes =="Mage":
                    self.assertIn(response.data.decode(), Male_Mage)

                elif gender == "Female" and classes =="Mage":
                    self.assertIn(response.data.decode(), Female_mage)

    def test_birthplace(self):
        for i in classes:
            for j in gender:
                content = {'classes': i,'gender':j}
                response = self.client.post(url_for('post_status'), json=content)
                self.assertIn("birth_place",response.data.decode())
