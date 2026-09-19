tinggi = int(input("Masukkan tinggi: "))

print("\nPola Bintang Segitiga:")

# Loop untuk menampilkan pola bintang segitiga
for i in range(1, tinggi + 1):
    print("*" * i)
for i in range(tinggi - 1):
    print("*" * i)