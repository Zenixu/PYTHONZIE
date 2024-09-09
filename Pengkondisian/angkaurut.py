angka1 = int(input("masukan angka pertama: "))
angka2 = int(input("masukan angka kedua: "))
angka3 = int(input("masukan angka ketiga: "))

if angka1 > angka2:
    angka1, angka2 = angka2, angka1
if angka1 > angka3:
    angka1, angka3 = angka3, angka1
if angka2 > angka3:
    angka2, angka3 = angka3, angka2
print (f"angka terkecil {angka1}, {angka2}, {angka3}")