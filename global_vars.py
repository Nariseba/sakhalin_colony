from PyQt5.QtGui import QColor
import sqlite3
class Global:
    MW = None # link for the MainWindow
    volume = 100
    SIZE = {'y':150,'x':200} # size of the map : 200*150 tiles
    SIZE_OF_MAP = {'Tiny':      (50,100),
                   'Small':     (75,125),
                   'Normal':    (100,150),
                   'Big':       (150,200),
                   'Huge':      (250,300)}
    SEVERITY = str()
    MAP_TYPE = ('Islands', 'Lakes', 'Big island', 'Archipelagos', 'NO sea')
    RES_DICT = {'Poorest':  0.5, 'Poor': 1, 'Normal': 2, 'Rich': 3, 'Richest': 4} 
    RESOURCES = float()
    WETNESS = int()
    SOIL_TYPE = ('sea', 'none', 'sea-coastal')
    HOT_KEYS = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Q+1', 'Q+2', 'Q+3', 'Q+4', 'Q+5', 'Q+6', 'Q+7', 'Q+8', 'Q+9', 'Q+0',
    'W+1', 'W+2', 'W+3', 'W+4', 'W+5','S', 'B', 'Q', 'E', 'D', 'G', 'P', 'R', 'F', 'N', 'W', 'M',)
    BUTTON_ICONS = (
    'farm', 'quarry', 'garden', 'oilproduction', 'waterpipes', 'goldmine','sawmill', 'powerstation', 'mine', 'hydrostation',
    'apiary', 'greenhouse', 'windpowerplant', 'smallnpp', 'npp', 'oiltorch', 'bigfarm', 'metallurgy', 'oilpump', 'bigsawmill', 
    'coalpit', 'huntingGrounds', 'fishery', 'cattlebreeding', 'watertower', 'sell-goods', 'buy-goods', 'sell-land', 'buy-land',
    'destroy', 'upgrade-land', 'close-open', 'repair', 'search', 'day', 'week', 'month')
    capital = [     50000,  0,    0,     0,     0,   0,    0,    0,    0,      0]
    #when start :   money, food, wood, stone, water coal, iron, oil, gold, electricity
    bought_tiles = []
    buildings = []
    picked_tiles = []
    my_buildings = []
    tiles = []
    TS = 25 #tile size
    landshaft = False
    SPEED = {'Quick':0.5, 'Standart':1.0, 'Long':2, 'Epic':4, 'Marafone':6}
    GAME_SPEED = None
    BUY_PRICE =                     (1,     14,      4,       6,      32,     54,     48,   1000,      37)
    SELL_PRICE =                    (1,     12,      4,       5,      30,     50,     45,   1000,      35)
    GOODS_NAME =        ('money', 'food', 'wood', 'stone', 'water', 'coal', 'iron', 'oil', 'gold', 'electricity')
    
    resource_amount =             (10800,  8250,   6750,   6600,    3000,    1800,    900,   750) # Total: 38 850 for 30000 tiles (islands)
    #           %  =                28       21      17     17        8       5        2      2
    resource_color = (
    QColor(255,255,255,90),  # food
    QColor(80,35,10,90),    # wood
    QColor(170,170,170,130),  # stone
    QColor(84,180,250,90),    # water
    QColor(0,0,0,90),        # coal
    QColor(240,70,20,90),    # iron
    QColor(140,10,120,90),     # oil
    QColor(255,255,0,90),)    # gold
    
    
    
    
    def data_base_output():
        connection = sqlite3.connect("sakh_db.sqlite")
        cursor = connection.cursor()
    
        cursor.execute('SELECT * FROM buildings;')
        for el in range(26):
            Global.buildings.append(list(cursor.fetchone()))
            Global.buildings[el][4] = {}
            connection.commit()
        
        cursor.execute('SELECT * FROM production;')
        for el in range(26):
            prod = list(cursor.fetchone())
            Global.buildings[el][4] = prod[2::]  
            B = Global.buildings[el]
            prod, cons = {},{}
            for goods in range(10):
                if B[4][goods] > 0:
                    prod.update({Global.GOODS_NAME[goods]:B[4][goods]})
                elif B[4][goods] < 0:
                    cons.update({Global.GOODS_NAME[goods]:B[4][goods]})
            prod, cons = map(lambda list_: str.replace(list_, '\'', ''),[str(prod)[1:-1], str(cons)[1:-1]])
            Global.buildings[el].append(f'{B[1]} ({Global.HOT_KEYS[el]}) - {B[2]} <Br> Takes {B[9]} days to build. Will work about {int(B[8]/360)} years ({B[7]} seasons). <Br> Needs {B[11]} workers. <Br> Production: {prod} <Br> Consumption: {cons}')
