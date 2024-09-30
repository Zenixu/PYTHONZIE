nama_karyawan = input("masukkan nama karyawan: ")
gaji_pokok = int(input("masukkan gaji pokok: "))

tunjangan = int(0.2 * gaji_pokok)
pajak = int(0.15 * (gaji_pokok + tunjangan))

gaji_bersih = int((gaji_pokok + tunjangan) - pajak)

print (f'''
gaji pokok : Rp.{gaji_pokok}
tunjangan  : Rp.{tunjangan}
pajak      : Rp.{pajak}
gaji bersih: Rp.{gaji_bersih}\n
''')