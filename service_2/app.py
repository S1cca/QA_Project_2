from flask import Flask
import random

app = Flask(__name__)

classes = ['Slayer','Fighter','Mage']

@app.route('/get_classes')
def get_classes():
    return random.choice(classes)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)




    