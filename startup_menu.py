import sys
import link
from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel , QLineEdit , QPushButton
from PyQt5.QtGui import QFont
import sqlite3
con = sqlite3.connect('data.bd')
c = con.cursor()

#Window
app = QApplication(sys.argv)

root = QMainWindow()
root.setWindowTitle('Class Manager')
root.resize(600 , 400)

#Create Class
create_button = QPushButton('Create Class' , root)
create_button.setFont(QFont('' , 24))
create_button.move(195 , 250)
create_button.resize(240 , 80)

#Search Class
class_label = QLabel('Class:' , root)
class_label.setFont(QFont('' , 24))
class_label.move(100 , 50)
class_label.resize(180 , 50)

class_input = QLineEdit(root)
class_input.setFont(QFont('' , 18))
class_input.resize(275 , 40)
class_input.move(220 , 55)

class_button = QPushButton('Join Class' , root)
class_button.setFont(QFont('' , 24))
class_button.move(195 , 150)
class_button.resize(240 , 80)

#functions
def join_class() :
    print(link.name)
    pass

class_button.clicked.connect(join_class)

#Window
root.show()
#sys.exit(app.exec_())