import os
os.system("cls")
a = int(input("masukkan angka 1: "))
b = int(input("masukkan angka 2: "))
print(f"{a} > {b}") if a > b else print("angka sama besar") if a == b else print(f"{a} < {b}")