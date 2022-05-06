from . import app, db
from .models import Classes
from flask import render_template, request, redirect, url_for, flash
import requests, json


@app.route('/', methods=['GET', 'POST'])
def index():
    classess = requests.get('http://service_2:5002/get/classes').text

    content = {'classess': classes, 'gender': gender}






    return render_template('index.html')