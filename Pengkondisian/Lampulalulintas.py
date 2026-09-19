WARNA1 = 'merah' 
WARNA2 = 'kuning'
WARNA3 = 'hijau'

lampu_lalu_lintas = input("masukkan warna lampu lalu lintas: ").lower()

if lampu_lalu_lintas == WARNA1:
    print ("KAMU HARUS BERHENTI\n")
elif lampu_lalu_lintas == WARNA2:
    print ("BERSIAP SIAP\n")
elif lampu_lalu_lintas == WARNA3:
    print ("WAKTUNYA MAJU\n")
else:
    print ("pilihan ini tidak ada di dalam daftar\n")