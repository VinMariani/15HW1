import sqlite3

with sqlite3.connect('animal.db') as connection:
    cursor = connection.cursor()

    # создаем промежуточную таблицу colors
    create_colors_query = """   
        create table colors (
        id integer primary key autoincrement,
        name varchar(30)
        )
        """
    cursor.execute(create_colors_query)

    # создаем таблицу animal_colors для связки животного по цвету
    create_animal_colors_query = """
        create table animal_colors (
        animal_id integer,
        color_id  integer
        )
        """
    cursor.execute(create_animal_colors_query)

    # заполняем таблицу animal_colors значениями из столбца index таблицы animals и
    # значениями из столбца name таблицы colors
    insert_animal_colors_query = """
        insert into animal_colors 
        select animals."index", colors.name
        from animals
        join colors on rtrim(animals.color1)=rtrim(colors.name)
        """
    cursor.execute(insert_animal_colors_query)

    # заполняем таблицу animal_colors значениями из столбца index таблицы animals и
    # значениями из столбца name таблицы colors
    insert_animal_colors_query = """
        insert into animal_colors 
        select animals."index", colors.name
        from animals
        join colors on rtrim(animals.color2)=rtrim(colors.name)
        """
    cursor.execute(insert_animal_colors_query)

    # создаем таблицу outcomes
    create_outcomes_query = """
        create table outcomes(
        outcome_id   integer primary key autoincrement,
        outcome_type varchar(100),
        outcome_subtype varchar(100),
        outcome_month integer,
        outcome_year integer,
        age_upon_outcome varchar(100),
        animal_id varchar(15)
        )      
    """
    cursor.execute(create_outcomes_query)

    # заполняем таблицу outcomes
    insert_outcomes_query = """
        insert into 
        outcomes (animal_id, outcome_subtype, outcome_type, age_upon_outcome, outcome_month, outcome_year)           
        select  distinct animal_id, outcome_subtype, outcome_type, age_upon_outcome, outcome_month, outcome_year 
        from animals
    """
    cursor.execute(insert_outcomes_query)

    # создаем таблицу animal_types
    create_animal_types_query = """
        create table animal_types (
        id   integer primary key autoincrement,
        name varchar(100)
        )
    """
    cursor.execute(create_animal_types_query)

    # заполняем таблицу animal_types
    insert_animal_types_query = """
        insert into animal_types(name)              
        select distinct (animal_type)               
        from animals
        """
    cursor.execute(insert_animal_types_query)

    # создаем таблицу breeds
    create_breeds_query = """
        create table breeds (
        id   integer primary key autoincrement,
        name varchar(100)
        )
    """
    cursor.execute(create_breeds_query)

    # заполняем таблицу breeds
    insert_breeds_query = """
        insert into breeds(name)
        select distinct (breed)
        from animals
        """
    cursor.execute(insert_breeds_query)

    # создаем таблицу unique_animal
    create_unique_animal_query = """
        create table unique_animal(
        id integer primary key autoincrement,
        animal_id varchar(15),
        type_id integer,
        name varchar(100),
        date_of_birth varchar(20),
        breed_id integer
        )
    """
    cursor.execute(create_unique_animal_query)

    # заполняем таблицу
    insert_unique_animal_query = """
        insert into unique_animal(animal_id, type_id, name, date_of_birth, breed_id)
        select distinct animal_id, animal_types.id, animals.name, date_of_birth, breeds.id
        from animals
        left join animal_types on animal_type=animal_types.name
        left join breeds on animals.breed=breeds.name    
    """
    cursor.execute(insert_unique_animal_query)





# def one_animal(itemid):
# '''вывод одного животного по ID'''
# con = sqlite3.connect('animal.db')
# sqlite_query = "SELECT 'name' FROM animal "
# cur = con.cursor()
# cur.execute(sqlite_query)
# animal = cur.fetchall()

# data = {
# "name": animal[0],
# "breed": animal[1]
# }

# con.close()
# return data

# one_animal(1)
