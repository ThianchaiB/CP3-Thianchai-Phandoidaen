def vatcalculate(price):
    result = price+(price*0.07)
    return result
print(vatcalculate(int(input("price :"))))