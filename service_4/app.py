from flask import Flask, request, jsonify
import random

app = Flask(__name__)

Male_Slayer = {
    "SubClass":{
        0: "Blade Master",
        1: "Soul Bender",
        2: "Berserker",
        3: "Asura",
        4: "Ghostblade"
    }
}

Female_Slayer = {
    "SubClass":{
        0: "Sword Master",
        1: "Demon Slayer",
        2: "Vagabond",
        3: "Dark Templar",
        4: "Spectre"
    }
}
Male_Fighter = {
    "SubClass":{
        0: "Nen Emperor",
        1: "Tyrant",
        2: "Hades",
        3: "Titan"
    }
}
Female_Fighter = {
    "SubClass":{
        0: "Nen Master",
        1: "Striker",
        2: "Brawler",
        3: "Grappler"
    }
}
Male_Mage = {
    "SubClass":{
        0: "Elemental Bomber",
        1: "Glacial Master",
        2: "Swift Master",
        3: "Blood Mage",
        4: "Dimension Walker"
    }
}
Famale_Mage = {
    "SubClass":{
        0: "Elementalist",
        1: "Summoner",
        2: "Battle Mage",
        3: "Witch",
        4: "Enchantress"
    }
}
Male_Gunner = {
    "SubClass":{
        0: "Ranger",
        1: "Launcher",
        2: "Mechanic",
        3: "Spitfire",
        4: "Assault"
    }
}
Female_Gunner = {
    "SubClass":{
        0: "Bloodia",
        1: "Demolitionist",
        2: "Metalheart",
        3: "Freyja"
    }
}
Male_Priest = {
    "SubClass":{
        0: "Crusader",
        1: "Monk",
        2: "Exorcist",
        3: "Avenger"
    }
}
Female_Priest = {
    "SubClass":{
        0: "Seraph",
        1: "Inquisitor ",
        2: "Shaman",
        3: "Mistress"
    }
}
BirthPlace = {
    0: "Pandemonium",
    1: "Empyrean",
    2: "Arad",
    3: "Unkown"
}
@app.route('/post_status', methods=['POST'])
def post_status():
    Classes = request.json['Classes']
    Gender = request.json['Gender']

    if Classes == 'Slayer':
        if Gender == 'Male':
            SubClass = random.choice(list(Male_Slayer["SubClass"].values()))
        else:
            SubClass = random.choice(list(Female_Slayer["SubClass"].values()))


    elif Classes == 'Fighter':
        if Gender == 'Male':
            SubClass = random.choice(list(Male_Fighter["SubClass"].values()))
        else:
            SubClass = random.choice(list(Feale_Slayer["SubClass"].values()))

    elif Classes == 'Mage':
        if Gender == 'Male':
            SubClass = random.choice(list(Male_Mage["SubClass"].values()))
        else:
            SubClass = random.choice(list(Female_Mage["SubClass"].values()))

    elif Classes == 'Gunner':
        if Gender == 'Male':
            SubClass = random.choice(list(Male_Gunner["SubClass"].values()))
        else:
            SubClass = random.choice(list(Female_Gunner["SubClass"].values()))

    elif Classes == 'Priest':
        if Gender == 'Male':
            SubClass = random.choice(list(Male_Priest["SubClass"].values()))
        else:
            SubClass = random.choice(list(Female_Priest["SubClass"].values()))
    
    BirthPlace = random.choice(list(BirthPlace.values()))

    status = {
        "SubClass" : SubClass,
        "BirthPlace" : BirthPlace
    }
    return jsonify(status) 

if __name__ == '__main__':
    app.run(debug = True, port = 5000, host = '0.0.0.0')