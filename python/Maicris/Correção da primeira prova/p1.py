a = "Suco"
b = 5
c = False

if a == "Açai":
    a=10
elif a =="Carro":
    a = 15/2
else:
    a = 10 ** 2
    if b >= 50:
        b = True
    else:
        b = False
if c == True:
    print(b or a >=100)
else:
    print(b and a >= 100)