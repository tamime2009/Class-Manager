import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel , QLineEdit , QPushButton
from PyQt5.QtGui import QFont
import sqlite3

#database
con = sqlite3.connect('data.bd')
c = con.cursor()
#c.execute('create table accounts(name char(350) , password char(350) )')

#Window
app = QApplication(sys.argv)

root = QMainWindow()
root.setWindowTitle('Class Manager')
root.resize(600 , 400)

#Sign in
name_label = QLabel('Name:' , root)
name_label.setFont(QFont('' , 24))
name_label.move(100 , 40)

name_input = QLineEdit(root)
name_input.setFont(QFont('' , 18))
name_input.resize(275 , 40)
name_input.move(210 , 35)

password_label = QLabel('Password:' , root)
password_label.setFont(QFont('' , 24))
password_label.move(100 , 120)
password_label.resize(180 , 50)

password_input = QLineEdit(root)
password_input.setFont(QFont('' , 18))
password_input.resize(213 , 40)
password_input.move(280 , 125)

sign_in_button = QPushButton('Sign In' , root)
sign_in_button.setFont(QFont('' , 24))
sign_in_button.move(200 , 240)
sign_in_button.resize(180 , 80)

#functions
def sign_in_func() :
    name = name_input.text()
    password = password_input.text()
    if name and password :
        c.execute('insert into accounts values("%s" , "%s")'%(name , password))
        con.commit()
        c.execute('create table "%s"(seating char(350) , class char(350) , students char(350) , Notes char(350) , tests char(350) , exams char(350))'%(name))
        root.destroy()

sign_in_button.clicked.connect(sign_in_func)

#Window
root.show()