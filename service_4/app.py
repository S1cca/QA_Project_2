from flask import Flask, request, jsonify
import random

app = Flask(__name__)

Male_Slayer = {
    "subclass":{
        0: "Blade Master",
        1: "Soul Bender",
        2: "Berserker",
        3: "Asura",
        4: "Ghostblade"
    }
}

Female_Slayer = {
    "subclass":{
        0: "Sword Master",
        1: "Demon Slayer",
        2: "Vagabond",
        3: "Dark Templar",
        4: "Spectre"
    }
}
Male_Fighter = {
    "subclass":{
        0: "Nen Emperor",
        1: "Tyrant",
        2: "Hades",
        3: "Titan"
    }
}
Female_Fighter = {
    "subclass":{
        0: "Nen Master",
        1: "Striker",
        2: "Brawler",
        3: "Grappler"
    }
}
Male_Mage = {
    "subclass":{
        0: "Elemental Bomber",
        1: "Glacial Master",
        2: "Swift Master",
        3: "Blood Mage",
        4: "Dimension Walker"
    }
}
Female_Mage = {
    "subclass":{
        0: "Elementalist",
        1: "Summoner",
        2: "Battle Mage",
        3: "Witch",
        4: "Enchantress"
    }
}
Male_Gunner = {
    "subclass":{
        0: "Ranger",
        1: "Launcher",
        2: "Mechanic",
        3: "Spitfire",
        4: "Assault"
    }
}
Female_Gunner = {
    "subclass":{
        0: "Bloodia",
        1: "Demolitionist",
        2: "Metalheart",
        3: "Freyja"
    }
}
Male_Priest = {
    "subclass":{
        0: "Crusader",
        1: "Monk",
        2: "Exorcist",
        3: "Avenger"
    }
}
Female_Priest = {
    "subclass":{
        0: "Seraph",
        1: "Inquisitor ",
        2: "Shaman",
        3: "Mistress"
    }
}

@app.route('/post_status', methods=['POST'])
def post_status():
    classes = request.json['classes']
    gender = request.json['gender']

    if classes == 'Slayer':
        if gender == 'Male':
            subclass = random.choice(list(Male_Slayer["subclass"].values()))
        else:
            subclass = random.choice(list(Female_Slayer["subclass"].values()))


    elif classes == 'Fighter':
        if gender == 'Male':
            subclass = random.choice(list(Male_Fighter["subclass"].values()))
        else:
            subclass = random.choice(list(Female_Slayer["subclass"].values()))

    elif classes == 'Mage':
        if gender == 'Male':
            subclass = random.choice(list(Male_Mage["subclass"].values()))
        else:
            subclass = random.choice(list(Female_Mage["subclass"].values()))

    elif classes == 'Gunner':
        if gender == 'Male':
            subclass = random.choice(list(Male_Gunner["subclass"].values()))
        else:
            subclass = random.choice(list(Female_Gunner["subclass"].values()))

    elif classes == 'Priest':
        if gender == 'Male':
            subclass = random.choice(list(Male_Priest["subclass"].values()))
        else:
            subclass = random.choice(list(Female_Priest["subclass"].values()))
    
    birth_place = random.choice(['Pandemonium','Empyrean','Arad','Unkown'])

    status = {
        "subclass" : subclass,
        "birth_place" : birth_place
    }
    return status

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)