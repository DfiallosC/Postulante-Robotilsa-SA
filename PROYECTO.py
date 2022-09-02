import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qtwidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qtimer, Qtime

from PyQt5.vic import loadUi

if __name__ == "__main__": #Condicional que comprueba si ha sido ejecutado
    app = QtWidgets.QApplication(sys.argv) #crea un objeto de aplicación (Argumentos de sys)
    MainWindow = QtWidgets.QMainWindow() #Instancia
    ui = Ui_MainWindow() #instancia
    ui.setupUi(MainWindow) #Llama al Metodo setupUI con MainWindow como argumento
    
class VentanaPrincipal(QMainWindow):
    
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('PROYECTO.ui', self)

        timer = QTimer(self)
        timer.timeout.connect(self.displayTime)
        timer.start(1000)
        
    def displayTime(self):
         currentTime = QTime.currentTime()
         displayText = currentTime.toString('hh:mm:ss')
         self.L_hora.setText(displayText)
         self.lcdNumber.display(displayText)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(675, 455)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 40, 361, 391))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 190, 181, 71))
        self.pushButton.setObjectName("pushButton")
        self.L_dia = QtWidgets.QLabel(self.centralwidget)
        self.L_dia.setGeometry(QtCore.QRect(460, 60, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.L_dia.setFont(font)
        self.L_dia.setObjectName("L_dia")
        self.L_hora = QtWidgets.QLabel(self.centralwidget)
        self.L_hora.setGeometry(QtCore.QRect(460, 130, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.L_hora.setFont(font)
        self.L_hora.setAlignment(QtCore.Qt.AlignCenter)
        self.L_hora.setObjectName("L_hora")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(560, 120, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setObjectName("lcdNumber")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Postulante para ROBOTILSA S.A."))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Luke Skywalker"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "C-3PO"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "R2-D2"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "Darth Vader"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "Leia Organa"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "Owen Lars"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "Beru Whitesun Lars"))
        item = self.listWidget.item(7)
        item.setText(_translate("MainWindow", "R5-D4"))
        item = self.listWidget.item(8)
        item.setText(_translate("MainWindow", "Biggs Darklighter"))
        item = self.listWidget.item(9)
        item.setText(_translate("MainWindow", "Obi-Wan Kenobi"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "REQUEST"))
        self.L_dia.setText(_translate("MainWindow", "02/09/2022"))
        self.L_hora.setText(_translate("MainWindow", "7:06:00"))

    app = QApplication(sys.argv)
    MainWindow.show()
    sys.exit(app.exec_())
