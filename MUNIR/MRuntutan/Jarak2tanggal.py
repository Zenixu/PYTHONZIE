TAHUN = 365
BULAN = 30

tahun1 = int(input("Masukkan tahun pertama: "))
bulan1 = int(input("masukkan bulan pertama: "))
hari1 = int(input("Masukkan hari pertama: "))

print ("==============================")

tahun2 = int(input("Masukkan tahun Kedua: "))
bulan2 = int(input("masukkan bulan kedua: "))
hari2 = int(input("Masukkan hari kedua: "))

total_hari1 = tahun1 * TAHUN + bulan1 * BULAN + hari1
total_hari2 = tahun2 * TAHUN + bulan2 * BULAN + hari2

selisih_hari = total_hari2 - total_hari1

tahun = int(selisih_hari / TAHUN)
sisa_hari = selisih_hari % TAHUN
bulan = int(sisa_hari / BULAN)
hari = sisa_hari % BULAN

print (f"{tahun} tahun {bulan} bulan {hari} hari")