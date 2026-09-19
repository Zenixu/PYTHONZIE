# buatlah program berupa inputan mata pelajaran uts tugas uas A = 85 B 70-85 C= 60-7 else= D
mapel = str(input("masukkan nama pelajaran: "))
tugas = int(input("masukkan nilai tugas: "))
uts = int(input("masukkan nilai uts: "))
uas = int(input("masukkan nilai uas: "))

jumlah = uts + tugas + uas 
rata_rata = jumlah/3

if rata_rata >= 85:
    print("nilai A")
elif 85 <= rata_rata >= 70:
    print("nilai B")
elif 70 <= rata_rata >= 60:
    print("nilai C")
else:
    print ('nilai D')