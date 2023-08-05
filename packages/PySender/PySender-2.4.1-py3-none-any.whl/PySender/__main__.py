import json
import os
import sqlite3
import sys
import webbrowser

import requests
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog

from PySender.dialogs import open_about_dialog
from PySender.errors import *
from PySender.request import Request
from PySender.ui.ui import Ui_MainWindow

db_path = "requests.db"


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_send.clicked.connect(self.send_request)
        self.button_add.clicked.connect(self.add_header)
        self.delete_header_button.clicked.connect(self.remove_header)
        self.clear_button.clicked.connect(self.clear_headers)
        self.actionAbout.triggered.connect(open_about_dialog)
        self.actionSupport.triggered.connect(lambda: webbrowser.open('https://t.me/fast_geek'))
        self.actionExit.triggered.connect(lambda: exit(0))
        self.actionSave.triggered.connect(self.save_file)
        self.actionSave_2.triggered.connect(self.save_request)
        self.actionRevert.triggered.connect(self.revert_request)
        self.lineEdit_URL.installEventFilter(self)
        self.tabWidget.setCurrentIndex(0)

    def send_request(self):
        params = {}
        for i in range(self.table_headers.rowCount()):
            params[self.table_headers.item(i, 0).text()] = self.table_headers.item(i, 1).text()
        try:
            user, passwd = self.field_username.text(), self.field_password.text() if \
                self.field_username.text() != "" or self.field_password.text() != "" \
                else None
            url = self.lineEdit_URL.text()
            method = self.method_selector.currentText().lower()
            res, status_code = Request(url, method, user, passwd, params).send()
            self.field_response.setText(res)
            self.field_status_code.setText(str(status_code))
            self.tabWidget.setCurrentIndex(2)
        except requests.exceptions.MissingSchema:
            valid_url(self)
        except json.decoder.JSONDecodeError:
            json_error(self)

    def add_header(self):
        name = self.field_name.text().strip()
        value = self.field_value.text().strip()
        if "" in (name, value):
            QMessageBox.warning(self, "Error", "Please enter a valid header", QMessageBox.Ok)
        self.table_headers.setRowCount(self.table_headers.rowCount() + 1)
        self.table_headers.setItem(self.table_headers.rowCount() - 1, 0, QTableWidgetItem(name))
        self.table_headers.setItem(self.table_headers.rowCount() - 1, 1, QTableWidgetItem(value))
        self.field_name.setText("")
        self.field_value.setText("")

    def remove_header(self):
        if self.table_headers.currentRow() != -1:
            self.table_headers.removeRow(self.table_headers.currentRow())
        else:
            QMessageBox.warning(self, "Error", "Select the item you want to delete", QMessageBox.Ok)

    def clear_headers(self):
        self.table_headers.clearContents()
        self.table_headers.setRowCount(0)

    def eventFilter(self, obj, event):
        if (
                event.type() == QtCore.QEvent.KeyPress
                and obj is self.lineEdit_URL
                and event.key() == QtCore.Qt.Key_Return
                and self.lineEdit_URL.hasFocus()
        ):
            self.send_request()
        return super().eventFilter(obj, event)

    def save_file(self):
        if self.field_response.toPlainText() == "":
            empty_request(self)
        file_name = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")
        if file_name[0] != "":
            with open(file_name[0], "w") as f:
                f.write(f"TYPE: {self.method_selector.currentText()} \n")
                f.write(f"URL: {self.lineEdit_URL.text()} \n")
                f.write(f"STATUS CODE: {self.field_status_code.text()} \n")
                f.write(f"RESPONSE: {self.field_response.toPlainText()}")

    def save_request(self):
        if os.path.isfile(db_path):
            con = sqlite3.connect(db_path)
            cur = con.cursor()
            rtype = self.method_selector.currentIndex() + 1
            url = self.lineEdit_URL.text()
            if cur.execute("""SELECT Count(*) FROM requests""").fetchone()[0] == 0:
                cur.execute(f"""INSERT INTO requests (type, url) VALUES('{rtype}', '{url}')""")
            else:
                cur.execute(f"""UPDATE requests SET type = '{rtype}', url = '{url}' WHERE id = 1""")
            con.commit()
            con.close()
        else:
            no_db(self)

    def revert_request(self):
        if os.path.isfile(db_path):
            con = sqlite3.connect(db_path)
            cur = con.cursor()
            try:
                _, rtype, url = cur.execute("""SELECT * FROM requests""").fetchall()[0]
                self.method_selector.setCurrentIndex(rtype - 1)
                self.lineEdit_URL.setText(url)
            except IndexError:
                no_recent_request(self)
            con.close()
        else:
            no_db(self)


def main():
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
