awal = int(input("masukkan angka awal: "))
akhir = int(input("masukkan angka akhir: "))

total = 0
jumlah = 0

for i in range(awal,akhir +1):
    print(f"{i}")
    total += i
    jumlah += 1
print()
print(f"total semua angka adalah {total}")
print()
print(f"total jumlah angka adalah {jumlah}")

