def Login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False
def Showmenu():
    print("Done !")
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def Menuselect():
    userSelected = int(input("Select Menu>>"))
    return userSelected
def Vatcalculate(totalprice):
    vat = 7
    result = totalprice + (totalprice * vat / 100)
    return result
def Pricecalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    totalprice = price1 + price2
    return Vatcalculate(totalprice)
def monoprice():
    totalprice = int(input("Price (THB) : "))
    return Vatcalculate(totalprice)
if Login() == True:
    Showmenu()
    userselect = Menuselect()
    if userselect == 1:
        print(monoprice(),"THB")
    elif userselect == 2:
        print(Pricecalculate(),"THB")
    elif userselect > 2:
        print("-sorry something wrong X \n   (please try againT_T)-")
else:
    print("username or password mistake please try again")


