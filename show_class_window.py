import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel , QLineEdit , QPushButton
from PyQt5.QtGui import QFont
import sqlite3
import link

#database
con = sqlite3.connect('data.bd')
c = con.cursor()

#window
app = QApplication(sys.argv)

root = QMainWindow()
root.setWindowTitle('Class Manager')
root.resize(600 , 400)

#funcions


#window
root.show()
sys.exit(app.exec_())