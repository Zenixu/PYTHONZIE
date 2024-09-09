print("\033[97mMASUKAN HARGA HARGA BARANG")
print("====================================================")

b1 = int(input("masukan harga barang pertama: Rp."))
b2 = int(input("masukan harga barang kedua: Rp."))
b3 = int(input("masukan harga barang ketiga: Rp."))
b4 = int(input("masukan harga barang keempat: Rp. "))

total_b = b1 + b2 + b3 + b4 
diskon = 7.5
total = ((100-diskon)/100*total_b)
print("\n====================================================")
print (f"\033[96mTotal semua harga barang yang anda beli adalah Rp.{round(total_b,2)}\n")
print("====================================================")

if total_b >= 200000:
    print (f"\033[93mHarga diskon = Rp.{total_b - total} \n")
    print("====================================================")
    print (f"\033[92mSelamat anda mendapatkan diskon sebesar 7,5%, dan harga yang harus anda bayar sekarang adalah Rp.{round(total,2)}\n")
else:
    print (f"\033[91mKamu tidak mendapat diskon dikarenakan total semua barang yang kemu beli tidak mencapai 200K dan hanya mencapai Rp.{round(total_b,2)}\n")