import sys
from PyQt5.QtCore import Qt, QPropertyAnimation, QTimer, QUrl
from PyQt5.QtGui import QIcon, QPixmap, QImage, QDesktopServices
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QGraphicsDropShadowEffect,
    QSizeGrip,
    QTableWidgetItem,
    QProgressBar,
    QProgressDialog,
    QPushButton,
    QMessageBox
)
from PyQt5 import QtGui, QtWidgets
import sqlite3

from Test import Ui_MainWindow


class MainWindow(QMainWindow):
    def open_instagram_signup(self):
        # Open the default web browser with the Instagram signup page
        url = QUrl("https://www.instagram.com/accounts/emailsignup/")
        QDesktopServices.openUrl(url)

    def open_facebook_signup(self):
        # Open the default web browser with the Facebook signup page
        url = QUrl("https://www.facebook.com/r.php")
        QDesktopServices.openUrl(url)

    def open_twitter_signup(self):
        # Open the default web browser with the Twitter signup page
        url = QUrl("https://twitter.com/i/flow/signup")
        QDesktopServices.openUrl(url)

    def open_linkedin_signup(self):
        # Open the default web browser with the LinkedIn signup page
        url = QUrl("https://www.linkedin.com/signup/")
        QDesktopServices.openUrl(url)

    def connect_social_media_buttons(self):
        # Connect each social media button to its respective function
        self.ui.instagram.clicked.connect(self.open_instagram_signup)
        self.ui.facebook.clicked.connect(self.open_facebook_signup)
        self.ui.twitter.clicked.connect(self.open_twitter_signup)
        self.ui.linkedIn.clicked.connect(self.open_linkedin_signup)

    def __init__(self):
        super().__init__()

        self.profile = QPushButton("Profile")
        self.clickPosition = None
        self.animation = None  # Animate minimumWidth
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        self.setWindowIcon(QIcon(":/newPrefix/images/good-review (1).png"))
        self.setWindowTitle("MODERN UI")
        QSizeGrip(self.ui.size_grip)
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        self.ui.exit_button.clicked.connect(lambda: self.close())
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())
        self.loadProducts()
        self.connect_social_media_buttons()
        self.update_table()  # Call update_table method directly during initialization
        self.ui.pushButton_6.clicked.connect(self.search_and_highlight)  # Connect search button to search method
        self.ui.profile.clicked.connect(self.open_file_dialog)

    def open_file_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setOptions(options)
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp *.gif)")

        # Get the selected file path
        file_path, _ = file_dialog.getOpenFileName(self, "Select Image", "",
                                                       "Images (*.png *.jpg *.jpeg *.bmp *.gif)")

        if file_path:
            # Update the button's icon with the selected image file
            icon = QtGui.QIcon(file_path)
            self.ui.profile.setIcon(icon)
    def loadProducts(self):
        self.ui.tableWidget.setGeometry(20, 20, 561, 481)
        self.ui.tableWidget.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.ui.tableWidget.setObjectName("tableWidget")
        self.ui.tableWidget.setColumnCount(6)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['Profile Image', 'Business Name', 'About', 'Address', 'Rating', 'Number of Reviews'])

        # Connect the load button click event to show_progress_bar method
        self.ui.load.clicked.connect(self.show_progress_bar)

        self.show()

    def add_row_from_database(self, row_data):
        row_position = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_position)

        # Profile Image
        # Assuming the image data is stored in the first column of the database
        image_data = row_data[0]
        profile_image_item = QTableWidgetItem()
        profile_image_item.setIcon(QIcon(QPixmap.fromImage(QImage.fromData(image_data))))
        self.ui.tableWidget.setItem(row_position, 0, profile_image_item)

        # Other columns with data from the database
        for col_index, col_value in enumerate(row_data[1:], start=1):
            item = QTableWidgetItem(str(col_value))
            # Set item flags to make cells non-editable
            item.setFlags(item.flags() ^ Qt.ItemIsEditable)
            self.ui.tableWidget.setItem(row_position, col_index, item)

    def add_ten_rows(self):
        for _ in range(10):
            self.add_row()

    def add_row(self):
        row_position = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_position)

        # Profile Image
        profile_image_item = QTableWidgetItem()
        profile_image_item.setIcon(QIcon(":/newPrefix/images/add-user.png"))
        self.ui.tableWidget.setItem(row_position, 0, profile_image_item)

        # Other columns with random data
        business_name_item = QTableWidgetItem("Business X")  # Replace with actual data from the database
        about_item = QTableWidgetItem("About X")  # Replace with actual data from the database
        address_item = QTableWidgetItem("Address X")  # Replace with actual data from the database
        rating_item = QTableWidgetItem(str(4.5))  # Replace with actual data from the database
        num_reviews_item = QTableWidgetItem(str(50))  # Replace with actual data from the database

        # Set item flags to make cells non-editable
        for item in [business_name_item, about_item, address_item, rating_item, num_reviews_item]:
            item.setFlags(item.flags() ^ Qt.ItemIsEditable)

        self.ui.tableWidget.setItem(row_position, 1, business_name_item)
        self.ui.tableWidget.setItem(row_position, 2, about_item)
        self.ui.tableWidget.setItem(row_position, 3, address_item)
        self.ui.tableWidget.setItem(row_position, 4, rating_item)
        self.ui.tableWidget.setItem(row_position, 5, num_reviews_item)

    def moveWindow(self, e):
        if not self.isMaximized():
            if e.buttons() == Qt.LeftButton:
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.restore_window_button.setIcon(QIcon(u":/newPrefix/images/expand.png"))
        else:
            self.showMaximized()
            self.ui.restore_window_button.setIcon(QIcon(u":/newPrefix/images/minimize.png"))

    def resizeEvent(self, event):
        # Handle window resize event
        super().resizeEvent(event)

        # Check if the window is maximized or restored
        if self.isMaximized():
            self.ui.tableWidget.setGeometry(30, 30, 1685, 900)
        else:
            self.ui.tableWidget.setGeometry(20, 20, 561, 481)

    def slideLeftMenu(self):
        width = self.ui.slide_menu_container.width()
        if width == 0:
            newWidth = 200
            self.ui.open_close_side_bar_btn.setIcon(QIcon(u":/newPrefix/images/menu (1).png"))
        else:
            newWidth = 0
            self.ui.open_close_side_bar_btn.setIcon(QIcon(u":/newPrefix/images/left-arrow.png"))

        self.animation = QPropertyAnimation(self.ui.slide_menu_container, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(Qt.EasingCurve.InOutQuart)
        self.animation.start()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def show_progress_bar(self):
        progress_bar = QProgressBar()
        progress_bar.setRange(0, 0)  # Setting the range to (0, 0) makes it an indeterminate progress bar
        progress_bar.setStyleSheet("QProgressBar {background-color: green; border: 2px solid grey;}")

        progress_dialog = QProgressDialog("Loading...", "", 0, 0, self)
        progress_dialog.setWindowFlags(
            Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        progress_dialog.setCancelButton(None)  # Disabling cancel button
        progress_dialog.setBar(progress_bar)
        progress_dialog.show()

        # Simulate loading process
        QTimer.singleShot(3000, progress_dialog.accept)  # Adjust the duration as needed

        # Connect the finished signal to update_table method
        progress_dialog.finished.connect(self.update_table)

    def update_table(self):
        # Fetch all rows from the "Business" table
        connection = sqlite3.connect("Database.db")  # Update with your actual database name
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Business")
        rows = cursor.fetchall()
        connection.close()

        # Clear existing rows
        self.ui.tableWidget.setRowCount(0)

        # Populate the tableWidget with the fetched data
        for row_data in rows:
            self.add_row_from_database(row_data)

    def search_and_highlight(self):
        search_text = self.ui.lineEdit.text().strip()
        if search_text:
            # Show yellow progress bar while searching
            progress_bar = QProgressBar()
            progress_bar.setRange(0, 0)
            progress_bar.setStyleSheet("QProgressBar {background-color: yellow; border: 2px solid grey;}")

            progress_dialog = QProgressDialog("Searching...", "", 0, 0, self)
            progress_dialog.setWindowFlags(
                    Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
            progress_dialog.setCancelButton(None)
            progress_dialog.setBar(progress_bar)
            progress_dialog.show()

            # Simulate search process
            QTimer.singleShot(3000, lambda: self.finish_search(progress_dialog, search_text))

        else:
            QMessageBox.warning(self, "Warning", "Please enter search text.", QMessageBox.Ok)

    def finish_search(self, progress_dialog, search_text):
        # Highlight cells with matching text
        self.highlight_cells(search_text)

        # Close progress dialog
        progress_dialog.accept()

        # Connect the finished signal to the method handling message box closing
        progress_dialog.finished.connect(self.handle_message_box)

    def handle_message_box(self):
        # Create a message box
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Warning")
        msg_box.setText("No results found.")
        msg_box.setStandardButtons(QMessageBox.Ok)

        # Close the message box at will
        result = msg_box.exec_()
        if result == QMessageBox.Ok:
            msg_box.close()

    def highlight_cells(self, search_text):
        for row in range(self.ui.tableWidget.rowCount()):
            for col in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(row, col)
                if item and search_text.lower() in item.text().lower():
                    item.setBackground(QtGui.QColor(255, 255, 0))  # Yellow background
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())