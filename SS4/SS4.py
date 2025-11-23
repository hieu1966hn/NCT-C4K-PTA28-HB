### Bài thực hành 1:
class DongVat:
    # Phương thức khởi tạo
    def __init__(self, name, age, kind, habitat):
        self.name = name
        self.age = age
        self.kind = kind
        self.habitat = habitat
    
    # Phương thức cập nhật môi trường sống
    def change_habitat(self, new_habitat):
        self.habitat = new_habitat # gán lại giá trị cho thuộc tính
    
    # In ra thông tin của động vật
    def __str__(self):
        return f'Loài {self.name} với {self.age} tuổi thuộc loài {self.kind} và sống ở {self.habitat}'
        
# dog1 = DongVat("Chó", 15, "Chihuahua", 'đô thị')
# dog1.change_habitat("Nông thôn")
# print(dog1)
    
    
    
### Bài thực hành số 2
class PhuongTien:
    def __init__(self, bien_so, hang_xe, mau_sac):
        self.bien_so = bien_so
        self.hang_xe = hang_xe
        self.mau_sac = mau_sac
    
    def change_color(self, new_mau_sac):
        self.mau_sac = new_mau_sac
    
    def display_info(self):
        return f'Phương tiện này có biển số là {self.bien_so} thuộc hãng xe {self.hang_xe} với màu sắc {self.mau_sac}'

### Lớp xe máy kế thừa từ lớp PhuongTien
class XeMay(PhuongTien):
    def __init__(self, bien_so, hang_xe, mau_sac, loai_xe):
        super().__init__(bien_so, hang_xe, mau_sac)
        self.loai_xe = loai_xe
    
    # Kế thừa phương thức display_info của cha và bổ sung thêm "loại xe" vào đó
    def display_info(self):
        return super().display_info() + f" và là loại xe {self.loai_xe}"
    

xemay1 = XeMay("29F1 - 99999", "Honda", 'xi măng', 'tay ga')
print(xemay1.display_info())
    
        

    
        
        
    