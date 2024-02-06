import sys
import sqlite3
from PyQt5 import QtWidgets, uic
# from signup import SignupWindow
# from forgot import Forgot_Window
from main import  open_main



class log_window(QtWidgets.QDialog):
    def __init__(self):
        super(log_window, self).__init__()
        uic.loadUi('log.ui', self)
        # self.pushButton_2.clicked.connect(self.open_Signup)
        self.pushButton.clicked.connect(self.open_rating)
        # self.commandLinkButton.clicked.connect(self.open_Forgot)


    def open_rating(self):
            # Get the entered username and password from the text fields
            Username = self.lineEdit.text()
            PassWord = self.lineEdit_2.text()

            # Connect to the SQLite database
            connection = sqlite3.connect('sign.db')
            cursor = connection.cursor()

            # Execute a SELECT query to check if the username and password are correct
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (Username, PassWord))
            result = cursor.fetchone()

            if result:
                # Open the next page
                self.open_main =open_main()
                self.open_main.show()
                self.hide()
            else:
                # Display an error message
                QtWidgets.QMessageBox.warning(self, "Authentication Failed", "Incorrect username or password")

            # Close the database connection
            connection.close()

    # def open_Signup(self):
    #     # self.close()  # Close the current dialog
    #     self.signup_window = SignupWindow()
    #     self.signup_window.show()
    #     self.hide()

    # def open_Forgot(self):
    #     # self.close()  # Close the current dialog
    #     self.Forgot_Window = Forgot_Window()
    #     self.Forgot_Window.show()
    #     self.hide()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = log_window()
    window.show()
    sys.exit(app.exec_())