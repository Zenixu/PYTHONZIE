DISKON = 0

total_belanja = int(input("masukan total belanja: "))
total_setelah_diskon = total_belanja

if total_belanja >= 100000:
    DISKON = total_belanja * 0.25
    total_setelah_diskon = total_belanja - DISKON
    print (f'''
        Kamu mendapatkan diskon 25% sebesar Rp.{DISKON} 
        Jadi total yang harus dibayar adalah {total_setelah_diskon}\n
        ''')
else:
    print ("kamu tidak mendapatkan diskon\n")
