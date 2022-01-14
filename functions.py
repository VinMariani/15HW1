import sqlite3

con = sqlite3.connect('animal.db')
cur = con.cursor()
query = " "
cur.execute(query)
con.close()


#def one_animal(itemid):
    '''вывод одного животного по ID'''
    #con = sqlite3.connect('animal.db')
    #sqlite_query = "SELECT 'name' FROM animal "
    #cur = con.cursor()
    #cur.execute(sqlite_query)
    #animal = cur.fetchall()

    #data = {
        #"name": animal[0],
        #"breed": animal[1]
    #}

    #con.close()
    #return data

#one_animal(1)