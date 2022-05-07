from flask import Flask
import random

app = Flask(__name__)

Gender = ['Male','Female']

@app.route('/get/gender')
def get_subclasses():
    return random.choice(Gender)

if __name__ == '__main__':
    app.run(host='0.0.0.0')