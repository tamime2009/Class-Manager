import sys
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

#login
name_label = QLabel('Name:' , root)
name_label.setFont(QFont('' , 24))
name_label.move(100 , 30)
name_label.resize(180 , 50)

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

login_button = QPushButton('Login' , root)
login_button.setFont(QFont('' , 24))
login_button.move(100 , 240)
login_button.resize(180 , 80)

#signin
sign_in_button = QPushButton('Sign In' , root)
sign_in_button.setFont(QFont('' , 24))
sign_in_button.move(310 , 240)
sign_in_button.resize(180 , 80)

#functions
def login() :
    name = name_input.text()
    password = password_input.text()
    names = []
    passwords= []
    c.execute('select * from accounts')
    data = c.fetchall()
    for u in data :
        names.append(u[0])
        passwords.append(u[1])
    if names and passwords :
        if name in names and password in passwords :
            pass

def sign_in() :
    import sign_in_window

login_button.clicked.connect(login)
sign_in_button.clicked.connect(sign_in)

#Window
root.show()
sys.exit(app.exec_())