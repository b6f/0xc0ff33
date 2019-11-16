import sys
import sqlite3
from PyQt5 import QtWidgets, uic


class W(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.tableWidget.setColumnCount(7)

        for i, name in enumerate(('ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах',
                                  'Описание вкуса', 'Цена', 'Объем упаковки')):
            self.tableWidget.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(name))
            self.tableWidget.setColumnWidth(i, 160)

        conn = sqlite3.connect('coffee.sqlite')
        cur = conn.cursor()

        types = cur.execute("""SELECT title FROM types""").fetchall()
        fired = cur.execute("""SELECT name FROM fired""").fetchall()
        data = cur.execute("""SELECT * FROM catalog""").fetchall()

        for i in range(len(data)):
            rc = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rc)
            chunk = list(data[i])
            chunk[1] = types[chunk[1] - 1][0]
            chunk[2] = fired[chunk[2] - 1][0]
            chunk[3] = 'молотый' if chunk[3] else 'в зернах'

            for j in range(7):
                self.tableWidget.setItem(rc, j, QtWidgets.QTableWidgetItem(str(chunk[j])))


        conn.close()



app = QtWidgets.QApplication(sys.argv)
ex = W()
ex.show()
sys.exit(app.exec_())
