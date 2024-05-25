dokjuninput = int(input("dokjun : "))  # กำหนดฐาน pyramid
b = 0
c = (dokjuninput-1)
for dokjun in range(dokjuninput):
    pyramid = (" "*c) + "*" + "*"*(2*b)  # สร้างรูป
    b = b+1
    c = c - 1
    print(pyramid)  #แสดงออก