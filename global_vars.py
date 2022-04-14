class Global:
    def __init__(self):
        self.SIZE = {'y':25,'x':46}
        self.SELL_PRICE = [1000, 1, 30, 50, 45, 4, 5, 12, 35]
        self.BUY_PRICE = [1000, 2, 32, 54, 48, 4, 6, 14, 37]
        self.SOIL_TYPE = ['coal-soil', 'oil-soil', 'gold-soil', 'iron-soil', 'wood-soil', 'water-soil']
        self.GOODS_NAME = ['money','gold', 'food', 'coal', 'iron', 'oil', 'stone', 'water', 'wood','electricity']
        self.date = {'day': 1, 'month': 3, 'year': 1890}
        self.capital = ['50000', '0', '0', '0', '0', '0', '0', '0', '0', '0']
        self.my_buildings = []
        self.bought_tiles = []
        self.goods_dict = {"icons":[],"amounts":[]}
        self.tiles = []
        self.picked_tiles = []
        self.buttons = []
        self.button_icons = [
        'farm', 'quarry', 'garden', 'oilproduction', 'waterpipes', 'goldmine',
        'sawmill', 'powerstation', 'mine', 'hydrostation', 'sell-goods', 'buy-goods',
        'sell-land', 'buy-land', 'destroy', 'upgrade-land', 'close-open', 'repair', 'search',
        'day', 'week', 'month']
        self.hot_keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'S', 'B', 'Q', 'E', 'D', 'G', 'P', 'R', 'F', 'N', 'W', 'M']
        self.buildings = []
  