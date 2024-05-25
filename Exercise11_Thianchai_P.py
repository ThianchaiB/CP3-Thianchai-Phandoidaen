dokjuninput = int(input("dokjun : "))
b = 0
c = (dokjuninput-1)
for dokjun in range(dokjuninput):
    a = (" "*c) + "*" + "*"*(2*b)
    b = b+1
    c = c - 1
    print(a)