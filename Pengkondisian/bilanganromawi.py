bilangan = int(input("masukkan bilangan positif: "))

if bilangan == 1:
    romawi = 'I'
elif bilangan == 2:
    romawi = "II"
elif bilangan == 3:
    romawi = "III"
elif bilangan == 4:
    romawi = "IV"
elif bilangan == 5:
    romawi = "V"
elif bilangan == 6:
    romawi = "VI"
elif bilangan == 7:
    romawi = "VII"
elif bilangan == 8:
    romawi = "VIII"
elif bilangan == 9:
    romawi = "IX"
elif bilangan == 10:
    romawi = "X"
else:
    romawi = "Bilangan bukan romawi"

print ("angka Romawi: ",romawi)

breakpoint
print ('='*30)
bilangan = int(input('masukkan bilangan positif: '))
angka_romawi = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
    (1, "I")
]

romawi = ""
for nilai, simbol in angka_romawi:
    while bilangan >= nilai:
        romawi += simbol
        bilangan -= nilai

print("Angka Romawi:", romawi)