import sys
from PyQt6.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)
msg_box = QMessageBox() # gán biến msg_box là cửa sổ thông báo (Khởi tạo đối tượng hộp thoại)
msg_box.setWindowTitle("Lỗi") # Thuộc tính hiển thị tên của cửa sổ
msg_box.setIcon(QMessageBox.Icon.Warning) # Cài đặt thuộc tính tạo icon hiển thị kèm
msg_box.setText("Vui lòng nhập email hoặc số điện thoại!")
msg_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
sys.exit(msg_box.exec()) # thực thi vòng lặp và hiển thị msg_box , tồn tại cho đến khi cửa sổ bị đóng.
