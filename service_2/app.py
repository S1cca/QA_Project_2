from flask import Flask
import random

app = Flask(__name__)

classess = ['Slayer','Fighter','Mage','Gunner','Priest']

@app.route('/get/classes')
def get_classes():
    return random.choice(classess)

if __name__ == '__main__':
    app.run(host='0.0.0.0')