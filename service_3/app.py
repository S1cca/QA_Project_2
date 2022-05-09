from flask import Flask
import random

app = Flask(__name__)

Gender = ['Male','Female']

@app.route('/get_gender')
def get_gender():
    return random.choice(Gender)

if __name__ == '__main__':
    app.run(debug = True, port = 5000, host = '0.0.0.0')