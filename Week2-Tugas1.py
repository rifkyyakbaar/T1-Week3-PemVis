# NAMA : RIFKY AKBAR UTOMO PUTRA
# NIM : F1D02310149
# KELAS : D

import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox)
from PySide6.QtCore import Qt

class FormBiodata(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Form Biodata Mahasiswa")
        self.resize(380, 520)

        self.setStyleSheet("""
            QWidget {
                background-color: #F8F9F9; 
                font-family: 'Segoe UI', Arial, sans-serif; 
                font-size: 13px;
            }
            
            /* 1. Box Nama, NIM, Kelas: Garis hijau & Latar hijau pudar */
            QLineEdit {
                border: 1px solid #52BE80; 
                border-radius: 5px;       
                padding: 8px;             
                background-color: #E9F7EF; 
                color: #333333;
            }
            
            /* 2. Box Jenis Kelamin: Tetap putih/abu-abu sesuai gambar */
            QComboBox {
                border: 1px solid #bdc3c7;
                border-radius: 5px;       
                padding: 8px;             
                background-color: white;
                color: #333333;
            }
            
            /* Efek saat kotak sedang diklik/mengetik */
            QLineEdit:focus {
                border: 2px solid #27AE60; 
            }
            QComboBox:focus {
                border: 2px solid #3498db; 
            }
            
            /* Tombol Tampilkan */
            QPushButton {
                background-color: #3498db; 
                color: white; 
                padding: 8px 15px;         
                border-radius: 5px;        
                border: none;
                font-weight: bold;
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
        layout.setSpacing(12)

        label_nama = QLabel("Nama Lengkap:")
        self.entry_nama = QLineEdit()
        layout.addWidget(label_nama)
        layout.addWidget(self.entry_nama)

        label_nim = QLabel("NIM:")
        self.entry_nim = QLineEdit()
        self.entry_nim.setPlaceholderText("Masukkan NIM")
        layout.addWidget(label_nim)
        layout.addWidget(self.entry_nim)

        label_kelas = QLabel("Kelas:")
        self.entry_kelas = QLineEdit()
        self.entry_kelas.setPlaceholderText("Contoh: TI-2A")
        layout.addWidget(label_kelas)
        layout.addWidget(self.entry_kelas)

        label_jk = QLabel("Jenis Kelamin:")
        self.combo_jk = QComboBox()
        self.combo_jk.addItem("Pilih Jenis Kelamin")
        self.combo_jk.addItems(["Laki-laki", "Perempuan"])
        layout.addWidget(label_jk)
        layout.addWidget(self.combo_jk)

        layout_tombol = QHBoxLayout()

        self.btn_tampil = QPushButton("Tampilkan")
        self.btn_tampil.clicked.connect(self.tampilkan_data)
        layout_tombol.addWidget(self.btn_tampil)

        self.btn_reset = QPushButton("Reset")
        self.btn_reset.setStyleSheet("""
            QPushButton { background-color: #95a5a6; }
            QPushButton:hover { background-color: #7f8c8d; }
            QPushButton:pressed { background-color: #616a6b; }
        """)
        self.btn_reset.clicked.connect(self.reset_data)
        layout_tombol.addWidget(self.btn_reset)

        layout_tombol.addStretch() 
        layout.addLayout(layout_tombol)
        layout.addSpacing(10)

        self.label_hasil = QLabel("")
        self.label_hasil.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.label_hasil.setStyleSheet("""
            background-color: #D5F5E3; 
            border-left: 5px solid #27AE60; 
            border-top-right-radius: 5px;
            border-bottom-right-radius: 5px;
            padding: 15px;
            color: #0e6251;
        """)
        self.label_hasil.setMinimumHeight(150) 
        layout.addWidget(self.label_hasil)

        self.setLayout(layout)

    def tampilkan_data(self):
        nama = self.entry_nama.text()
        nim = self.entry_nim.text()
        kelas = self.entry_kelas.text()
        jk = self.combo_jk.currentText()

        if not nama or not nim or not kelas or jk == "Pilih Jenis Kelamin":
            QMessageBox.warning(self, "Peringatan", "Semua field harus diisi!")
            return

        teks = f"<b>DATA BIODATA</b><br><br>Nama: {nama}<br>NIM: {nim}<br>Kelas: {kelas}<br>Jenis Kelamin: {jk}"
        self.label_hasil.setText(teks)

    def reset_data(self):
        self.entry_nama.clear()
        self.entry_nim.clear()
        self.entry_kelas.clear()
        self.combo_jk.setCurrentIndex(0)
        self.label_hasil.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormBiodata()
    window.show()
    sys.exit(app.exec())