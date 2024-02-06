import sys
import sqlite3
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets, uic


class open_Reply(QtWidgets.QMainWindow):
    def __init__(self):
        super(open_Reply, self).__init__()
        uic.loadUi('reply.ui', self)

        # Connect to the SQLite database
        self.connection = sqlite3.connect('reply.db')
        self.cursor = self.connection.cursor()

        self.pushButton_12.clicked.connect(self.save_infos)
       
    def create_table(self):
        # Create the table if it doesn't exist
        query = '''
        CREATE TABLE IF NOT EXISTS ratings (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            BUSINESS_NAME TEXT,
            COMMENT TEXT,
            REPLY TEXT
        )
        '''
        self.cursor.execute(query)
        self.connection.commit()

    def save_infos(self):
        button = self.sender()
        button.setStyleSheet("background-color: orange;")

        # Create a connection to the database
        self.connection = sqlite3.connect('reply.db')
        self.cursor = self.connection.cursor()

        # Create the table if it doesn't exist
        self.create_table()

        # Get the information from the UI
        business_name = self.lineEdit_9.text()
        comment = self.lineEdit_7.text()
        reply = self.lineEdit_8.text()

        # Insert the information into the database
        query = '''
        INSERT INTO ratings (BUSINESS_NAME, COMMENT, REPLY)
        VALUES (?, ?, ?)
        '''
        self.cursor.execute(query, (business_name, comment, reply))
        self.connection.commit()

        # Retrieve the business name and comment from the database
        query = '''
        SELECT BUSINESS_NAME, COMMENT
        FROM ratings
        WHERE BUSINESS_NAME = ?
        '''
        self.cursor.execute(query, (business_name,))
        result = self.cursor.fetchone()

        # Display the retrieved information in the UI
        if result:
            self.lineEdit_9.setText(result[0])  # Set the text of lineEdit_9 with the retrieved business name
            self.lineEdit_7.setText(result[1])  # Set the text of lineEdit_7 with the retrieved comment
        else:
            self.lineEdit_9.setText("")  # Clear the text of lineEdit_9 if no result found
            self.lineEdit_7.setText("")  # Clear the text of lineEdit_7 if no result found

        # Show a message box indicating successful addition and rating
        message = "Replied"
        QMessageBox.information(self, "Successfully", message)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = open_Reply()
    window.show()
    sys.exit(app.exec())