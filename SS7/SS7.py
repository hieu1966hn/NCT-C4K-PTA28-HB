from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel

class MyApp(QWidget):
    def __init__(self, ):
        super().__init__()
        
        self.label = QLabel("Button not clicked", self)
        btn = QPushButton("click me", self)
        btn.clicked.connect(self.onButtonClick) # Kết nối signal 'clicked' với slot 'onButtonClick'
        
        ## trang chí chút
        self.label.move(50,50)
        btn.move(50, 100)
        
        self.setGeometry(300, 300, 200, 150)
        self.setWindowTitle("Signal-Slot Example")
        
        
        self.show()
    
    # Khởi tạo phương thức onButtonClick
    def onButtonClick(self):
        self.label.setText("Button clicked")
        
if __name__ == "__main__":
    app = QApplication([])
    ex = MyApp()
    app.exec()



