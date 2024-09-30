barang1 = int(input("Masukkan harga barang: "))
diskon = 5
if barang1 >= 100000:
    print (f"selamat kamu mendapatkan diskon sebesar 5% jadi total harga yang harus kamu bayar adalah {((100-diskon)/100*barang1)}")
else:
    print ("Kamu tidak mendapatkan diskon")