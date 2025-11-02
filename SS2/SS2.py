# ### Buổi 2: 



# ##### Đối tượng "dictionary": key - value
# cho1 = {
#     "name": "Golden",
#     'age': 30,
#     'fur': 'black',
#     "nose": "long",
#     'kind': 'Husky',
# }

# ##### Truy cập thuộc tính
# ## tên?
# print(cho1["name"])

# ##### Cập nhật giá trị
# ## đổi tuổi 30 -> 25
# cho1['age'] = 25
# print(cho1['age']) # 25!!!

# ##### Thêm thuộc tính: 'gender'
# cho1['gender'] = 'male'
# print(cho1['gender'])


# ##### Xóa thuộc tính or xóa hết 
# del cho1['nose']
# print(cho1)

# ##### Xóa hết key: dict.clear()
# cho1.clear()
# print(cho1)



######### Tạo lớp Xehoi - bản thiết kế
class Car:
    # Hàm khởi tạo thuộc tính
    def __init__(self, so_banh, mau_sac, hang_xe, so_cho):
        self.so_banh = so_banh
        self.mau_sac = mau_sac
        self.hang_xe = hang_xe
        self.so_cho = so_cho
            
    # Hàm in ra terminal: Hàm trình bày KDL này dưới dạng String. 
    def __str__(self):
        return f'Ô tô có số bánh là {self.so_banh}, màu {self.mau_sac} thuộc hãng xe {self.hang_xe} với số chỗ là {self.so_cho}'
        
### Khởi tạo đối tượng mang kiểu dữ liệu ô tô
car1 = Car(4, "blue", "Tesla", "12")
print(car1) ### 


car2 = Car(12, 'Black', 'Limo', '7')
print(car2)

