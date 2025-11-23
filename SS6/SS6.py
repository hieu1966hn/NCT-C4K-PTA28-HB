import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic

class Login(QMainWindow):
    def __init__(self) -> None:
        super().__init__() # gọi phương thức khởi tạo của lớp cha
        uic.loadUi('SS6/Login.ui', self) # tải giao diện từ file .ui vào đối tượng Login được tạo
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login() 
    window.show()
    
    sys.exit(app.exec())