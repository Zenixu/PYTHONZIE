golongan = input('masukkan golongan A,B,C,D: ').upper()
jam_kerja = int(input('masukkan jam kerja: '))
jam_lembur = int(input('masukkan jam lembur: '))
print ("="*40)

if golongan == 'A':
    upah_perjam = 4000
elif golongan == 'B':
    upah_perjam = 5000
elif golongan == 'C':
    upah_perjam = 6000
elif golongan == 'D':
    upah_perjam = 7500
else:
    print ("Golongan ini tidak ada")
    upah_perjam = 0

upah_kerja = jam_kerja * upah_perjam
upah_lembur = jam_lembur * (upah_perjam * 1.5) 
total_upah = upah_kerja + upah_lembur

print (f"Total upah = Rp.{round(total_upah)}\n")