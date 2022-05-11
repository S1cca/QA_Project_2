from flask import url_for
from flask_testing import TestCase
from app import app, post_status, Male_Slayer, Female_Slayer, Male_Fighter, Female_Fighter, Male_Mage, Female_Mage, Birth_Place
import random

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_get_status(self):
        response = self.client.post(url_for('post_status'), json={'classes': 'Slayer', 'gender':'Male'})
        self.assertEqual(response.status_code, 200)
    
    def test_birthplace(self):
        response = self.client.post(url_for('post_status'), json={'classes': 'Slayer', 'gender':'Male'})
        self.assertIn("birth_place",response.data.decode())

    def test_MaleSlayer(self):
        subclass = random.choice(list(Male_Slayer))
        response = self.client.post(url_for('post_status'), json={'classes': 'Slayer', 'gender':'Male'})
        self.assertIn("subclass",response.data.decode())
    
    def test_FemaleSlayer(self):
        subclass = random.choice(list(Female_Slayer))
        response = self.client.post(url_for('post_status'), json={'classes': 'Slayer', 'gender':'Female'})
        self.assertIn("subclass",response.data.decode())
        
    def test_MaleFighter(self):
        subclass = random.choice(list(Male_Fighter))
        response = self.client.post(url_for('post_status'), json={'classes': 'Fighter', 'gender':'Male'})
        self.assertIn("subclass",response.data.decode())
    
    def test_MaleMage(self):
        subclass = random.choice(list(Male_Mage))
        response = self.client.post(url_for('post_status'), json={'classes': 'Mage', 'gender':'Male'})
        self.assertIn("subclass",response.data.decode())

    def test_MaleMage(self):
        subclass = random.choice(list(Female_Mage))
        response = self.client.post(url_for('post_status'), json={'classes': 'Mage', 'gender':'Female'})
        self.assertIn("subclass",response.data.decode())
