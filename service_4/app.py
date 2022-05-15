from flask import Flask, request, jsonify
import random

app = Flask(__name__)

Male_Slayer = {"Blade Master","Soul Bender","Berserker","Asura","Ghostblade"}

Female_Slayer = {"Sword Master","Demon Slayer","Vagabond","Dark Templar","Spectre"}

Male_Fighter = {"Nen Emperor","Tyrant","Hades","Titan"}

Female_Fighter = {"Nen Master","Striker","Brawler","Grappler"}

Male_Mage = {"Elemental Bomber","Glacial Master","Swift Master","Blood Mage","Dimension Walker"}

Female_Mage = {"Elementalist","Summoner","Battle Mage","Witch","Enchantress"}

Birth_Place = ['Pandemonium','Empyrean','Arad','Unkown']

@app.route('/post_status', methods=['POST'])
def post_status():
    classes = request.json['classes']
    gender = request.json['gender']

    if classes == 'Slayer':
        if gender == 'Male':
            subclass = random.choice(list(Male_Slayer))
        else:
            subclass = random.choice(list(Female_Slayer))


    elif classes == 'Fighter':
        if gender == 'Male':
            subclass = random.choice(list(Male_Fighter))
        else:
            subclass = random.choice(list(Female_Slayer))

    elif classes == 'Mage':
        if gender == 'Male':
            subclass = random.choice(list(Male_Mage))
        else:
            subclass = random.choice(list(Female_Mage))
    
    birth_place = random.choice(Birth_Place)

    status = {
        "subclass" : subclass,
        "birth_place" : birth_place
    }
    return jsonify(status)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)
    


    