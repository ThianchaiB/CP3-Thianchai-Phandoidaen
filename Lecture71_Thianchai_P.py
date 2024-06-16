menuList = []
priceList = []
while True:
    menuName = input("please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)
def TotalPrice():
    price = 0
    for a in range(len(priceList)):
        price = price + int(priceList[a])
    print("Total : ",price,"Bath")
def Showbill():
    a = "Food Bill"
    print(a.center(20,"-"))
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
    TotalPrice()
    b = ""
    print(b.__add__(20*"-"))
Showbill()
