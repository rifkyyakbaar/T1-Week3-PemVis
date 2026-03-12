# NAMA : RIFKY AKBAR UTOMO PUTRA
# NIM : F1D02310149
# KELAS : D

import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QLineEdit, QPushButton, QCheckBox, QMessageBox)
from PySide6.QtCore import Qt

class FormLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Login")
        self.resize(350, 480)
        
        self.setStyleSheet("""
            QWidget {
                background-color: #FAFAFA; 
                font-family: 'Segoe UI', Arial, sans-serif; 
                font-size: 13px;
            }
            QLabel#header {
                background-color: #9B59B6; /* Warna ungu */
                color: white;
                font-weight: bold;
                font-size: 18px;
                padding: 15px;
                border-radius: 5px;
            }
        """)

        self.style_input_default = """
            border: 1px solid #bdc3c7; 
            border-radius: 5px; 
            padding: 8px; 
            background-color: white;
            font-size: 14px;
        """

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        label_header = QLabel("LOGIN")
        label_header.setObjectName("header") 
        label_header.setAlignment(Qt.AlignCenter)
        layout.addWidget(label_header)

        layout.addWidget(QLabel("Username:"))
        self.input_user = QLineEdit()
        self.input_user.setStyleSheet(self.style_input_default)
        layout.addWidget(self.input_user)

        layout.addWidget(QLabel("Password:"))
        self.input_pass = QLineEdit()
        self.input_pass.setStyleSheet(self.style_input_default)
        self.input_pass.setEchoMode(QLineEdit.Password) 
        layout.addWidget(self.input_pass)

        self.cek_password = QCheckBox("Tampilkan Password")
        self.cek_password.toggled.connect(self.toggle_password) 
        layout.addWidget(self.cek_password)

        layout_tombol = QHBoxLayout()

        self.btn_login = QPushButton("Login")
        self.btn_login.setStyleSheet("""
            QPushButton { background-color: #27AE60; color: white; padding: 10px; border-radius: 5px; font-weight: bold; border: none; }
            QPushButton:hover { background-color: #2ECC71; }
        """)
        self.btn_login.clicked.connect(self.proses_login)
        layout_tombol.addWidget(self.btn_login)

        self.btn_reset = QPushButton("Reset")
        self.btn_reset.setStyleSheet("""
            QPushButton { background-color: #95a5a6; color: white; padding: 10px; border-radius: 5px; font-weight: bold; border: none; }
            QPushButton:hover { background-color: #7f8c8d; }
        """)
        self.btn_reset.clicked.connect(self.reset_form) 
        layout_tombol.addWidget(self.btn_reset)

        layout.addLayout(layout_tombol)

        self.label_hasil = QLabel("")
        self.label_hasil.setWordWrap(True) 
        self.label_hasil.hide() 
        layout.addWidget(self.label_hasil)
        
        layout.addStretch()
        self.setLayout(layout)

    def toggle_password(self, checked):
        if checked:
            self.input_pass.setEchoMode(QLineEdit.Normal)
        else:
            self.input_pass.setEchoMode(QLineEdit.Password)

    def proses_login(self):
        username = self.input_user.text()
        password = self.input_pass.text()

        self.label_hasil.show()

        if username == "admin" and password == "12345":

            style_sukses = """
                border: 1px solid #27AE60; 
                background-color: #E9F7EF; 
                padding: 8px; 
                border-radius: 5px;
                font-size: 14px;
            """
            self.input_user.setStyleSheet(style_sukses)
            self.input_pass.setStyleSheet(style_sukses)
            
            self.label_hasil.setText("Login berhasil! Selamat datang, admin.")
            self.label_hasil.setStyleSheet("""
                background-color: #D5F5E3; border-left: 5px solid #27AE60; 
                border-top-right-radius: 5px; border-bottom-right-radius: 5px; 
                padding: 15px; color: #1E8449;
            """)
        else:

            style_gagal = """
                border: 1px solid #E74C3C; 
                background-color: white; 
                padding: 8px; 
                border-radius: 5px;
                font-size: 14px;
            """
            self.input_user.setStyleSheet(style_gagal)
            self.input_pass.setStyleSheet(style_gagal)
            
            self.label_hasil.setText("Login gagal! Username atau password salah.")
            self.label_hasil.setStyleSheet("""
                background-color: #FADBD8; border-left: 5px solid #E74C3C; 
                border-top-right-radius: 5px; border-bottom-right-radius: 5px; 
                padding: 15px; color: #922B21;
            """)

    def reset_form(self):
        self.input_user.clear()
        self.input_pass.clear()
        
        self.input_user.setStyleSheet(self.style_input_default)
        self.input_pass.setStyleSheet(self.style_input_default)
        
        self.cek_password.setChecked(False)
        self.label_hasil.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormLogin()
    window.show()
    sys.exit(app.exec())