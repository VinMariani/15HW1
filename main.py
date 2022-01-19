from flask import Flask, jsonify, request
import json
import sqlite3

app = Flask(__name__)


@app.route("/animal/id/<int:itemid>")  # страничка вывода одного животного по ID
def animal_id_page(itemid):
    con = sqlite3.connect('animal.db')
    cur = con.cursor()
    query = f"""select * 
                from unique_animal ua
                left join outcomes on outcomes.animal_id=ua.animal_id
                where ua.id = {itemid}"""
    cur.execute(query)
    animals = cur.fetchall()

    result_animals = {
        "Result": animals[0],
        #"Result 2": animals[1],
        #"Result 3": animals[2],
        #"Result 4": animals[3],
        #"Result 5": animals[4]
    }

    con.close()
    return jsonify(result_animals)


@app.route("/animal/name/<name>")  # страничка вывода одного животного по имени
def animal_name_page(name):
    con = sqlite3.connect('animal.db')
    cur = con.cursor()
    query = f"""select ua.animal_id, ua.name, ua.date_of_birth
                from unique_animal ua
                left join outcomes on outcomes.animal_id=ua.animal_id
                where ua.name = '{name}' limit 10"""
    cur.execute(query)
    animals = cur.fetchall()
    if len(animals)>0:
        result_animals = []
        for animal in animals:
            result_animals.append({
                'animal_id': animal[0],
                'name': name[1],
                'date_of_birth': name[2]
            })
    else:
        result_animals = {
            'result': '0'
        }
    con.close()
    return jsonify(result_animals)


app.run()
