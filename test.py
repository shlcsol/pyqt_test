# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import  QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 120, 151, 61))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Hello pyqt5"))

if __name__ == '__main__':
    #测试
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

