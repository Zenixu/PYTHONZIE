nilai = int(input("masukkan nilai: "))

if nilai >= 80:
    indeks= 'A'
elif nilai >= 70 < 80:
    indeks = 'B'
elif nilai >= 55 < 70:
    indeks = 'C'
elif nilai >= 40 < 55:
    indeks = 'D'
else:
    indeks = 'E'

print (f"nilai {nilai} dan Indeks nilai adalah {indeks}\n")
