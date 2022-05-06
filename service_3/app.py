from flask import Flask
import random

app = Flask(__name__)

gender = ['male','female']

@app.route('/get/gender')
def get_subclasses():
    return random.choice(gender)

if __name__ == '__main__':
    app.run(host='0.0.0.0')