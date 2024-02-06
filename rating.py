import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import sqlite3

class home_window(QtWidgets.QDialog):
    def __init__(self):
        super(home_window, self).__init__()
        uic.loadUi('Rating.ui', self)

        # self.pushButton.clicked.connect(self.change_button_color)
        # self.pushButton_2.clicked.connect(self.change_button_color)
        # self.pushButton_5.clicked.connect(self.change_button_color)
        self.pushButton_3.clicked.connect(self.save_information)
        # self.pushButton_6.clicked.connect(self.change_button_color)
        # self.pushButton_4.clicked.connect(self.change_button_color)

    # def change_button_color(self):
    #     button = self.sender()
    #     button.setStyleSheet("background-color: yellow;")

    def save_information(self):
        button = self.sender()
        button.setStyleSheet("background-color: yellow;")

        # Create a connection to the database
        self.connection = sqlite3.connect('ratings.db')
        self.cursor = self.connection.cursor()

        # Create the table if it doesn't exist
        self.create_table()

        # Get the information from the UI
        business_name = self.lineEdit_3.text()
        description = self.lineEdit_2.text()
        rate_us = self.comboBox.currentIndex()
        like_dislike = "LIKE" if self.radioButton.isChecked() else "DISLIKE"
        comment = self.lineEdit.text()

        # Insert the information into the database
        query = '''
        INSERT INTO ratings (BUSINESS_NAME, DESCRIPTION, RATE_US, LIKE_DISLIKE, COMMENT)
        VALUES (?, ?, ?, ?, ?)
        '''
        self.cursor.execute(query, (business_name, description, rate_us, like_dislike, comment))
        self.connection.commit()

        # Show a message box indicating successful addition and rating
        message = f"Business '{business_name}' successfully added with rating: {rate_us}"
        QMessageBox.information(self, "Success", message)

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS ratings (
            BUSINESS_NAME TEXT,
            DESCRIPTION TEXT,
            RATE_US INTEGER,
            LIKE_DISLIKE TEXT,
            COMMENT TEXT
        )
        '''
        self.cursor.execute(query)
        self.connection.commit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = home_window()
    window.show()
    sys.exit(app.exec_())