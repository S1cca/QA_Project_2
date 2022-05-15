from flask import Flask
import random

app = Flask(__name__)

gender = ['Male','Female']

@app.route('/get_gender')
def get_gender():
    return random.choice(gender)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)




    