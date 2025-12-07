from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget

from PyQt6 import uic
import sys

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("SS7/GUI/Login.ui", self)

        # self.btnRegister.clicked.connect(self.show_register)
        self.btnLogin.clicked.connect(self.check_login) # 1 signal
    # self  objectName #tên sự kiện.       gọi check_login
        self.msg_box = QMessageBox()
        
    def check_login(self): # Slot
        email = self.txtEmail.text() # lấy ra thông tin người dùng nhập tại đây
        password = self.txtPassword.text() # lấy ra mật khẩu
        if email == "admin@example.com" and password == "admin":
            main.show()
            self.close()
        else:
            self.msg_box.setText("Vui lòng kiểm tra lại thông tin đăng nhập")
            self.msg_box.setIcon(QMessageBox.Icon.Warning)
            self.msg_box.exec()
    
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("SS7/GUI/main.ui")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    main = Main()
    app.exec()
        
        