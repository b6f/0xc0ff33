# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(387, 458)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 331, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 331, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 331, 16))
        self.label_3.setObjectName("label_3")
        self.type_name = QtWidgets.QComboBox(Form)
        self.type_name.setGeometry(QtCore.QRect(20, 90, 341, 26))
        self.type_name.setEditable(False)
        self.type_name.setObjectName("type_name")
        self.fire_type = QtWidgets.QComboBox(Form)
        self.fire_type.setGeometry(QtCore.QRect(20, 150, 341, 26))
        self.fire_type.setEditable(False)
        self.fire_type.setObjectName("fire_type")
        self.ground = QtWidgets.QCheckBox(Form)
        self.ground.setGeometry(QtCore.QRect(20, 190, 87, 20))
        self.ground.setObjectName("ground")
        self.id = QtWidgets.QSpinBox(Form)
        self.id.setGeometry(QtCore.QRect(20, 30, 341, 24))
        self.id.setSuffix("")
        self.id.setMinimum(-1)
        self.id.setProperty("value", -1)
        self.id.setObjectName("id")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 230, 331, 16))
        self.label_5.setObjectName("label_5")
        self.taste_description = QtWidgets.QLineEdit(Form)
        self.taste_description.setGeometry(QtCore.QRect(20, 250, 331, 21))
        self.taste_description.setObjectName("taste_description")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 290, 331, 16))
        self.label_4.setObjectName("label_4")
        self.price = QtWidgets.QSpinBox(Form)
        self.price.setGeometry(QtCore.QRect(20, 310, 341, 24))
        self.price.setSuffix("")
        self.price.setMinimum(10)
        self.price.setMaximum(10000)
        self.price.setProperty("value", 100)
        self.price.setObjectName("price")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 350, 331, 16))
        self.label_6.setObjectName("label_6")
        self.vol = QtWidgets.QSpinBox(Form)
        self.vol.setGeometry(QtCore.QRect(20, 370, 341, 24))
        self.vol.setSuffix("")
        self.vol.setMinimum(10)
        self.vol.setMaximum(10000)
        self.vol.setProperty("value", 100)
        self.vol.setObjectName("vol")
        self.done = QtWidgets.QPushButton(Form)
        self.done.setGeometry(QtCore.QRect(130, 410, 113, 32))
        self.done.setObjectName("done")

        self.retranslateUi(Form)
        self.type_name.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавить"))
        self.label.setText(_translate("Form", "ID (оставьте -1 чтобы создать новую запись):"))
        self.label_2.setText(_translate("Form", "Название сорта"))
        self.label_3.setText(_translate("Form", "Степерь обжарки"))
        self.ground.setText(_translate("Form", "Молотый"))
        self.label_5.setText(_translate("Form", "Описание вкуса"))
        self.label_4.setText(_translate("Form", "Цена:"))
        self.label_6.setText(_translate("Form", "Объем:"))
        self.done.setText(_translate("Form", "Готово"))
