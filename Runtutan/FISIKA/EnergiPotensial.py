import os
os.system("cls")

print("="*35)
print("Menghitung Energi Potensial")
print("="*35)

m = int(input("masukkan massa bendanya: "))
G = 10
h = int(input("masukkan ketinggian bendanya: "))

ep = m * G * h

print(f"Energi potensialnya adalah {ep}")