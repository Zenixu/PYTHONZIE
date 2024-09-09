#LATIHAN 1 VARIABEL
nama = "Ibnu Hambal Al Bantani Rch"
kelamin ="Laki-Laki"
usia = 15
nilai_matematika = 78.56
nilai_Bahasa_Indonesia = 80.91
nilai_Ipas = 88.12
nilai_Bahasa_inggris = 95.21
jumlah_nilai = nilai_matematika + nilai_Bahasa_inggris + nilai_Bahasa_Indonesia + nilai_Ipas
rata_rata = (nilai_Bahasa_Indonesia + nilai_Bahasa_inggris + nilai_matematika + nilai_Ipas) / 5

print(f'''
    Nama saya adalah {nama} berjenis kelamin {kelamin} 
    sekarang usia saya adalah {usia} 
    Nilai ujian terakhir saya adalah sebagai berikut: 
    Matematika   : {nilai_matematika} 
    B. Indonesia : {nilai_Bahasa_Indonesia} 
    B. Inggris   : {nilai_Bahasa_Indonesia} 
    IPAS         : {nilai_Ipas} 
    TOTAL NILAI  : {jumlah_nilai}
    RATA-RATA    : {rata_rata}
''')