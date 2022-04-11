import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection("C:\Games\Sakhalin\draft\sakh_db.sqlite")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
        
create_tiles_table = """
 CREATE TABLE IF NOT EXISTS tiles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  x INTEGER,
  y INTEGER
  soil_type TEXT,
  isBought BOOLEAN,
  itsBuilding BOOLEAN
);
"""     
execute_query(connection, create_tiles_table)

#create_goods_table = """
# CREATE TABLE IF NOT EXISTS goods (
#  id INTEGER PRIMARY KEY AUTOINCREMENT,
#  money INTEGER,
#  gold INTEGER
#  food INTEGER,
#  coal INTEGER,
#  iron INTEGER,
#  oil INTEGER,
#  stone INTEGER,
#  water INTEGER,
#  wood INTEGER,
#  electricity INTEGER
#);
#"""    
#execute_query(connection, create_goods_table)

create_production_table = """
CREATE TABLE IF NOT EXISTS production (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  building_type TEXT,
  money INTEGER,
  gold INTEGER
  food INTEGER,
  coal INTEGER,
  iron INTEGER,
  oil INTEGER,
  stone INTEGER,
  water INTEGER,
  wood INTEGER,
  electricity INTEGER
  );
  """
execute_query(connection, create_production_table)  

create_buildings_table = """
 CREATE TABLE IF NOT EXISTS buildings (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  description TEXT NOT NULL
  max_lifetime INTEGER,
  lifetime INTEGER,
  price INTEGER,
  repair_cost INTEGER,
  production_id INTEGER,
  soil TEXT,
  seasons INTEGER,
  daysToBuild INTEGER,
  isFinished BOOLEAN,
  tile_id INTEGER,
  FOREIGN KEY (tile_id) REFERENCES tiles (id),
  FOREIGN KEY (production_id) REFERENCES production (id)
);
"""
execute_query(connection, create_buildings_table)

add_building_types_production = """
INSERT INTO
  production (building_type, money, gold, food, coal, iron, oil, stone, water, wood, electricity)
VALUES
  ('Storehose', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
  ('Farm', 0, 0, 38, 0, 0, 0, 0, -2, 0, 0),
  ('Quarry', 0, 0, 0, 0, 8, -8, 30, 0, 0, 0),
  ('Garden', 0, 0, 20, 0, 0, 0, 0, -1, 0, 0),
  ('Oil-production',  0, 0, 0, 0, 0, 8, 0, 0, 0, 0);
  ('Waterpipes', 0, 0, 0, 0, 0, 0, 0, 4, 0, 0),  
  ('Goldmine', 0, 2, 0, 0, 0, 0, 100, -200, 0, 0),
  ('Sawmill', 0, 0, 0, 0, -1, -2, 0, 0, 18, 0),
  ('Powerstation', 0, 0, 0, 0, 0, -1, 0, 0, 0, 2),
  ('Mine', 0, 0, 0, 4, 0, 0, 0, 20, -2, -2),
  ('Hydrostation', 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
"""
execute_query(connection, add_building_types_production)





"""
Farm (1) - 15500
Can be built everywhere for 38 days. 1200 days to live. Works during: spring; summer; autumm.
Consumption: water - 2
Production: food - 38

Quarry (2) - 20200
Can be built on iron soil for 36 days. 1200 days to live. Works during: summer.
Consumption: oil - 8
Production: iron - 8, stone - 30

Garden (3) - 18000
Can be built everywhere for 20 days. 3800 days to live. Works during: summer; autumm.
Consumption: water - 2
Production: food - 38

Oil-production (4) - 57500
Can be built oil soil for 46 days. 900 days to live. Works during: summer.
Consumption: none
Production: oil - 8

Waterpipes (5) - 8100
Can be built on water for 38 days. 900 days to live. Works during: spring; summer; autumm.
Consumption: none
Production: water - 4

Goldmine (6) - 132000
Can be built on golden soil for 20 days. 900 days to live. Works during: summer.
Consumption: water - 200
Production: gold - 2, stone - 100

Sawmill (7) - 35500
Can be built wood-soil for 10 days. 1200 days to live. Works during: winter; spring; summer; autumm.
Consumption: iron - 1, oil - 2
Production: wood - 18

Powerstation (8) - 23000
Can be built everywhere for 65 days. 1600 days to live. Works during: winter; spring; summer; autumm.
Consumption: oil - 1
Production: electricity - 2

Mine (9) - 63000
Can be built on coal soil for 68 days. 1200 days to live. Works during: winter; spring; summer; autumm.
Consumption: wood - 2, electricity - 2
Production: coal - 4, stone - 20

Hydrostation (0) - 71500
Can be built on water for 100 days. 3200 days to live. Works during: winter; spring; summer; autumm.
Consumption: none
Production: electricity - 1
"""
