# ## Khởi tạo bản thiết kế/ kiểu dữ liệu "PhuongTien"
# class PhuongTien:
#     def __init__(self, loai_xe, hang_xe, mau_sac, so_cho_ngoi, so_banh_xe, gia_tien):
#         self.loai_xe = loai_xe
#         self.hang_xe = hang_xe
#         self.mau_sac = mau_sac
#         self.so_cho_ngoi = so_cho_ngoi
#         self.so_banh_xe = so_banh_xe
#         self.gia_tien = gia_tien
        
#     def in_thong_tin(self):
#         print(self.loai_xe)
#         print(self.hang_xe)
#         print(self.mau_sac)
#         print(self.so_cho_ngoi)
#         print(self.so_banh_xe)
#         print(self.gia_tien)
        
# # Khởi tọa đối tượng thuộc lớp PhuongTien 
# phuong_tien_1 = PhuongTien('Trực thăng', 'VN', 'đỏ - đen', 4, 0, 9000000000)

# # Viết phương thức in ra một số thông tin của phương tiện 
# phuong_tien_1.in_thong_tin()



#### Kế thừa trong OOP
class HocSinhMindX:
    def say_hello(self):
        print("hello")
        
    def introduce(self):
        print("Hello, I am a student at mindX School")
    
#### C1: Khởi tạo class mới và viết y hệt (Không sử dụng cách này)
# class HocSinhHocApp:
#     def say_hello():
#         print("hello")
        
#     def introduce():
#         print("Hello, I am a student at mindX School")
    
#     def age():
#         print("I am 14 years old")

#### C2: Sử dụng tính chất Kế thừa trong OOP để không phải viết lại các phương thức đã có.
# class HocSinhHocApp(HocSinhMindX):
#     def age(self):
#         print("I am 14 years old")
    
# # TueMinh = HocSinhHocApp()
# # TueMinh.say_hello()
# # TueMinh.introduce()
# # TueMinh.age()




##### Chữa bài tập thực hành

class Xe:
    def __init__(self, hang, mau_sac, gia_tien):
        self.hang = hang
        self.mau_sac = mau_sac
        self.gia_tien = gia_tien
        
    def khoi_dong(self):
        print(f'Xe {self.hang} đang hoạt động')
        
class XeHoi(Xe): ## Mặc định sẽ được kế thừa phương thức
    ## Kế thừa thuộc tính từ lớp cha
    def __init__(self, hang, mau_sac, gia_tien, so_cho):
        super().__init__(hang, mau_sac, gia_tien) # kế thừa toàn bộ các thuộc tính của class cha
        self.so_cho = so_cho
        
    def chay_bang_bon_banh(self):
        print(f'Xe {self.hang} đang chạy về phía trước bằng động cơ')
        
class XeDap(Xe): ## Mặc định sẽ được kế thừa phương thức
    ## Kế thừa thuộc tính từ lớp cha
    def __init__(self, hang, mau_sac, gia_tien, so_cho):
        super().__init__(hang, mau_sac, gia_tien) # kế thừa toàn bộ các thuộc tính của class cha
        self.so_cho = so_cho
        
    def dap_bang_hai_chan(self):
        print(f'Xe {self.hang} đang được đạp về phía trước')
        
Xehoi1 = XeHoi("Toyota", 'red', '1 tỏi', 4)
Xedap1 = XeDap("X Game", 'white', '10 triệu', 1)

Xehoi1.khoi_dong()
Xehoi1.chay_bang_bon_banh()

Xedap1.khoi_dong()
Xedap1.dap_bang_hai_chan()
    

        