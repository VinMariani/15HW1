from flask import Flask, jsonify, request
import json
import sqlite3

app = Flask(__name__)


@app.route("/animal/id/<int:itemid>")  # страничка вывода одного животного по ID
def animal_id_page(itemid):
    con = sqlite3.connect('animal.db')
    cur = con.cursor()
    query = f"""select * 
                from unique_animal
                left join outcomes on outcomes.animal_id=outcomes.animal_id
                where unique_animal.id = {itemid}"""
    cur.execute(query)
    animals = cur.fetchone()

    result_animals = {
        "Result": animals[0],
        #"Result 2": animals[1],
        #"Result 3": animals[2],
        #"Result 4": animals[3],
        #"Result 5": animals[4]
    }

    con.close()
    #return result_animals
    return jsonify(result_animals)


@app.route("/animal/name/<name>")  # страничка вывода одного животного по имени
def animal_name_page(name):
    con = sqlite3.connect('animal.db')
    cur = con.cursor()
    name = request.args.get("name")
    query = f"""select * 
                from unique_animal
                left join outcomes on outcomes.animal_id=outcomes.animal_id
                where unique_animal.name = '{name}'"""
    cur.execute(query)
    animals = cur.fetchall()

    result_animals = {
        "Result 1": animals[0],
        "Result 2": animals[1],
        "Result 3": animals[2],
        "Result 4": animals[3],
        "Result 5": animals[4]
    }

    con.close()
    return result_animals
    # return jsonify(result_animals)


app.run()
