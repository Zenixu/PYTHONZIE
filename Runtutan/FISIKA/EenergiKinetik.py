import os
os.system("cls")

print("="*35)
print("Menghitung Energi Kinetik")
print("="*35)

m = int(input("masukkan massanya: "))
v = int(input("masukkan kecepatannya: "))

ek = m * 1/2 ** v

print(f"Jadi energi kinetiknya adalah '{ek}' ")