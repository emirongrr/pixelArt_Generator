import random
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from path import *

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(589, 392)
        MainWindow.setFixedSize(590,395)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 271, 351))
        self.label.setPixmap(QtGui.QPixmap("pixel art.png"))
        self.label.setObjectName("label")

        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(340, 70, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setTickInterval(3)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(number_of_head)
        self.horizontalSlider.valueChanged['int'].connect(self.sliderValue)

        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(340, 130, 160, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.setTickInterval(3)
        self.horizontalSlider_2.setMinimum(1)
        self.horizontalSlider_2.setMaximum(number_of_glasses)
        self.horizontalSlider_2.valueChanged['int'].connect(self.sliderValue2)

        self.horizontalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(340, 190, 160, 22))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalSlider_3.setTickInterval(3)
        self.horizontalSlider_3.setMinimum(1)
        self.horizontalSlider_3.setMaximum(number_of_beard)
        self.horizontalSlider_3.valueChanged['int'].connect(self.sliderValue3)

        self.horizontalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(340, 250, 160, 22))
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.horizontalSlider_4.setTickInterval(3)
        self.horizontalSlider_4.setMinimum(1)
        self.horizontalSlider_4.setMaximum(number_of_body)
        self.horizontalSlider_4.valueChanged['int'].connect(self.sliderValue4)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(312, 280, 91, 41))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(418, 280, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 40, 60, 13))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 100, 60, 13))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 160, 60, 13))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 220, 60, 13))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 5, 60, 13))
        self.label_6.setObjectName("label_6")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 589, 21))

        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.getRandom)
        self.pushButton_2.clicked.connect(self.getAll)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pixel_artGenerator"))
        MainWindow.setWindowIcon(QIcon('heart.png'))
        self.pushButton.setText(_translate("MainWindow", "RANDOMIZE"))
        self.pushButton_2.setText(_translate("MainWindow", "GET ALL"))
        self.label_2.setText(_translate("MainWindow", "HEAD: "+str(number_of_head)))
        self.label_3.setText(_translate("MainWindow", "GLASSES: "+str(number_of_glasses)))
        self.label_4.setText(_translate("MainWindow", "BEARD: "+str(number_of_beard)))
        self.label_5.setText(_translate("Mainwindow",  "BODY: "+str(number_of_body)))
        self.label_6.setText(_translate("Mainwindow", "TOTAL:"+str(TOTAL)))

    def getRandom(self):
        global x, y, z, q
        x = random.randint(1, number_of_body)
        y = random.randint(1, number_of_glasses)
        z = random.randint(1, number_of_head)
        q = random.randint(1, number_of_beard)

        background = Image.open("source/body/body{}.png".format((x)))
        glasses = Image.open(("source/glasses/glasses{}.png".format(y)))
        foreground = Image.open(("source/head/head{}.png".format(z)))
        lastground = Image.open(("source/beard/beard{}.png".format(q)))

        background.paste(foreground, (94, 5), foreground)
        background.paste(glasses, (73, 86), glasses)
        background.paste(lastground, (147, 258), lastground)
        background.save("myChar/newMergeChar{}+{}+{}+{}.png".format(x, y, z, q), "PNG")
        self.label.setPixmap(QtGui.QPixmap("myChar/newMergeChar{}+{}+{}+{}.png".format(x, y, z, q)))
        self.horizontalSlider.setValue(z)
        self.horizontalSlider_2.setValue(y)
        self.horizontalSlider_3.setValue(q)
        self.horizontalSlider_4.setValue(x)



    def getAll(self):

       for a in range(1,number_of_body+1):
           for b in range(1,number_of_glasses+1):
               for c in range(1,number_of_head+1):
                   for d in range(1,number_of_beard+1):

                        background = Image.open("source/body/body{}.png".format((a)))
                        glasses = Image.open(("source/glasses/glasses{}.png".format(b)))
                        foreground = Image.open(("source/head/head{}.png".format(c)))
                        lastground = Image.open(("source/beard/beard{}.png".format(d)))

                        background.paste(foreground, (94, 5), foreground)
                        background.paste(glasses, (73, 86), glasses)
                        background.paste(lastground, (147, 258), lastground)
                        background.save("myChar/newMergeChar{}+{}+{}+{}.png".format(a, b, c, d), "PNG")

    def sliderValue(self,value):

        global z
        try:
            background = Image.open("source/body/body{}.png".format((x)))
            glasses = Image.open(("source/glasses/glasses{}.png".format(y)))
            foreground = Image.open(("source/head/head{}.png".format(value)))
            lastground = Image.open(("source/beard/beard{}.png".format(q)))
            background.paste(foreground, (94, 5), foreground)
            background.paste(glasses, (73, 86), glasses)
            background.paste(lastground, (147, 258), lastground)
            background.save("myChar/newMergeChar{}+{}+{}+{}.png".format(x, y, value, q), "PNG")

            self.label.setPixmap(QtGui.QPixmap("myChar/newMergeChar{}+{}+{}+{}.png".format(x, y, value, q)))
            z = value
        except NameError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Dont be quick")
            msg.setInformativeText('Please first of all click RANDOMIZE')
            msg.setWindowTitle("Error")
            msg.exec_()


    def sliderValue2(self,value):

        global y
        try:
            background = Image.open("source/body/body{}.png".format((x)))
            glasses = Image.open(("source/glasses/glasses{}.png".format(value)))
            foreground = Image.open(("source/head/head{}.png".format(z)))
            lastground = Image.open(("source/beard/beard{}.png".format(q)))

            background.paste(foreground, (94, 5), foreground)
            background.paste(glasses, (73, 86), glasses)
            background.paste(lastground, (147, 258), lastground)
            background.save("myChar/newMergeChar{}+{}+{}+{}.png".format(x, value, z, q), "PNG")

            self.label.setPixmap(QtGui.QPixmap("myChar/newMergeChar{}+{}+{}+{}.png".format(x,value,z,q)))
            y = value
        except NameError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Dont be quick")
            msg.setInformativeText('Please first of all click RANDOMIZE')
            msg.setWindowTitle("Error")
            msg.exec_()

    def sliderValue3(self,value):

        global q
        try:
            background = Image.open("source/body/body{}.png".format((x)))
            glasses = Image.open(("source/glasses/glasses{}.png".format(y)))
            foreground = Image.open(("source/head/head{}.png".format(z)))
            lastground = Image.open(("source/beard/beard{}.png".format(value)))

            background.paste(foreground, (94, 5), foreground)
            background.paste(glasses, (73, 86), glasses)
            background.paste(lastground, (147, 258), lastground)
            background.save("myChar/newMergeChar{}+{}+{}+{}.png".format(x, y, z, value), "PNG")
            self.label.setPixmap(QtGui.QPixmap("myChar/newMergeChar{}+{}+{}+{}.png".format(x,y,z,value)))
            q = value
        except NameError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Dont be quick")
            msg.setInformativeText('Please first click RANDOMIZE')
            msg.setWindowTitle("Error")
            msg.exec_()

    def sliderValue4(self,value):

        global x
        try:
            background = Image.open("source/body/body{}.png".format((value)))
            glasses = Image.open(("source/glasses/glasses{}.png".format(y)))
            foreground = Image.open(("source/head/head{}.png".format(z)))
            lastground = Image.open(("source/beard/beard{}.png".format(q)))

            background.paste(foreground, (94, 5), foreground)
            background.paste(glasses, (73, 86), glasses)
            background.paste(lastground, (147, 258), lastground)
            background.save("myChar/newMergeChar{}+{}+{}+{}.png".format(value, y, z, q), "PNG")
            self.label.setPixmap(QtGui.QPixmap("myChar/newMergeChar{}+{}+{}+{}.png".format(value,y,z,q)))
            x = value
        except NameError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Dont be quick")
            msg.setInformativeText('Please first of all click RANDOMIZE')
            msg.setWindowTitle("Error")
            msg.exec_()

if __name__ == "__main__":

    while True:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

