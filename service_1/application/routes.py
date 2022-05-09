from flask import render_template, request, redirect, url_for, flash
from application import app, db
from application.model import Character
import requests, json


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    # Classess = requests.get('http://service_2:5002/get_classes').text
    # Gender = requests.get('http://service_2:5002/get_gender').text

    # content = {'classess': classes, 'Gender': Gender}
    # status = requests.post('http://service-4:5000/post/status', json=content).json()

    # context = db.session.query(Classes).order_by(Classes.id.desc()).first()

    # statement = f"You have generated a new class: {Classes} with the gender of {Gender} \n "
    return render_template('home.html')