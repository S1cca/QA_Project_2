from . import app, db
from .models import none
from flask import render_template, request, redirect, url_for, flash
import requests, json


@app.route('/', methods=['GET', 'POST'])
def index():
    pass
    return render_template('index.html')