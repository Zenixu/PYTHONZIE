import os

os.system("cls")
print("="*35)
print("Menghitung Energi Mekanik")
print("="*35)

m = int(input("masukkan massa: "))
v = int(input("masukkan kecepatannya: "))
ek = m * 1/2 ** v

print("="*35)
m1 = int(input("masukkan massa bendanya: "))
G = 10
h = int(input("masukkan ketinggian bendanya: "))

ep = m1 * G * h
em = ek + ep

print(f"Energi mekanik nya adalah {round(em)}")