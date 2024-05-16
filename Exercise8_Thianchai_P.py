# assign username and password
username = "ballly"
password = "001"
# inputpassword
usernameInput = input("Username : ")
passwordInput = input("Password : ")
# เงื่อนไข
if usernameInput == username and passwordInput == password:
    goods1 = "collagen(II)     size (1,000 g.) "
    price1 = 990
    goods2 = "Cocoa             size (500 g)    "
    price2 = 500
    goods3 = "Whey Protein size(500g)      "
    price3 = 990
# แสดงชื่อร้าน + เมนู
    print("==========================")
    print("Program calculateSomething")
    print("==========================")
    print("-------Hello Welcome-------")
    print("menu")
    print("1."+goods1, "price :", price1, "THB")
    print("2."+goods2, "price :", price2, "THB")
    print("3."+goods3, "price :", price3, "THB")
    print("-----------------------------------")
# ใส่ลำดับของสินค้า
    require1 = int(input("list product round1 : "))
# round 1
    if require1 == 1:
        print(goods1)
        amount1 = int(input("amount : "))
        print(goods1, "x", amount1)
        end1 = input("end? write Y no write N : ")  # ต้องการจบหรือจะเลือกต่อ
        if end1 == "Y":
            print("---------------------bill---------------------")
            print(goods1, "x", amount1, (price1*amount1),  "THB")
            print("total :", (price1*amount1), "THB")
            print("---------------------------------------------")
        else:
            require2 = int(input("list product round2 : "))
            if require2 == 2:
                print(goods2)
                amount2 = int(input("amount : "))
                print(goods2, "x", amount2)
                end2 = input("end? write Y no write N : ")
                if end2 == "Y":
                    print("---------------------bill---------------------")
                    print(goods1, "x", amount1,  (price1 * amount1), "THB")
                    print(goods2, "x", amount2, (price2 * amount2), "THB")
                    print("total :", (price1 * amount1)+(price2 * amount2), "THB")
                    print("---------------------------------------------")
                else:
                    print(goods3)
                    amount3 = int(input("amount : "))
                    print(goods3, "x", amount3)
                    print("---------------------bill---------------------")
                    print(goods1, "x", amount1, (price1 * amount1), "THB")
                    print(goods2, "x", amount2, (price2 * amount2), "THB")
                    print(goods3, "x", amount3, (price3 * amount3), "THB")
                    print("total :", (price1 * amount1) + (price2 * amount2)+(price3 * amount3), "THB")
                    print("---------------------------------------------")
# round 2
            elif require2 == 3:
                print(goods3)
                amount3 = int(input("amount : "))
                print(goods3, "x", amount3)
                end2 = input("end? write Y no write N : ")
                if end2 == "Y":
                    print("---------------------bill---------------------")
                    print(goods1, "x", amount1, (price1 * amount1),  "THB")
                    print(goods3, "x", amount3, (price2 * amount3), "THB")
                    print("total :", (price1 * amount1) + (price3 * amount3), "THB")
                    print("---------------------------------------------")
                else:
                    print(goods2)
                    amount2 = int(input("amount : "))
                    print(goods2, "x", amount2)
                    print("---------------------bill---------------------")
                    print(goods1, "x", amount1, (price1 * amount1), "THB")
                    print(goods2, "x", amount2, (price2 * amount2), "THB")
                    print(goods3, "x", amount3,  (price3 * amount3), "THB")
                    print("total :", (price1 * amount1) + (price2 * amount2) + (price3 * amount3), "THB")
                    print("---------------------------------------------")
# round 1
    elif require1 == 2:
        print(goods2)
        amount2 = int(input("amount : "))
        print(goods2, "x", amount2)
        end1 = input("end? write Y no write N : ")
        if end1 == "Y":
            print("---------------------bill---------------------")
            print(goods2, "x", amount2, (price2 * amount2), "THB")
            print("total :", (price2 * amount2), "THB")
            print("---------------------------------------------")
# round 2
        else:
            require2 = int(input("list product round2 : "))
            if require2 == 3:
                print(goods3)
                amount3 = int(input("amount : "))
                print(goods3, "x", amount3)
                end2 = input("end? write Y no write N : ")
                if end2 == "Y":
                    print("---------------------bill---------------------")
                    print(goods2, "x", amount2, (price2 * amount2), "THB")
                    print(goods3, "x", amount3, (price3 * amount3),  "THB")
                    print("total :", (price2 * amount2) + (price3 * amount3), "THB")
                    print("---------------------------------------------")
                else:
                    print(goods1)
                    amount1 = int(input("amount : "))
                    print(goods1, "x", amount1)
                    print("---------------------bill---------------------")
                    print(goods1, "x", amount1, (price1 * amount1), "THB")
                    print(goods2, "x", amount2, (price2 * amount2), "THB")
                    print(goods3, "x", amount3, (price3 * amount3),  "THB")
                    print("total :", (price1 * amount1) + (price2 * amount2) + (price3 * amount3), "THB")
                    print("---------------------------------------------")
            elif require2 == 1:
                print(goods1)
                amount1 = int(input("amount : "))
                print(goods1, "x", amount1)
                end2 = input("end? write Y no write N : ")
                if end2 == "Y":
                    print("---------------------bill---------------------")
                    print(goods1, "x", amount1, (price1 * amount1),  "THB")
                    print(goods2, "x", amount2, (price2 * amount2),  "THB")
                    print("total :", (price1 * amount1) + (price2 * amount2), "THB")
                    print("---------------------------------------------")
                else:
                    print(goods3)
                    amount3 = int(input("amount : "))
                    print(goods3, "x", amount3)
                    print("---------------------bill---------------------")
                    print(goods1, "x", amount1, (price1 * amount1), "THB")
                    print(goods2, "x", amount2, (price2 * amount2),  "THB")
                    print(goods3, "x", amount3, (price3 * amount3),  "THB")
                    print("total :", (price1 * amount1) + (price2 * amount2) + (price3 * amount3), "THB")
                    print("---------------------------------------------")
# round 1
    elif require1 == 3:
        print(goods3)
        amount3 = int(input("amount : "))
        print(goods3, "x", amount3)
        end1 = input("end? write Y no write N : ")
        if end1 == "Y":
            print("---------------------bill---------------------")
            print(goods3, "x", amount3, (price3 * amount3),  "THB")
            print("total :", (price3 * amount3), "THB")
            print("---------------------------------------------")
        else:
            require2 = int(input("list product round2 : "))
            if require2 == 2:
                print(goods2)
                amount2 = int(input("amount : "))
                print(goods2, "x", amount2)
                end2 = input("end? write Y no write N : ")
                if end2 == "Y":
                    print("---------------------bill---------------------")
                    print(goods2, "x", amount2, (price2 * amount2), "THB")
                    print(goods3, "x", amount3, (price3 * amount3),  "THB")
                    print("total :", (price2 * amount2) + (price3 * amount3), "THB")
                    print("---------------------------------------------")
                else:
                    print(goods1)
                    amount1 = int(input("amount : "))
                    print(goods1, "x", amount1)
                    print("---------------------bill---------------------")
                    print(goods1, "x", amount1, (price1 * amount1),  "THB")
                    print(goods2, "x", amount2, (price2 * amount2),  "THB")
                    print(goods3, "x", amount3, (price3 * amount3),  "THB")
                    print("total :", (price1 * amount1) + (price2 * amount2) + (price3 * amount3), "THB")
                    print("---------------------------------------------")
# round 2
            elif require2 == 1:
                print(goods1)
                amount1 = int(input("amount : "))
                print(goods1, "x", amount1)
                end2 = input("end? write Y no write N : ")
                if end2 == "Y":
                    print("---------------------bill---------------------")
                    print(goods1, "x", amount1, (price1 * amount1), "THB")
                    print(goods3, "x", amount3, (price3 * amount3),  "THB")
                    print("total :", (price1 * amount1) + (price3 * amount3), "THB")
                    print("---------------------------------------------")
                else:
                    print(goods2)
                    amount2 = int(input("amount : "))
                    print(goods2, "x", amount2)
                    print("---------------------bill---------------------")
                    print(goods1, "x", amount1, (price1 * amount1), "THB")
                    print(goods2, "x", amount2, (price2 * amount2),  "THB")
                    print(goods3,  "x", amount3, (price3 * amount3), "THB")
                    print("total :", (price1 * amount1) + (price2 * amount2) + (price3 * amount3), "THB")
                    print("---------------------------------------------")
# not correct password
else:
    print("sorry somthing wrong! please try again. T_T")

