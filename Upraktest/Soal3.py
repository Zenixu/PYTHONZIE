# Soal 3 buatlah 3 inputan barang dengan 1 point barang = 20000

b1 = int(input("masukkan harga barang 1: "))
b2 = int(input("masukkan harga barang 2: "))
b3 = int(input("masukkan harga barang 3: "))

jumlah = b1 + b2 + b3

PHB = 20000
point = 1
while jumlah >= PHB:
    print (f"point yang didapatkan {point}")
    point += 1
    PHB += 20000