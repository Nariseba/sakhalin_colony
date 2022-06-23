from random import random as rnd
from time import time
from functools import reduce
from random import randint
from global_vars import Global as G
from PyQt5.QtWidgets import QGraphicsRectItem
from PyQt5.QtGui import QBrush, QPixmap, QPen, QColor
from PyQt5.QtCore import Qt

class Population():
    def __init__(self):
        self.total = 25
        self.housing = 50
        self.jobs = 0
        self.unemployment = self.total - self.jobs
        self.people = [self.total, self.housing, self.jobs,  self.unemployment]
    def growthAndStarvation(self):
        if G.capital[1] >= self.total and rnd() < 0.01:
            self.total = int(self.total*1.04)
            if G.capital[0] and rnd() < 0.02:
                self.total = int(self.total*1.04)
        elif G.capital[1] < self.total and rnd() < 0.24:
            self.total = int(self.total * 0.9)
            G.MW.statusbar_message('Starvation!')
    def consumption(self):
        if 0 <= G.capital[0] - self.jobs:
            G.capital[0] = G.capital[0] - self.jobs
        if 0 <= G.capital[1] - self.total:
            G.capital[1] = G.capital[1] - self.total
    def update(self):
        self.unemployment = self.total
        self.jobs = 0 
    def live(self):
        self.consumption()
        self.growthAndStarvation()
        self.people = [self.total, self.housing, self.jobs,  self.unemployment]
        for i in range(4):
            G.MW.popLabel.numb[i].setText(f'{self.people[i]}')      
            
class Building():
    def __init__(self, id,  icon, price, repair_cost, prod, lifetime, soil, seasonsStr, max_lifetime, days_to_build, isFinished, workers, discription, y, x):
        self.id = id
        self.icon = icon
        self.price = price
        self.repair_cost = repair_cost
        self.prod = prod
        self.lifetime = lifetime
        self.soil = soil
        self.seasons = tuple(map(int,seasonsStr))
        self.max_lifetime = max_lifetime
        self.days_to_build = days_to_build
        self.discription = discription
        self.isFinished = False
        self.workers = workers
        self.y, self.x = y, x
        brush = QBrush(QPixmap("objs/"+self.icon+".bmp"))
        self.img = QGraphicsRectItem(x*G.TS, y*G.TS, G.TS, G.TS, G.MW.gameArea.buildingPlast)
        self.img.setBrush(brush)
        self.statusImg = QGraphicsRectItem(x*G.TS+13, y*G.TS+11, 12, 14, G.MW.gameArea.buildingPlast)
        self.statusImg.setPen(QPen(Qt.NoPen))
        self.isLocked = False

    def __str__(self):
        return self.icon
        
    def isWork_time(self):
        D = G.MW.dateWidget
        if D.date.timetuple()[1] <= 2 and self.seasons[0]:
            return True
        elif D.date.timetuple()[1] == 12 and self.seasons[0]:
            return True
        elif 3 <= D.date.timetuple()[1] <= 5 and self.seasons[1]:
            return True
        elif 6 <= D.date.timetuple()[1] <= 8 and self.seasons[2]:
            return True   
        elif 9 <= D.date.timetuple()[1] <= 11 and self.seasons[3]:
            return True   
        return False
    def production(self):        
        if self.isFinished: 
            if self.isWork_time():
                permission = True
                if self.workers > G.MW.population.unemployment:
                    permission = False
                    self.statusImg.setBrush(QBrush(QPixmap('objs/needMorePeople.png')))
                else: 
                    for el in range(10):
                        if (G.capital[el] + self.prod[el]) < 0:
                            permission = False
                    if permission:
                        self.statusImg.setBrush(QBrush(Qt.NoBrush))
                        G.MW.population.unemployment -= self.workers
                        G.MW.population.jobs += self.workers
                        for el in range(1,9):
                            if self.prod[el] >= 0:
                                G.capital[el] = G.capital[el] + self.prod[el] * (G.tiles[self.y][self.x].resource[el-1]/10)
                            else: G.capital[el] = G.capital[el] + self.prod[el] - (G.tiles[self.y][self.x].resource[el-1]/10)*self.prod[el]
                    else: 
                        self.statusImg.setBrush(QBrush(QPixmap('objs/needResources.png')))
            else: self.statusImg.setBrush(QBrush(QPixmap('objs/notInSeason.png')))
            self.lifetime -= 1
            if self.lifetime <= 30:
                self.statusImg.setBrush(QBrush(QPixmap('objs/soonToDestruct.png')))
            if self.lifetime <= 0:
                t = G.tiles[self.y][self.x]
                G.MW.gameArea.buildingPlast.removeFromGroup(self.img)
                G.MW.gameArea.buildingPlast.removeFromGroup(self.statusImg)
                del self.img
                del self.statusImg
                t.itsBuilding = False
                G.my_buildings.remove(self)
        else:
            self.days_to_build = self.days_to_build - 1
            self.statusImg.setBrush(QBrush(QPixmap('objs/IsNotFinished.png')))
            if self.days_to_build == 0:
                self.isFinished = True

class Tile():
    multipicking_mode = False
    shift_picking_mode = False 
    def focus_up():
        if G.picked_tiles and G.picked_tiles[0].y:
            tile = G.picked_tiles[0]
            next_tile = G.tiles[G.picked_tiles[0].y//G.TS - 1][ G.picked_tiles[0].x//G.TS]
            while len(G.picked_tiles): G.picked_tiles[-1].unpicking()
            next_tile.picking()
            G.MW.statusbar_message()
    def focus_down():
        if (G.picked_tiles and G.picked_tiles[0].y < (G.SIZE['y'] - 1)*G.TS):
            tile = G.picked_tiles[0]
            next_tile = G.tiles[G.picked_tiles[0].y//G.TS + 1][ G.picked_tiles[0].x//G.TS]
            while len(G.picked_tiles): G.picked_tiles[-1].unpicking()
            next_tile.picking()
            G.MW.statusbar_message()
    def focus_left():
        if G.picked_tiles and G.picked_tiles[0].x:
            tile = G.picked_tiles[0]
            next_tile = G.tiles[G.picked_tiles[0].y//G.TS][ G.picked_tiles[0].x//G.TS - 1]
            while len(G.picked_tiles): G.picked_tiles[-1].unpicking()
            next_tile.picking()
            G.MW.statusbar_message()
    def focus_right():
        if (G.picked_tiles and G.picked_tiles[0].x < (G.SIZE['x'] - 1)*G.TS):
            tile = G.picked_tiles[0]
            next_tile = G.tiles[G.picked_tiles[0].y//G.TS][ G.picked_tiles[0].x//G.TS + 1]
            while len(G.picked_tiles): G.picked_tiles[-1].unpicking()
            next_tile.picking()
            G.MW.statusbar_message()
    def rndTile():
        x = randint(0, G.SIZE['x'] - 1)
        y = randint(0, G.SIZE['y'] - 1)
        return G.tiles[y][x]
    def __init__(self, y:int, x:int):
        self.isBought = False
        self.itsBuilding = False
        self.isVisible = False
        self.isUpgrated = False
        self.h = 0      # height
        self.wet = 0    # wetness
        self.soil_type = 'sea'
        self.x = x*G.TS
        self.y = y*G.TS
        self.resource = [0,0,0,0,0,0,0,0]
        self.resImg = {'color':[], 'point':[], 'radius': []}
        self.rect = 0

    def setHeight(self, rad, radEllipse, island):
        if 0 < (radEllipse - rad):
            self.h += int((radEllipse - rad)/25)
        if island['centre'].count(self): self.h = 20
    def resTypes(self):
        rTypes = []
        for i in range(len(self.resource)):
            if self.resource[i] and not rTypes.count(i):
                rTypes.append(i)
        return rTypes
    def drawRes(self):
        gA = G.MW.gameArea
        for i in range(len(self.resImg['point'])):
                        r = self.resImg['radius'][i]
                        indx = G.resource_color.index(self.resImg['color'][i])
                        G.MW.settings.res_btns[indx].isChecked()
                        if G.MW.settings.res_btns[indx].isChecked():
                            gA.Brush = QBrush(self.resImg['color'][i])
                            gA.resPlast.addToGroup(gA.scene.addEllipse(self.resImg['point'][i].x(), self.resImg['point'][i].y(), r, r, gA.pen, gA.Brush))
    def color (self):
        #            red                            green                           blue
            color = [100 + self.h*2 - self.wet*2,    150 - self.h*4 - self.wet*3,    60 - self.h + self.wet*4]
            for i in range(3): 
                if color[i] > 255: 
                    color[i] = 255
                elif color[i] < 0: 
                    color[i] = 0
            return QColor(*color)
    def unpicking(self):
        G.picked_tiles.remove(self)
        while G.MW.gameArea.pickPlast.childItems(): G.MW.gameArea.pickPlast.removeFromGroup(G.MW.gameArea.pickPlast.childItems()[-1])
        del self.rect       
    def picking(self):
        if not self.isVisible: return False
        G.picked_tiles.append(self)
        self.rect = QGraphicsRectItem(self.x, self.y, G.TS, G.TS, G.MW.gameArea.pickPlast)
        self.rect.setPen(QPen(QColor(255,255,255,140), 2, Qt.DotLine))
        G.picked_tiles = list(set(G.picked_tiles))
        G.MW.scrollTilesArea.ensureVisible(G.picked_tiles[-1].x, G.picked_tiles[-1].y, 10, 10)
    def shift_picking(self):
        t = G.picked_tiles[-1]
        iy = 1 if (self.y - G.picked_tiles[-1].y) >= 0 else -1
        ix = 1 if (self.x - G.picked_tiles[-1].x) >= 0 else -1
        i = 1 + abs(self.x - G.picked_tiles[-1].x)//G.TS
        while self.y * iy >= G.picked_tiles[-1].y * iy:
            while self.x * ix != G.picked_tiles[-1].x * ix:
                G.picked_tiles.append(G.tiles[G.picked_tiles[-1].y//G.TS][G.picked_tiles[-1].x//G.TS + ix])
            if (G.picked_tiles[-1] != self):
                G.picked_tiles.append(G.tiles[G.picked_tiles[-i].y//G.TS + iy][G.picked_tiles[-i].x//G.TS])
            else: break 
        G.picked_tiles = list(set(filter(lambda el: el.isVisible, G.picked_tiles)))
        for tile in G.picked_tiles: tile.picking()
    def picking_on_click(self):
        if Tile.shift_picking_mode and G.picked_tiles:
            self.shift_picking()
        else:        
            if G.picked_tiles and not Tile.multipicking_mode:
                while G.picked_tiles:
                    for el in G.picked_tiles:
                        el.unpicking()
            if G.picked_tiles.count(self):
                self.unpicking()
            else:
                self.picking()
        G.MW.statusbar_message()                       
    def neighbours(self):
        try: yield G.tiles[self.y//G.TS+1][self.x//G.TS]
        except(IndexError): pass
        
        try: yield G.tiles[self.y//G.TS-1][self.x//G.TS]
        except(IndexError): pass
        
        try: yield G.tiles[self.y//G.TS][self.x//G.TS+1]
        except(IndexError): pass
        
        try: yield G.tiles[self.y//G.TS][self.x//G.TS-1]
        except(IndexError): pass

def landshaft():
    islands_amount = 15
    islands = {'centre':[], 'radius':[], 'rx':[], 'ry':[]}
    while len(islands['centre']) != islands_amount:
        x = randint(0, G.SIZE['x'] - 1)
        y = randint(0, G.SIZE['y'] - 1)
        islands['centre'].append((x, y))
        islands['rx'].append(randint(1, int(G.SIZE['y']/5)))
        islands['ry'].append(int(G.SIZE['y']/5) - islands['rx'][-1] + 1)    
        islands['radius'].append(int(G.SIZE['y']/7))
    return islands
    
def set_sea_tile(x, y , island):
        distances = [((x-X)**2 + (y-Y)**2) for (X,Y) in island['centre']]
        closest = island['centre'][distances.index(min(distances))]
        i = island['centre'].index(closest)
        try:
            dH = 0
            rad =((closest[1] - y) ** 2 + (closest[0] - x) ** 2)**0.5
            rx = island['rx'][i]
            ry = island['ry'][i]
            vectB = [x - closest[0] , y - closest[1]]
            modul = ((vectB[0]**2+vectB[1]**2)**0.5) * rx
            scalar = vectB[0] * rx
            cosF = scalar/modul
            sinF = (1 - cosF**2)**0.5
            radEllipse = (rx*ry/((rx*cosF)**2 + (ry*sinF)**2)**0.5)
            if radEllipse - rad >=  0:
                dH = int(radEllipse - rad)
                return False, dH
            elif radEllipse - rad >= -2 and rnd() > 0.6:
                dH = int(radEllipse - rad)
                return False, dH
        except(ZeroDivisionError): pass
        if closest == (x,y):
            dH = 20
            return False, dH
        return True, dH 
 
def set_wetnessMatrix(landshaftMatrix, T = None, average_wetness=None):
    if not T:
        T = time()
    matrix = []
    desert_centres = list()
    total = 0
    while len(desert_centres) < 15:
        x = randint(0, G.SIZE['x'] - 1)
        y = randint(0, G.SIZE['y'] - 1)
        if not landshaftMatrix[y][x][0]:
            desert_centres.append((x,y))
    for Y in range(G.SIZE['y']):
        matrix.append([])
        for X in range(G.SIZE['x']):
            if not landshaftMatrix[Y][X][0]:
                distances = [(((x-X)**2 + (y-Y)**2)**0.5) for x,y in desert_centres]
                wetness = int(min(distances)/2.5 - 8 + G.WETNESS) 
                matrix[Y].append(wetness)
                total += wetness
            else: (matrix[Y].append(0))
    average_wetness = total/(G.SIZE['x']*G.SIZE['y'])
    # if abs(average_wetness) > 0.1 :
        # return set_wetnessMatrix(landshaftMatrix, T, average_wetness)
    print(f'average_wetness: {average_wetness}')
    print(f'def set_wetness takes {time()-T} sec.') 
    return matrix
        
def setResourceMatrix(landshaftMatrix, wetnessMatrix):
    T = time()
    total = int(G.SIZE['x']*G.SIZE['y']*G.RESOURCES)
    resMatrix = []
    amounts = [0,0,0,0,0,0,0,0]
    def resAllocation():
        while True:
            x = randint(0, (G.SIZE['x'] - 1)*G.TS)
            y = randint(0, (G.SIZE['y'] - 1)*G.TS)
            if not landshaftMatrix[int(y/G.TS)][int(x/G.TS)][0]: # if it`s not on a sea tile
                return (x,y)
    while total: 
        loc = resAllocation()
        h = landshaftMatrix[int(loc[1]/G.TS)] [int(loc[0]/G.TS)] [1]
        w = wetnessMatrix[int(loc[1]/G.TS)] [int(loc[0]/G.TS)]
        resRND = [0 for i in range(8)]
        resRND[0] = (28 -0.6*h +1.8*w)*rnd()          # food 
        resRND[1] = (25 -0.5*h +1.3*w)*rnd()          # wood
        resRND[2] = (17 +0.3*h -0.5*w)*rnd()          # stone
        resRND[3] = (23 -0.2*h +2.4*w)*rnd()          # water
        resRND[4] = (16 +0.3*h       )*rnd()          # coal
        resRND[5] = (15 +0.5*h       )*rnd()          # iron
        resRND[6] = (10 +0.0*h -1.6*w)*rnd()          # oil
        resRND[7] = (3  +1.4*h       )*rnd()          # gold
        resType = resRND.index(max(resRND))
        amounts[resType] += 1
        total -= 1
        resMatrix.append((resType, loc))
    # for i in range(8):
        # print(f'{G.GOODS_NAME[1+i]} : {amounts[i]} : {amounts[i]/amounts[7]}')
    print(f'def setResourceMatrix takes:{time()-T} sec')
    return resMatrix

          