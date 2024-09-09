a = int(input("masukkan sisi a: "))
b = int(input("masukkan sisi b: "))
c = int(input("masukkan sisi c: "))

if a < b < c:
    if a**2 + b**2 == c**2:
        print ("segitiga siku-siku")
    elif a**2 + b**2 > c**2:
        print ("segitiga Lancip")
    else:
        print ("segitiga tumpul")
else:
    print("Panjang sisi tidak benar, pastika a < b < c")