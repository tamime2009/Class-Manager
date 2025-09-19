import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel , QLineEdit , QPushButton
from PyQt5.QtGui import QFont
import sqlite3

#database
con = sqlite3.connect('data.bd')
c = con.cursor()

#window
app = QApplication(sys.argv)

root = QMainWindow()
root.setWindowTitle('Class Manager')
root.resize(750 , 400)

#create class
name_label = QLabel('Name of Class:' , root)
name_label.setFont(QFont('' , 24))
name_label.move(100 , 30)
name_label.resize(280 , 50)

name_input = QLineEdit(root)
name_input.setFont(QFont('' , 18))
name_input.move(360 , 35)
name_input.resize(275 , 40)

seating_label = QLabel('Seating of Class:' , root)
seating_label.setFont(QFont('' , 24))
seating_label.move(100 , 120)
seating_label.resize(280 , 50)

seating_input = QLineEdit(root)
seating_input.setFont(QFont('' , 18))
seating_input.move(385 , 125)
seating_input.resize(275 , 40)

create_class_button = QPushButton('Create Class' , root)
create_class_button.setFont(QFont('' , 24))
create_class_button.move(260 , 240)
create_class_button.resize(220 , 80)

#functions
def create_class() :
    name = name_input.text()
    seating = int(seating_input.text())
    if name and seating :
        c.execute('insert into classes values("%s" , "%d")'%(name , seating))
        con.commit()

create_class_button.clicked.connect(create_class)

#window
root.show()
sys.exit(app.exec_())