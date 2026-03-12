# NAMA : RIFKY AKBAR UTOMO PUTRA
# NIM : F1D02310149
# KELAS : D

import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QLineEdit, QPushButton, QMessageBox)
from PySide6.QtCore import Qt

class KonversiSuhu(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Konversi Suhu")
        self.resize(380, 400)
        
        self.setStyleSheet("""
            QWidget {
                background-color: #FAFAFA; 
                font-family: 'Segoe UI', Arial, sans-serif; 
                font-size: 13px;
            }
            
            QLabel#header {
                background-color: #3498db;
                color: white;
                font-weight: bold;
                font-size: 16px;
                padding: 15px;
                border-radius: 5px;
            }
            
            QLineEdit {
                border: 1px solid #52BE80; 
                border-radius: 5px;       
                padding: 8px;             
                background-color: #E9F7EF; 
                color: #333333;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #27AE60; 
            }
            
            QPushButton {
                background-color: #3498db; 
                color: white; 
                padding: 10px;         
                border-radius: 5px;        
                border: none;
            }
            QPushButton:hover {
                background-color: #2980b9; 
            }
            QPushButton:pressed {
                background-color: #1f618d;
            }
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        label_header = QLabel("KONVERSI SUHU")
        label_header.setObjectName("header") 
        label_header.setAlignment(Qt.AlignCenter)
        layout.addWidget(label_header)

        layout.addWidget(QLabel("Masukkan Suhu (Celsius):"))
        self.input_suhu = QLineEdit()
        layout.addWidget(self.input_suhu)

        layout_tombol = QHBoxLayout()

        btn_f = QPushButton("Fahrenheit")
        btn_f.clicked.connect(self.hitung_fahrenheit)
        layout_tombol.addWidget(btn_f)

        btn_k = QPushButton("Kelvin")
        btn_k.clicked.connect(self.hitung_kelvin)
        layout_tombol.addWidget(btn_k)

        btn_r = QPushButton("Reamur")
        btn_r.clicked.connect(self.hitung_reamur)
        layout_tombol.addWidget(btn_r)

        layout.addLayout(layout_tombol)

        self.label_hasil = QLabel("<b>Hasil Konversi:</b><br><br>")
        self.label_hasil.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.label_hasil.setStyleSheet("""
            background-color: #D6EAF8; 
            border-left: 5px solid #1A5276; 
            border-top-right-radius: 5px;
            border-bottom-right-radius: 5px;
            padding: 15px;
            color: #1A5276;
        """)
        self.label_hasil.setMinimumHeight(100) 
        layout.addWidget(self.label_hasil)
        layout.addStretch()

        self.setLayout(layout)

    def ambil_suhu_valid(self):
        teks = self.input_suhu.text()
        
        if not teks:
            QMessageBox.warning(self, "Peringatan", "Masukkan suhu terlebih dahulu!")
            return None
            
        try:
            suhu = float(teks)
            return suhu
        except ValueError:
            QMessageBox.critical(self, "Error", "Input tidak valid! Harus berupa angka.")
            self.input_suhu.clear()
            return None

    def hitung_fahrenheit(self):
        celsius = self.ambil_suhu_valid()
        if celsius is not None:
            hasil = (celsius * 9/5) + 32
            teks_asli = self.input_suhu.text() 
            teks = f"<b>Hasil Konversi:</b><br><br>{teks_asli} Celsius = {hasil:.2f} Fahrenheit"
            self.label_hasil.setText(teks)

    def hitung_kelvin(self):
        celsius = self.ambil_suhu_valid()
        if celsius is not None:
            hasil = celsius + 273.15
            teks_asli = self.input_suhu.text()
            teks = f"<b>Hasil Konversi:</b><br><br>{teks_asli} Celsius = {hasil:.2f} Kelvin"
            self.label_hasil.setText(teks)

    def hitung_reamur(self):
        celsius = self.ambil_suhu_valid()
        if celsius is not None:
            hasil = celsius * 4/5
            teks_asli = self.input_suhu.text() 
            teks = f"<b>Hasil Konversi:</b><br><br>{teks_asli} Celsius = {hasil:.2f} Reamur"
            self.label_hasil.setText(teks)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KonversiSuhu()
    window.show()
    sys.exit(app.exec())