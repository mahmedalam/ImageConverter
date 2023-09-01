from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(637, 185)
        MainWindow.setStyleSheet("background-color: #2d3233;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openBtn.setGeometry(QtCore.QRect(10, 60, 220, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.openBtn.setFont(font)
        self.openBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.openBtn.setStyleSheet("color: white;\n"
"background-color:  #383838;\n"
"border: 1.5px solid black;\n"
"border-radius: 20px;")
        self.openBtn.setObjectName("openBtn")
        self.exportBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exportBtn.setGeometry(QtCore.QRect(404, 60, 220, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.exportBtn.setFont(font)
        self.exportBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exportBtn.setStyleSheet("color: white;\n"
"background-color:  #383838;\n"
"border: 1.5px solid black;\n"
"border-radius: 20px;")
        self.exportBtn.setObjectName("exportBtn")
        self.typeComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.typeComboBox.setGeometry(QtCore.QRect(241, 80, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.typeComboBox.setFont(font)
        self.typeComboBox.setStyleSheet("*{\n"
"    color: white;\n"
"    background-color:  #383838;\n"
"}\n"
"\n"
"QComboBox{\n"
"    padding: 0px 0px 1.5px 50px;\n"
"}")
        self.typeComboBox.setObjectName("typeComboBox")
        self.typeComboBox.addItem("")
        self.typeComboBox.addItem("")
        self.typeComboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(297, 50, 38, 24))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Converter"))
        self.openBtn.setText(_translate("MainWindow", "Open File"))
        self.exportBtn.setText(_translate("MainWindow", "Export"))
        self.typeComboBox.setItemText(0, _translate("MainWindow", "PNG"))
        self.typeComboBox.setItemText(1, _translate("MainWindow", "JPEG"))
        self.typeComboBox.setItemText(2, _translate("MainWindow", "WEBP"))
        self.label.setText(_translate("MainWindow", "Type"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
