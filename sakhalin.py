# Form implementation generated from reading ui file 'sakhalin.ui'
#
# Created by: PyQt6 UI code generator 6.2.3

from PyQt6 import QtCore, QtGui, QtWidgets
import random, pickle, sqlite3
from game_widgets import Ui_Exit_Widget, Ui_Sale_Widget
from global_vars import *


G = Global()

def DB_output():
    connection = sqlite3.connect("C:\Games\Sakhalin\draft\sakh_db.sqlite")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM buildings;')
    for el in range(11):
        G.buildings.append(list(cursor.fetchone()))
        G.buildings[el][4] = {}
        connection.commit()
    
    cursor.execute('SELECT * FROM production;')
    for el in range(11):
        prod = list(cursor.fetchone())
        G.buildings[el][4] = prod[2::]
DB_output()        

  
class Tile(QtWidgets.QToolButton):
    def __init__(self, y, x):
        super(QtWidgets.QToolButton, self).__init__()
        self.isBought = False
        self.itsBuilding = False
        self.soil_type = 'none'
        self.x = x
        self.y = y
        self.setIconSize(QtCore.QSize(45, 45))
        self.setStyleSheet(" border: 0px;")  
    
    def setSoil_type(self):
        rnd = random.random()
        if (rnd <= 20/216):
            self.soil_type = G.SOIL_TYPE[0]
            self.setStyleSheet("background-color: #bbbbbb ; background-image : url(objs/"+G.SOIL_TYPE[0]+".bmp); border: 0px;")
        elif (20/216 < rnd <= 26/216): 
            self.soil_type = G.SOIL_TYPE[1]
            self.setStyleSheet("background-image : url(objs/"+G.SOIL_TYPE[1]+".bmp); border: 0px;")
        elif (26/216 < rnd <= 31/216): 
            self.soil_type = G.SOIL_TYPE[2]
            self.setStyleSheet("background-image : url(objs/"+G.SOIL_TYPE[2]+".bmp); border: 0px;")
        elif (31/216 < rnd <= 44/216): 
            self.soil_type = G.SOIL_TYPE[3]
            self.setStyleSheet("background-image : url(objs/"+G.SOIL_TYPE[3]+".bmp); border: 0px;")
        elif (44/216 < rnd <= 99/216): 
            self.soil_type = G.SOIL_TYPE[4]
            self.setStyleSheet("background-image : url(objs/"+G.SOIL_TYPE[4]+".bmp); border: 0px;")  
        elif (99/216 < rnd <= 143/216):
            self.soil_type = G.SOIL_TYPE[5]
            self.setStyleSheet("background-image : url(objs/"+G.SOIL_TYPE[5]+".bmp); border: 0px;")

    def unpicking(self):
        G.picked_tiles.remove(self)
        self.setStyleSheet("background-image : url(objs/"+self.soil_type+".bmp); border: 0px;")
        if self.isBought:
            self.setStyleSheet("background-image : url(objs/"+self.soil_type+".bmp); border: 1px solid #00ff00;")
        if self.itsBuilding:
            self.setStyleSheet("background-image : url(objs/"+self.itsBuilding.icon+".bmp); border: 1px solid #00ff00;")
    
    def picking(self):
        G.picked_tiles.append(self)
        self.setStyleSheet("background-image : url(objs/"+self.soil_type+".bmp); border: 1px outset blue;")
        if self.isBought:
            self.setStyleSheet("background-image : url(objs/"+self.soil_type+".bmp); border: 1px outset rgb(250,250,0);")
        if self.itsBuilding:
            self.setStyleSheet("background-image : url(objs/"+self.itsBuilding.icon+".bmp); border: 1px outset  rgb(250,250,0);")

    def picking_on_click(self):
        if G.picked_tiles:
            for el in G.picked_tiles:
                el.unpicking()
        self.picking()

print(dir(Tile))

class Building():
    def __init__(self, id,  icon, price, repair_cost, production_consumption, lifetime, soil, seasons, max_lifetime, days_to_build, discription, isFinished, y, x):
        self.id = id
        self.icon = icon
        self.price = price
        self.repair_cost = repair_cost
        self.production_consumption = production_consumption
        self.lifetime = lifetime
        self.soil = soil
        self.seasons = seasons
        self.max_lifetime = max_lifetime
        self.days_to_build = days_to_build
        self.discription = discription
        self.isFinished = False
        self.y, self.x = y, x

    def __str__(self):
        return self.icon

    def isWork_time(self):
        if self.seasons == 4:
            return True
        elif self.seasons == 3:
            if G.date['month'] > 2 and G.date['month'] < 12:
                return True
            else:
                return False
        elif self.seasons == 2:
            if G.date['month'] > 5 and G.date['month'] < 12:
                return True
            else:
                return False
        elif self.seasons == 1:
            if G.date['month'] > 5 and G.date['month'] < 9:
                return True
            else:
                return False


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630+(G.SIZE['x'] - 18)*26, 440+(G.SIZE['y'] - 12)*25)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(630+(G.SIZE['x'] - 18)*26, 440+(G.SIZE['y'] - 12)*25))
        MainWindow.setMaximumSize(QtCore.QSize(630+(G.SIZE['x'] - 18)*26, 440+(G.SIZE['y'] - 12)*25))
        if(G.SIZE['x'] >=45 and G.SIZE['y'] >=24):
            MainWindow.showFullScreen()
            MainWindow.setStyleSheet('background-color: black;color: #bbbbbb;')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("objs/icon.bmp"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 640+(G.SIZE['x'] - 18)*26, 401+(G.SIZE['y'] - 12)*25))
        self.frame.setStyleSheet("background-color: black;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 84, 145, 315+(G.SIZE['y'] - 12)*25))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayoutWidget.setStyleSheet("border: 1px solid #bbbbbb;")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setStyleSheet("background-color:#252525; color: #bbbbbb; border: 1px solid #e3e3e3;")
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage('Welcome!')
        MainWindow.setStatusBar(self.statusbar)

        def statusbar_message():
            if(len(G.picked_tiles) < 1):
                self.statusbar.showMessage(str(G.date['day']) + ' . ' + str(G.date['month']) + ' . ' + str(G.date['year']))
            elif(len(G.picked_tiles) > 1):
                self.statusbar.showMessage(str(len(G.picked_tiles))+' tiles')
            else:
                if G.picked_tiles[0].itsBuilding:
                    if G.picked_tiles[0].itsBuilding.isFinished:
                        self.statusbar.showMessage(G.picked_tiles[0].itsBuilding.icon + ', ' + str(G.picked_tiles[0].itsBuilding.lifetime) + ' days left to live')
                    else:
                        self.statusbar.showMessage(G.picked_tiles[0].itsBuilding.icon + ', ' + str(G.picked_tiles[0].itsBuilding.days_to_build) + ' days left to build')
                else:
                    self.statusbar.showMessage(G.picked_tiles[0].soil_type)

        self.seasonLabel = QtWidgets.QLabel(self.frame)
        self.seasonLabel.setGeometry(QtCore.QRect(-1, -1, 146, 87))
        self.seasonLabel.setStyleSheet("border: 1px solid #bbbbbb; color: rgb(255,244,244)")
        self.seasonLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.seasonLabel.setPixmap(QtGui.QPixmap("objs/spring.bmp"))
        self.seasonLabel.setToolTip('<div style="background-color:black; color: #bbbbbb; font: 10px;" >Spring</div>')
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(540, 10, 83, 24))
        self.textBrowser.setStyleSheet("color: #bbbbbb; border: 0px")
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName("textBrowser")

        def left_tab_init():
            # for el in range(10):
            #     if len(G.goods_dict["icons"]):
            #        G.goods_dict["icons"][el].close()
            #        G.goods_dict["amounts"][el].close()
            # G.goods_dict["icons"].clear()
            # G.goods_dict["amounts"].clear()
            for el in range(10):
                G.goods_dict["icons"].append(QtWidgets.QLabel(self.formLayoutWidget))
                G.goods_dict["icons"][el].setPixmap(QtGui.QPixmap("objs/"+G.GOODS_NAME[el]+".bmp"))
                G.goods_dict["icons"][el].setStyleSheet("border: 0px; color: #bbbbbb;")
                G.goods_dict["icons"][el].setToolTip('<div>'+G.GOODS_NAME[el]+'</div>')
                self.formLayout.setWidget(el, QtWidgets.QFormLayout.ItemRole.LabelRole, G.goods_dict["icons"][el])

                G.goods_dict["amounts"].append(QtWidgets.QLineEdit(self.formLayoutWidget))
                G.goods_dict["amounts"][el].setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
                G.goods_dict["amounts"][el].setAutoFillBackground(False)
                G.goods_dict["amounts"][el].setStyleSheet("color: #bbbbbb;\n border: 0px;")
                G.goods_dict["amounts"][el].setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
                G.goods_dict["amounts"][el].setReadOnly(True)
                G.goods_dict["amounts"][el].setText(G.capital[el])
                G.goods_dict["amounts"][el].setToolTip(G.GOODS_NAME[el])

                self.formLayout.setWidget(el, QtWidgets.QFormLayout.ItemRole.FieldRole, G.goods_dict["amounts"][el])
            print(len(G.goods_dict["amounts"]))
        left_tab_init()


        self.Tiles_area = QtWidgets.QWidget(self.frame)
        self.Tiles_area.setGeometry(QtCore.QRect(140, 80, 480+(G.SIZE['x'] - 18)*26, 324+(G.SIZE['y'] - 12)*25))
        self.Tiles_area.setObjectName("Tiles_area")
        self.Tiles_area.setStyleSheet("background-color: rgb(54,160,84); margin: 5px; border: 1px solid #bbbbbb ")
        self.gridLayout = QtWidgets.QGridLayout(self.Tiles_area)
        self.gridLayout.setObjectName("gridLayout")
        self.mass_picking = QtGui.QAction(MainWindow)
        self.mass_picking.setShortcut("Ctrl+A")
        self.Tiles_area.addAction(self.mass_picking)
        self.mass_picking.setCheckable(True)
        
        # CREATING THE MAP 
        
        def tiles_area_init():
            for y in range(G.SIZE['y']):
                G.tiles.append([])
                for x in range(G.SIZE['x']):            
                    G.tiles[y].append(Tile(y,x)) 
                    G.tiles[y][x].setParent(self.Tiles_area)
                    G.tiles[y][x].show()
                    G.tiles[y][x].setGeometry(QtCore.QRect(x*26, y*25+2, 35, 35))
                    G.tiles[y][x].clicked.connect( G.tiles[y][x].picking_on_click)
                    #G.tiles[y][x].mouseMoveEvent.connect(lambda : G.tiles[y][x].setStyleSheet('border:1px solid black;'))
                    G.tiles[y][x].clicked.connect(statusbar_message)
                    G.tiles[y][x].setSoil_type()
        tiles_area_init()

        def storehouse_allocation():
            y = random.randint(0, G.SIZE['y'] - 1)
            x = random.randint(0, G.SIZE['x'] - 1)
            G.bought_tiles.append(G.tiles[y][x])
            G.tiles[y][x].isBought = True
            my_building = Building(*G.buildings[0], y, x)
            G.my_buildings.append(my_building)
            G.tiles[y][x].itsBuilding = G.my_buildings[0]
            G.tiles[y][x].itsBuilding.isFinished = True
            G.tiles[y][x].setStyleSheet("background-image : url(objs/"+G.tiles[y][x].itsBuilding.icon+".bmp); border: 1px solid rgb(0,255,0);")
            return G.tiles[y][x]

        storehouse_tile = []
        storehouse_tile.append(storehouse_allocation())

        # END OF CREATING THE MAP

        #BUTTONS

        for el in range(19):
            G.buttons.append(QtWidgets.QPushButton(self.frame))
            G.buttons[el].setGeometry(QtCore.QRect(160+(((el)//2)*30)+((el)//10)*20,(30*(el%2))+10, 25, 25))
            G.buttons[el].setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            G.buttons[el].setStyleSheet("background-image : url(objs/"+G.button_icons[el]+".bmp); border: 0px;")
            G.buttons[el].setShortcut(G.hot_keys[el])
            G.buttons[el].setToolTip('<div style="background-color:black; color: #bbbbbb ; border: 5px ;font: 10px;;">'+G.button_icons[el]+'</div>')
            
        for el in range(10):
            G.buttons[el].setToolTip('<div style="background-color:black; color: #bbbbbb ; border: 5px ; font: 10px;">'+G.buildings[el+1][-2]+'</div>')

        for el in range(3):
            G.buttons.append(QtWidgets.QPushButton(self.frame))
            G.buttons[el+19].setGeometry(QtCore.QRect(520+el*30, 40, 25, 25))
            G.buttons[el+19].setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            G.buttons[el+19].setStyleSheet("background-image : url(objs/"+G.button_icons[el+19]+".bmp); border: 0px;")
            G.buttons[el+19].setShortcut(G.hot_keys[el+19])
            

        # DATE PART

        self.date_label = QtWidgets.QLabel(self.frame)
        self.date_label.setGeometry(QtCore.QRect(525, 15, 80, 15))
        self.date_label.setStyleSheet("color: #bbbbbb")
        self.date_label.setText(str(G.date['day']) + ' . ' + str(G.date['month']) + ' . ' + str(G.date['year']))

        def  production():
            for building in G.my_buildings:
                if building.isFinished: 
                    if building.isWork_time():
                        permission = True
                        for el in range(10):
                            if (int(G.capital[el]) + building.production_consumption[el]) < 0:
                                permission = False
                        if permission:
                            for el in range(10):
                                G.capital[el] = str(int(G.capital[el]) + building.production_consumption[el])
                    building.lifetime -= 1
                    if building.lifetime <= 0:
                        G.tiles[building.y][building.x].setStyleSheet("background-image : url(objs/"+G.tiles[building.y][building.x].soil_type+".bmp); border: 1px solid rgb(0,255,0);")
                        G.tiles[building.y][building.x].itsBuilding = False
                        if G.picked_tiles.count(G.tiles[building.y][building.x]):
                            G.picked_tiles.remove(G.tiles[building.y][building.x])
                        G.my_buildings.remove(building)
                else:
                    building.days_to_build = building.days_to_build - 1
                    if building.days_to_build == 0:
                        building.isFinished = True

        def gameover():
            if not storehouse_tile[-1].itsBuilding:
                game_over.show()
                return True
 
        def change_season_icon():
            if G.date['month'] == 3:
                self.seasonLabel.setPixmap(QtGui.QPixmap("objs/spring.bmp"))
                self.seasonLabel.setToolTip('<div style="color: #bbbbbb; font: 10px;" >Spring</div>')
            elif G.date['month'] == 6:
                self.seasonLabel.setPixmap(QtGui.QPixmap("objs/summer.bmp"))
                self.seasonLabel.setToolTip('<div style="color: #bbbbbb; font: 10px;" >Summer</div>')
            elif G.date['month'] == 9:
                self.seasonLabel.setPixmap(QtGui.QPixmap("objs/autumm.bmp"))
                self.seasonLabel.setToolTip('<div style="color: #bbbbbb; font: 10px;" >Autumm</div>')
            elif G.date['month'] == 12:
                self.seasonLabel.setPixmap(QtGui.QPixmap("objs/winter.bmp"))
                self.seasonLabel.setToolTip('<div style="color: #bbbbbb; font: 10px;" >Winter</div>')

        def next_day():
            if not gameover():
                production()
                if G.date['day'] == 30:
                    G.date['day'] = 1
                    if G.date['month'] == 12:
                        G.date['month'] = 1
                        G.date['year'] += 1
                    else:
                        G.date['month'] += 1
                        change_season_icon()
                else:
                    G.date['day'] += 1
                self.date_label.setText(str(G.date['day']) + ' . ' + str(G.date['month']) + ' . ' + str(G.date['year']))
                left_tab_init()
                statusbar_message()

        def next_week():
            for i in range(7):
                next_day()

        def next_month():
            for i in range(30):
                next_day()

        # END OF DATE PART
            
        def upgrade_soil():
            pass
            
        def locker():
            pass

        def tile_purchase():
            for tile in G.picked_tiles:
                if not tile.isBought and int(G.capital[0]) >= 9000:
                    def neighbour():
                        for el in G.bought_tiles:
                            if (el.y - tile.y)**2 == 0 and (el.x - tile.x)**2 == 1: return True
                            if (el.y - tile.y)**2 == 1 and (el.x - tile.x)**2 == 0: return True
                        return False
                    if neighbour():
                        tile.isBought = True
                        tile.setStyleSheet("background-image : url(objs/"+tile.soil_type+".bmp); border: 1px solid rgb(255,255,0);")
                        G.capital[0] = str(int(G.capital[0]) - 9000)
                        G.bought_tiles.append(tile)
                    else:
                        self.statusbar.showMessage('You can only buy neighbouring G.tiles')
            left_tab_init()

        def tile_sale():
            for tile in G.picked_tiles:
                if tile.isBought and not tile.itsBuilding:
                    tile.isBought = False
                    tile.setStyleSheet("background-image : url(objs/"+tile.soil_type+".bmp); border: 1px solid rgb(0,255,0)")
                    G.bought_tiles.remove(tile)
                    G.capital[0] = str(int(G.capital[0]) + 8000)
            left_tab_init()
            statusbar_message()

        def destroy():
            for tile in G.picked_tiles:
                if tile.itsBuilding:
                    tile.itsBuilding = False
                    tile.setStyleSheet("background-image : url(objs/"+tile.soil_type+".bmp); border: 1px solid rgb(255,255,0);")
                    for building in G.my_buildings:
                        if building.y == tile.y and building.x == tile.x:
                            G.my_buildings.remove(building)
            statusbar_message()                          

        def repair():
            for tile in G.picked_tiles:

                def remont():
                    while (tile.itsBuilding.max_lifetime != tile.itsBuilding.lifetime):
                        if (int(G.capital[0]) - tile.itsBuilding.repair_cost) >= 0:
                            G.capital[0] = str(int(G.capital[0]) - tile.itsBuilding.repair_cost)
                            tile.itsBuilding.lifetime += 1
                        else: break

                if tile.itsBuilding:
                    remont()
                    statusbar_message()
                else:
                    self.statusbar.showMessage('There is nothng to repair')
            left_tab_init()

        def search():
            if not len(G.picked_tiles):
                weakest = False
                x = 4000
                for el in G.my_buildings:
                    if el.max_lifetime != el.lifetime and el.lifetime < x:
                        x = el.lifetime
                        weakest = el
                if not weakest:
                    pass
                else:
                    G.tiles[weakest.y][weakest.x].setStyleSheet("background-image : url(objs/"+weakest.icon+".bmp); border: 1px outset  rgb(255,255,0);")
                    G.picked_tiles.append(G.tiles[weakest.y][weakest.x])
                statusbar_message()

        def sale():
            sale_widget = QtWidgets.QDialog(MainWindow)
            ui_sale = Ui_Sale_Widget()
            ui_sale.setupUi(sale_widget, G.SELL_PRICE, "Sell", G)
            sale_widget.show()
            sale_widget.finished.connect(left_tab_init)

        def buy():
            buy_widget = QtWidgets.QDialog(MainWindow)
            ui_buy = Ui_Sale_Widget()
            ui_buy.setupUi(buy_widget, G.BUY_PRICE, "Buy", G)
            buy_widget.show()
            buy_widget.finished.connect(left_tab_init)

        def buy_object(*argv):
            for tile in G.picked_tiles:
                my_building = Building(*argv, tile.y, tile.x)
                if tile.isBought and not tile.itsBuilding and (my_building.soil == tile.soil_type or my_building.soil == 'none') and int(G.capital[0]) >= my_building.price:
                    G.capital[0] = str(int(G.capital[0]) - my_building.price)
                    G.my_buildings.append(my_building)
                    tile.itsBuilding = my_building
                    tile.setStyleSheet("background-image : url(objs/"+my_building.icon+".bmp); border: 1px solid #ffff00;")
            left_tab_init() 
            statusbar_message()

        btn_functions = [lambda: buy_object(*G.buildings[1]),lambda: buy_object(*G.buildings[2]),lambda: buy_object(*G.buildings[3])
        ,lambda: buy_object(*G.buildings[4]),lambda: buy_object(*G.buildings[5]),lambda: buy_object(*G.buildings[6]),
        lambda: buy_object(*G.buildings[7]), lambda: buy_object(*G.buildings[8]),lambda: buy_object(*G.buildings[9]),
        lambda: buy_object(*G.buildings[10]), sale, buy, tile_sale, tile_purchase, destroy, upgrade_soil,
        locker, repair, search, next_day, next_week, next_month]
        
        for btn in range(22):
            G.buttons[btn].clicked.connect(btn_functions[btn])

        # END OF BUTTONS

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 21))
        self.menubar.setStyleSheet('border: 1px solid #bbbbbb')
        self.menubar.setObjectName("menubar")
        self.menuGame = QtWidgets.QMenu(self.menubar)
        self.menuGame.setObjectName("menuGame")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        
        def finish_game():
            G.picked_tiles.clear()
            G.bought_tiles.clear()
            G.my_buildings.clear()
            for y in range(G.SIZE['y']):
                for x in range(G.SIZE['x']):
                    G.tiles[y][x].close()
                G.tiles[y].clear()
            storehouse_tile.clear()

        def new_game():
            finish_game()
            tiles_area_init()
            storehouse_tile.append(storehouse_allocation())
            G.capital = ['50000', '0', '0', '0', '0', '0', '0', '0', '0', '0']
            G.date = {'day': 1, 'month': 3, 'year': 1890}
            change_season_icon()
            left_tab_init()
            self.date_label.setText(str(G.date['day']) + ' . ' + str(G.date['month']) + ' . ' + str(G.date['year']))
            statusbar_message()

        def save_game():
            G.bought_tiles = []
            soils = []
            for y in range(G.SIZE['y']):
                G.bought_tiles.append([])
                soils.append([])
                for x in range(G.SIZE['x']): 
                    G.bought_tiles[y].append(G.tiles[y][x].isBought)
                    soils[y].append(G.tiles[y][x].soil_type)
            saved_data = {0: G.bought_tiles, 1: soils, 2: G.my_buildings, 3: G.capital, 4: G.date}
            with open('save.dat', 'wb') as save:
                pickle.dump([saved_data], save, protocol=5)
            save.close()
            
        def load_game():
            finish_game()
            with open('save.dat', 'rb') as save:
                loaded_data = pickle.load(save)
            save.close()
            G.capital = loaded_data[0][3]
            G.date = loaded_data[0][4]
            tiles_area_init()
            for y in range(G.SIZE['y']):
                for x in range(G.SIZE['x']):            
                    G.tiles[y][x].soil_type = loaded_data[0][1][y][x]
                    G.tiles[y][x].setStyleSheet("background-image : url(objs/"+G.tiles[y][x].soil_type+".bmp); border: 0px;")
                    G.tiles[y][x].isBought = loaded_data[0][0][y][x]
                    if G.tiles[y][x].isBought:
                        G.bought_tiles.append(G.tiles[y][x])
                        G.tiles[y][x].setStyleSheet("background-image : url(objs/"+G.tiles[y][x].soil_type+".bmp); border: 1px solid #00ff00;")
            storehouse_tile.append(G.tiles[loaded_data[0][2][0].y][loaded_data[0][2][0].x])
            G.my_buildings = loaded_data[0][2]
            for building in loaded_data[0][2]:
                G.tiles[building.y][building.x].setStyleSheet("background-image : url(objs/"+building.icon+".bmp); border: 1px solid #00ff00;")
                G.tiles[building.y][building.x].itsBuilding = building
                
            left_tab_init()
            self.date_label.setText(str(G.date['day']) + ' . ' + str(G.date['month']) + ' . ' + str(G.date['year']))

        # KEYBOARD ACTIONS BLOCK
            
        def up():
            if G.picked_tiles and G.picked_tiles[0].y:
                G.tiles[G.picked_tiles[0].y - 1][ G.picked_tiles[0].x].picking()
                G.picked_tiles[0].unpicking()
                statusbar_message()
                    
        def down():
            if (G.picked_tiles and G.picked_tiles[0].y < (G.SIZE['y'] - 1)):
                G.tiles[G.picked_tiles[0].y + 1][ G.picked_tiles[0].x].picking()
                G.picked_tiles[0].unpicking()
                statusbar_message()

        def left():
            if G.picked_tiles and G.picked_tiles[0].x:
                G.tiles[G.picked_tiles[0].y][ G.picked_tiles[0].x - 1].picking()
                G.picked_tiles[0].unpicking()
                statusbar_message()
 
        def right():
            if (G.picked_tiles and G.picked_tiles[0].x < (G.SIZE['x'] - 1)):
                G.tiles[G.picked_tiles[0].y][ G.picked_tiles[0].x + 1].picking()
                G.picked_tiles[0].unpicking()
                statusbar_message()
        
        self.up = QtGui.QAction(MainWindow)
        self.up.setShortcut("Up")
        self.up.triggered.connect(up)
        self.Tiles_area.addAction(self.up)
        self.down = QtGui.QAction(MainWindow)
        self.down.setShortcut("Down")
        self.down.triggered.connect(down)
        self.Tiles_area.addAction(self.down)
        self.left = QtGui.QAction(MainWindow)
        self.left.setShortcut("Left")
        self.left.triggered.connect(left)
        self.Tiles_area.addAction(self.left)
        self.right = QtGui.QAction(MainWindow)
        self.right.setShortcut("Right")
        self.right.triggered.connect(right)
        self.Tiles_area.addAction(self.right)
        
        # END OF KEYBOARD ACTIONS BLOCK

        question = QtWidgets.QDialog(MainWindow)
        ui = Ui_Exit_Widget()
        ui.setupUi(question, 1)
        question.accepted.connect(MainWindow.close)
        
        game_over = QtWidgets.QDialog(MainWindow)
        ui = Ui_Exit_Widget()
        ui.setupUi(game_over, 2)
        game_over.accepted.connect(new_game)
        game_over.rejected.connect(MainWindow.close)
        
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action.setShortcut("Ctrl+N")
        self.action.triggered.connect(new_game)
        self.action_2 = QtGui.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_2.setShortcut("Ctrl+L")
        self.action_2.triggered.connect(load_game)
        self.action_3 = QtGui.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_3.setShortcut("Ctrl+S")
        self.action_3.triggered.connect(save_game)
        self.action_5 = QtGui.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_5.setCheckable(True)
        self.action_5.setChecked(True)
        self.action_5.setShortcut("Alt+S")
        self.action_7 = QtGui.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_7.setShortcut("Ctrl+Q")
        self.action_7.triggered.connect(question.show)
        self.actionHelf = QtGui.QAction(MainWindow)
        self.actionHelf.setObjectName("actionHelf")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuGame.addAction(self.action)
        self.menuGame.addAction(self.action_2)
        self.menuGame.addAction(self.action_3)
        self.menuGame.addSeparator()
        self.menuGame.addAction(self.action_5)
        self.menuGame.addSeparator()
        self.menuGame.addAction(self.action_7)
        self.menu.addAction(self.actionHelf)
        self.menu.addSeparator()
        self.menu.addAction(self.actionAbout)
        self.menubar.addAction(self.menuGame.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sakhalin"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-G.SIZE:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">01.03.1890</p></body></html>"))
        self.menuGame.setTitle(_translate("MainWindow", "Game"))
        self.menu.setTitle(_translate("MainWindow", "?"))
        self.action.setText(_translate("MainWindow", "New game"))
        self.action_2.setText(_translate("MainWindow", "Load"))
        self.action_3.setText(_translate("MainWindow", "Save"))
        self.action_5.setText(_translate("MainWindow", "Sound"))
        self.action_7.setText(_translate("MainWindow", "Exit"))
        self.actionHelf.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
