#MEMBUAT PROGRAM NILAI 
while True:
    nama = str(input("Siapa nama kamu?: "))
    nilai = int(input("Masukkan nilai kamu: "))

    if(nilai > 80):
        print(f"Selamat {nama}, Kamu telah Lulus dengan nilai {nilai}")
    else:
        print(f"Yahhh {nama}, Kamu Tidak Lulus dengan nilai {nilai} di bawah KKM SI BRO\n")