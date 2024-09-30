nilai_belanja = int(input("masukkan nilai belanja: Rp."))
PECAHAN_TERENDAH = 25

nilai_belanja_bulat = (nilai_belanja // PECAHAN_TERENDAH) * PECAHAN_TERENDAH

print (f"Nilai belanja setelah dibulatkan ke pecahan terendah adalah Rp.{nilai_belanja_bulat}")