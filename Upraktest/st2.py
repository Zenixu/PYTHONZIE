awal = int(input("masukkan nilai awal: "))
akhir = int(input("masukkan nilai akhir: ")) 

total = 0
jumlah = 0

for i in range(awal, akhir + 1):
    if i % 2 == 0:
        print("-", i)
        total += i
        jumlah += 1
print(f"total semua angka adalah {total}")
print()
print(f"total jumlah angka adalah {jumlah}")
