#Soal 4 menghitung berapa kali seseorang yang lahir di tahun kabisat ulang tahun dengan memasukan tanggal lahir dan tanggal sekarang
tl = int(input("Masukkan tahun lahir: "))
ts = int(input("Masukkan tahun sekarang: "))

if (tl % 4 == 0 and tl % 100 != 0) or (tl % 400 == 0):

    jumlah_ultah = 0
    for tahun in range(tl, ts + 1):
        if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
            jumlah_ultah += 1
    
    print(f'''\nRincian perhitungan
    - Tahun lahir: {tl}
    - Tahun sekarang: {ts}
    - Jumlah ulang tahun yang dirayakan: {jumlah_ultah} kali''')
    
    print("\nUlang tahun dirayakan pada tahun:")
    for tahun in range(tl, ts + 1):
        if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
            print(f"- {tahun}")
else:
    print('''\nMaaf, tahun lahir yang dimasukkan bukan tahun kabisat!
    Tahun kabisat adalah tahun yang habis dibagi 4 dan bukan kelipatan 100
    atau tahun yang habis dibagi 400.''')