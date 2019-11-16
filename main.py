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



        conn.close()

        # print(data)


app = QtWidgets.QApplication(sys.argv)
ex = W()
ex.show()
sys.exit(app.exec_())
