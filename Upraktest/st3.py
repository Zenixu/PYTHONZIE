angka = int(input("masukkan angka: "))
kali = int(input("masukkan angka yang ingin dikali: "))

print(f"tabel perkalian {angka}:")
for i in range(1, kali + 1):
    hasil = angka * i
    print(f"{angka} x {i} = {hasil}")
