# import sys
# import sqlite3
# from login import log_window
# from PyQt5 import QtWidgets, uic


# class SignupWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(SignupWindow, self).__init__()
#         uic.loadUi('Signup.ui', self)

#         # Connect to the SQLite database
#         self.connection = sqlite3.connect('sign.db')
#         self.cursor = self.connection.cursor()

#         # Create the 'users' table if it doesn't exist
#         self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#                                 Username TEXT ,
#                                 Email TEXT,
#                                 Security_Question TEXT,
#                                 Answer TEXT,
#                                 PassWord TEXT,
#                                 ID TEXT PRIMARY KEY
#                                 )''')

#         # Connect the "Sign Up" button to a function
#         self.pushButton_2.clicked.connect(self.signup)
#         self.pushButton.clicked.connect(self. back_log)

#     def back_log(self):
#         # self.close()  # Close the current dialog
#         self.hide()
#         self.log_window = log_window()
#         self.log_window.show()
        

#     def signup(self):
#         # Get the entered username, password, and email
#         Username  = self.lineEdit.text()
#         Email= self.lineEdit_2.text()
#         Security_Question= self.lineEdit_3.text()
#         Answer=self.lineEdit_4.text()
#         PassWord=self.lineEdit_5.text()
#         ID=self.lineEdit_6.text()

#         # Insert the user data into the 'users' table
#         self.cursor.execute("INSERT INTO users VALUES (?, ?, ?,?,?,?)", (Username ,Email,Security_Question,Answer,PassWord,ID))
#         self.connection.commit()

#         # Display a message after successful signup
#         msg_box = QtWidgets.QMessageBox()
#         msg_box.setStyleSheet("QLabel{ color: white; }")
#         msg_box.setText("Signup successful!")
#         msg_box.setWindowTitle("Signup")
#         msg_box.exec_()

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     window = SignupWindow()
#     window.show()
#     sys.exit(app.exec())