TAHUN_HARI = 365
BULAN_HARI = 30

hari = int(input("masukkan jumlah hari: "))
tahun = int(hari / TAHUN_HARI)
hari = hari % TAHUN_HARI
bulan = int (hari / BULAN_HARI)
hari = hari % BULAN_HARI

print (f"{tahun} tahun {bulan} bulan {hari} hari")