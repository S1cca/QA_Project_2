from . import app, db
from .models import Classes, Gender, SubClass, BirthPlace
from flask import render_template, request, redirect, url_for, flash
import requests, json


@app.route('/', methods=['GET', 'POST'])
def index():
    Classess = requests.get('http://service_2:5002/get/classes').text
    Gender = requests.get('http://service_2:5002/get/gender').json()

    content = {'classess': classes, 'Gender': Gender}
    status = requests.post('http://service-4:5000/post/status', json=content).json()

    context = db.session.query(Classes).order_by(Classes.id.desc()).first()

    statement = f"You have generated a new class: {Classes} with the gender of {Gender} \n "

    return render_template('index.html')