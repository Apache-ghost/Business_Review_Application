# import sys
# import sqlite3
# from login import log_window
# from PyQt5 import QtWidgets, uic


# class Forgot_Window(QtWidgets.QDialog):
#     def __init__(self):
#         super(Forgot_Window, self).__init__()
#         uic.loadUi('reset Password.ui', self)

#         # Connect to the SQLite database
#         self.connection = sqlite3.connect('sign.db')
#         self.cursor = self.connection.cursor()

#         # Connect the "Retrieve" button to a function
#         self.pushButton_2.clicked.connect(self.retrieve_data)
#         self.pushButton.clicked.connect(self. back_log)
#     def back_log(self):
#         # self.close()  # Close the current dialog
#         self.log_window = log_window()
#         self.log_window.show()
#         self.hide()

#     def retrieve_data(self):
#         # Get the entered ID, security question, and answer from the text fields
#         ID = self.lineEdit_3.text()
#         security_Question = self.lineEdit_5.text()
#         Answer = self.lineEdit_4.text()

#         # Execute a SELECT query to retrieve the password, security question, and answer for the given ID
#         self.cursor.execute("SELECT password, security_Question, Answer FROM users WHERE ID = ?", (ID,))
#         result = self.cursor.fetchone()

#         if result:
#             password, stored_question, stored_answer = result

#             if security_Question == stored_question and Answer == stored_answer:
#                 # Display the retrieved password in lineEdit_10
#                 self.lineEdit.setText(password)
#             else:
#                 QtWidgets.QMessageBox.warning(self, "Authentication Failed", "Incorrect security question or answer")
#         else:
#             QtWidgets.QMessageBox.warning(self, "Password", f"No password found for {ID}")


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     window = Forgot_Window()
#     window.show()
#     sys.exit(app.exec())