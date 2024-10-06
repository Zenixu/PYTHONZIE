bulan = int(input("masukkan nomor bulan 1-12: "))
tahun = int(input("masukkan tahun: "))

if bulan == 1:
    hari = (f"31, Januari")
elif bulan == 2:
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        hari = (f"29, Februari") 
    else:
        hari = (f"28, Februari")
elif bulan == 3:
    hari = (f"31, Maret")
elif bulan == 4:
    hari = (f"30, April")
elif bulan == 5:
    hari = (f"31, Mei")
elif bulan == 6:
    hari = (f"30, Juni")
elif bulan == 7:
    hari = (f"31, Juli")
elif bulan == 8:
    hari = (f"31, Agustus")
elif bulan == 9:
    hari = (f"30, September")
elif bulan == 10:
    hari = (f"31, Oktober")
elif bulan == 11:
    hari = (f"30, November")
elif bulan == 12:
    hari = (f"31, Desember")
else:
    hari = 0

if hari != 0: 
    print(f"Jumlah hari dalam bulan {bulan} tahun {tahun} adalah {hari}.")
else:
    print("nomor bulan tidak ada masukkan 1-12")