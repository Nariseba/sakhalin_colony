#import signal 
class Global:
    def __init__(self):
        self.date = {'day': 1, 'month': 3, 'year': 1890}
        self.capital = ['50000', '0', '0', '0', '0', '0', '0', '0', '0', '0']
        self.GOODS_NAME = ['money','gold', 'food', 'coal', 'iron', 'oil', 'stone', 'water', 'wood','electricity']
        self.BUILDING = ['storehouse', 'farm', 'quarry', 'garden', 'oilproduction', 'waterpipes', 'goldmine','sawmill', 'powerstation', 'mine', 'hydrostation']
        self.my_buildings = []
        self.goods_dict = {"icons":[],"amounts":[]}
        self.tiles = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[]}
        self.SOIL_TYPE = ['coal-soil', 'oil-soil', 'gold-soil', 'iron-soil', 'wood-soil', 'water-soil']
        self.BUY_PRICE = [1000, 2, 32, 54, 48, 4, 6, 14, 37]
        self.SELL_PRICE = [1000, 1, 30, 50, 45, 4, 5, 12, 35]
        self.picked_tiles = []
        self.buttons = []
        self.button_icons = [
        'farm', 'quarry', 'garden', 'oilproduction', 'waterpipes', 'goldmine',
        'sawmill', 'powerstation', 'mine', 'hydrostation', 'sell-goods', 'buy-goods',
        'sell-land', 'buy-land', 'destroy', 'upgrade-land', 'close-open', 'repair', 'search',
        'day', 'week', 'month']
        self.hot_keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'S', 'B', 'Q', 'E', 'D', 'G', 'P', 'R', 'F', 'N', 'W', 'M']
        self.season = ['spring', 'summer', 'autumm', 'winter']
        #self.max_lifetime =[4000, 1200, 1200, 3800, 900, 900, 900, 900, 1600, 1200, 3200]
