from flask import render_template, request, redirect, url_for, flash
from application import app, db
# from application.model import Character
import requests, json

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    classes = requests.get('http://service_2:5000/get_classes').text
    gender = requests.get('http://service_3:5000/get_gender').text
    character = {'classes': classes, 'gender': gender}
    status = requests.post('http://service_4:5000/post_status', json=character).json()

    return render_template('home.html',classes=classes, gender=gender, status = status )