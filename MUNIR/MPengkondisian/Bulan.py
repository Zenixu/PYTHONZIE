nomor_bulan = int(input("masukan nomor bulan 1-12: "))

if nomor_bulan == 1:
    bulan = "Januari"
elif nomor_bulan == 2:
    bulan = "Februari"
elif nomor_bulan == 3:
    bulan = "Maret"
elif nomor_bulan == 4:
    bulan = "April"
elif nomor_bulan == 5:
    bulan = "Mei"
elif nomor_bulan == 6:
    bulan = "Juni"
elif nomor_bulan == 7:
    bulan = "Juli"
elif nomor_bulan == 8:
    bulan = "Agustus"
elif nomor_bulan == 9:
    bulan = "September"
elif nomor_bulan == 10:
    bulan = "Oktober"
elif nomor_bulan == 11:
    bulan = "November"
elif nomor_bulan == 12:
    bulan = "Desember"
else:
    print("nomor bulan tidak valid")

print (f"bulan {nomor_bulan} adalah {bulan}\n")