from flask import Flask
import random

app = Flask(__name__)

Classess = ['Slayer','Fighter','Mage','Gunner','Priest']

@app.route('/get_classes')
def get_classes():
    return random.choice(Classess)

if __name__ == '__main__':
    app.run(debug = True, port = 5000, host = '0.0.0.0')