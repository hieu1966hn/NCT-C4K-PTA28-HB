# ## Ví dụ về biến toàn cụ & cục bộ

# a = 100

# def test():
#     b = 200 ## biến cục bộ (phạm vi: trong hàm test)
#     print(a) ## 100 - biến toàn cục
    
# test() # gọi hàm
# print(b) ## không ra????


#### Các kiểu dữ liệu trong Python: String, int, float, bools, list, Dict (mới)

#### Khởi tạo 1 Dictinary: key - value
# dog = {
#     "name": "Alaska",
#     "age": 30,
#     "color": "White",
#     "eat": "meat",
#     "kind": {
#         "Giới": "Animals",
#         "Ngành": "Động vật có xương sống",
#         "Lớp": "Thú ăn thịt",
#         "Họ": "Chó",
#     },
#     "Hành vi & giao tiếp": {
#         "Tiếng kêu chính": ['Sủa', "gầm gừ",'Tru', 'Rên rỉ'],
#     }
# }

# ### Truy vấn giá trị: theo key dict["key"]
# # print(dog["name"])

# ## Chỉ in ra tiếng sủa của chú chó DOG
# print(dog["Hành vi & giao tiếp"]["Tiếng kêu chính"][0])

# ### Thêm khóa mới cho dict dog: dog.update(newkey)
# khoamoi = {
#     "Chăm sóc hàng ngày": ["chải lông", 'vệ sinh răng miệng', 'cắt tỉa móng']
# }
# dog.update(khoamoi)

# ### Cập nhật "cắt tỉa móng" => "Cắt tỉa râu"
# dog["Chăm sóc hàng ngày"][2] = "Cắt tỉa râu"
# print(dog["Chăm sóc hàng ngày"])

# #### xóa khóa 
# del dog['age']
# print(dog["age"]) ## Lỗi vì đã xóa khóa

###### CCCD
# "00001123020103" = {
#     "id": "00001123020103",
#     "name": "Nguyễn Trung Hiếu",
#     "gender": "Nam"
# }



##### Kiểu số
# a = 3**4 # 81
# print(f"Chia lấy phần nguyên {a // 2}")
# print(f"Chia lấy phần dư {a % 2}")


#### Danh sách
# so_phan_tu_list = int(input("Nhập số phần tử danh sách: ")) # 5
# arr = []
# for i in range(so_phan_tu_list):
#     arr.append(int(input(f"Nhập vào phần tử vị trí thứ {i + 1}: ")))

# ## Xóa các số lẻ trong danh sách
# for item in arr:
#     if item % 2 == 0:
#         continue ## break vẫn hoạt động (vô lý)!!!!
#     else: 
#         arr.remove(item)
        
# print(f'Danh sách sau khi xóa các số lẻ là {arr}')



##### Xây dựng bài: 
import math
def rut_gon(tu, mau):
    UC = math.gcd(tu, mau)
    phan_so_clean = f'{int(tu/UC)}/{int(mau/UC)}'
    return phan_so_clean

tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))

print("Phân số được rut gọn: ", rut_gon(tu, mau))
