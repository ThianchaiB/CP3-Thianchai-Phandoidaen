menuList = []
def ShowBill():  #ใช้แสดงบิล
    print("Food Bill".center(20, "-"))
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
    print("Total :", TotalPrice(), "Bath")
    print("".__add__(20*"-"))
def TotalPrice():  #ใช้คำนวนราคาทั้งหมด
    price = 0
    for number in range(len(menuList)):
        price = price + int(menuList[number][1])
    return price
while True:  #เพื่อเรียกใช้ลูปเติมรายการสินค้า
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Price : ")
        menuList.append([menuName, menuPrice])
ShowBill()

