import PyQt6


from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
import sys
app = QApplication(sys.argv)
window = QWidget()
button = QPushButton("Click me", window)
button.setGeometry(100, 100, 100, 30)
window.show()
app.exec() # Khi nào đóng cửa sổ app => mới chạy code phía dưới.

