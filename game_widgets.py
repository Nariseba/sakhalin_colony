# Form implementation generated from reading ui file 'exit_question.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from global_vars import *

# Всплывающее окно при выходе из игры
class Ui_Exit_Widget(object):
    def setupUi(self, Question, state):
        Question.resize(255, 96)
        self.buttonBox = QtWidgets.QDialogButtonBox(Question)
        self.buttonBox.setGeometry(QtCore.QRect(50, 50, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.No|QtWidgets.QDialogButtonBox.StandardButton.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Question)
        self.label.setGeometry(QtCore.QRect(10, 0, 231, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        QtCore.QMetaObject.connectSlotsByName(Question)
        self.buttonBox.accepted.connect(Question.accept) # type: ignore
        self.buttonBox.rejected.connect(Question.reject) # type: ignore
        if state == 1:
            self.label.setText("Do you really want to quit the game?")
            Question.setWindowTitle("Question")
        if state == 2:
            self.label.setText("GAME OVER! Start a new game?")
            Question.setWindowTitle("GAME OVER")

# Всплывающее окно для продаже товаров
class Ui_Sale_Widget(object):
        
    def setupUi(self, Dialog, price, title, G):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(335, 280)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(335, 280))
        Dialog.setMaximumSize(QtCore.QSize(335, 280))
        Dialog.setWindowTitle(title)

        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("background-color: black;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.frame)  #удалить?
        
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)        
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.addWidget(self.pushButton, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 4, 1)

        goods_icon, sale_input, sale_price_label, sale_output = [], [], [], []
        for el in range(9):
            goods_icon.append(QtWidgets.QLabel(self.frame))
            goods_icon[el].setMinimumSize(QtCore.QSize(25, 25))
            goods_icon[el].setMaximumSize(QtCore.QSize(25, 25))
            goods_icon[el].setPixmap(QtGui.QPixmap("objs/"+G.GOODS_NAME[el+1]+".bmp"))
            goods_icon[el].setIndent(0)
            goods_icon[el].setObjectName(G.GOODS_NAME[el]+"_icon")
            self.gridLayout.addWidget(goods_icon[el], el, 0, 1, 1)
        
            sale_input.append(QtWidgets.QLineEdit(self.frame))
            sale_input[el].setMinimumSize(QtCore.QSize(0, 20))
            sale_input[el].setMaximumSize(QtCore.QSize(45, 45))
            sale_input[el].setStyleSheet("border: 1px solid white;\n color: white;")
            sale_input[el].setObjectName(G.GOODS_NAME[el+1]+"input")
            self.gridLayout.addWidget(sale_input[el], el, 1, 1, 1)     
            if len(sale_input[el].text()) == 0:
                sale_input[el].setText('0')
        
            sale_price_label.append(QtWidgets.QLabel(self.frame))
            sale_price_label[el].setStyleSheet("border: 1px solid white;\n color: white;")
            sale_price_label[el].setObjectName(G.GOODS_NAME[el+1]+"_price")
            sale_price_label[el].setText(str(price[el]))
            sale_price_label[el].setMaximumSize(QtCore.QSize(50, 50))
            self.gridLayout.addWidget(sale_price_label[el], el, 2, 1, 1)
        
            sale_output.append(QtWidgets.QLabel(self.frame))
            sale_output[el].setStyleSheet("border: 1px solid white;\n color: white;")
            sale_output[el].setObjectName(G.GOODS_NAME[el+1]+"_output")
            sale_output[el].setMinimumSize(QtCore.QSize(95, 0))    
            self.gridLayout.addWidget(sale_output[el], el, 3, 1, 1)
        def calculated():
            total_for_trade = 0
            for el in range(9):
                try:
                    sale_output[el].setText(str(int(sale_input[el].text())*price[el]))
                    total_for_trade += int(sale_output[el].text())
                except(ValueError):
                    sale_output[el].setText('-')
                Dialog.setWindowTitle('Trade  -  ' + str(total_for_trade))
            return total_for_trade
        
        def all_for_trade():
            for el in range(9):
                sale_input[el].setText(G.capital[el+1])
                
        def sold ():
            permission = []
            for el in range(9):
                permission.append(int(G.capital[el+1]) >= int(sale_input[el].text()))
            if  permission.count(False) == 0:
                for el in range(9):
                    G.capital[el+1] = str(int(G.capital[el+1]) - int(sale_input[el].text()))
                G.capital[0] = str(int(G.capital[0]) + calculated())
                Dialog.close()
        
        def bought ():
                if int(G.capital[0]) >= calculated():
                    for el in range(9):
                        G.capital[el+1] = str(int(G.capital[el+1]) + int(sale_input[el].text()))
                    G.capital[0] = str(int(G.capital[0]) - calculated())
                    Dialog.close()
                else: pass
                
        def input_control():
            for el in range(9):
                try:
                    int(sale_input[el].text())
                except(ValueError):
                    sale_input[el].setText('0')

        for el in range(9):
            sale_input[el].textChanged.connect(calculated)
            sale_input[el].cursorPositionChanged.connect(input_control)
        
        if price[1] == 1:
            self.pushButton.clicked.connect(sold)
            self.pushButton.setText("Sell")
            self.pushButton_3 = QtWidgets.QPushButton(Dialog)
            self.pushButton_3.setObjectName("pushButton_3")   
            self.gridLayout_2.addWidget(self.pushButton_3, 3, 1, 1, 1)
            self.pushButton_3.setText("All")
            self.pushButton_3.clicked.connect(all_for_trade)
            
        else:
            self.pushButton.clicked.connect(bought)
            self.pushButton.setText("Buy")
            
        self.pushButton_2.clicked.connect(Dialog.close)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
                    
        calculated()    

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
