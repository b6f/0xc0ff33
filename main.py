import sys
import sqlite3
from PyQt5 import QtWidgets, QtCore

from addEditCoffeeForm import Ui_Form as AddEdit
from main_interface import Ui_MainWindow as MainWindow


class Add(QtWidgets.QMainWindow, AddEdit):
    def __init__(self, parent, types, fire_types, add_callback):
        super().__init__(parent)

        super().setupUi(self)

        c.show()

        self.type_name.addItems(types)
        self.fire_type.addItems(fire_types)

        self.done_cb = add_callback
        self.done.clicked.connect(self.klk)

    def klk(self):
        zid = self.id.value()
        type_name = self.type_name.currentIndex()
        fired_type = self.fire_type.currentIndex()
        ground = self.ground.isChecked()
        td = self.taste_description.text()
        price = self.price.value()
        vol = self.vol.value()

        self.done_cb(zid, type_name, fired_type, ground, td, price, vol)


class W(QtWidgets.QMainWindow, MainWindow):
    def __init__(self):
        super().__init__()

        super().setupUi(self)

        self.tableWidget.setColumnCount(7)

        for i, name in enumerate(('ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах',
                                  'Описание вкуса', 'Цена', 'Объем упаковки')):
            self.tableWidget.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(name))
            self.tableWidget.setColumnWidth(i, 160)

        self.conn = sqlite3.connect('data/coffee.sqlite')
        cur = self.conn.cursor()

        self.addButton.clicked.connect(self.open_add)

        self.types = cur.execute("""SELECT title FROM types""").fetchall()
        self.fired = cur.execute("""SELECT name FROM fired""").fetchall()
        self.data = cur.execute("""SELECT * FROM catalog""").fetchall()
        self.retable(self.data)

    def retable(self, data):
        self.tableWidget.setRowCount(0)

        for i in range(len(data)):
            rc = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rc)
            chunk = list(data[i])
            chunk[1] = self.types[chunk[1] - 1][0]
            chunk[2] = self.fired[chunk[2] - 1][0]
            chunk[3] = 'молотый' if chunk[3] else 'в зернах'

            id_obj = QtWidgets.QTableWidgetItem(str(chunk[0]))
            id_obj.setFlags(id_obj.flags() ^ QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(rc, 0, id_obj)

            for j in range(1, 7):
                self.tableWidget.setItem(rc, j, QtWidgets.QTableWidgetItem(str(chunk[j])))

    def closeEvent(self, e):
        self.conn.commit()
        self.conn.close()

    def item_inject(self, zid, itype, ftype, ground, td, price, vol):
        itype += 1
        ftype += 1

        if zid == -1:
            self.conn.execute("""INSERT INTO catalog (type, fired, ground, 
            taste_description, price, size) VALUES (?, ?, ?, ?, ?, ?)""",
                              (itype, ftype, ground, td, price, vol))
            zid = len(self.data) + 1
            self.data.append((zid, itype, ftype, ground, td, price, vol))

        else:
            self.conn.execute("""DELETE FROM catalog WHERE id = ?""", (zid, ))
            self.conn.execute("""INSERT INTO catalog (id, type, fired, ground, 
                        taste_description, price, size) VALUES (?, ?, ?, ?, ?, ?, ?)""",
                              (zid, itype, ftype, ground, td, price, vol))
            self.data[zid - 1] = (zid, itype, ftype, ground, td, price, vol)
        self.retable(self.data)

    def open_add(self):
        of = Add(self, map(lambda x: x[0], self.types), map(lambda x: x[0], self.fired), self.item_inject)
        of.show()


app = QtWidgets.QApplication(sys.argv)
ex = W()
ex.show()
sys.exit(app.exec_())
