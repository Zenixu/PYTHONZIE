print("\n")
print("="*30)
print("Next Month")
print("="*30)

bulan = input("Masukan nama Bulan: ").lower()

if bulan == "januari":
    print("Bulan depan adalah Februari")
elif bulan == "februari":
    print("Bulan depan adalah Maret")
elif bulan == "maret":
    print("Bulan depan adalah April")
elif bulan == "april":
    print("Bulan depan adalah Mei")
elif bulan == "mei":
    print("Bulan depan adalah Juni")
elif bulan == "juni":
    print("Bulan depan adalah Juli")
elif bulan == "juli":
    print("Bulan depan adalah Agustus")
elif bulan == "agustus":
    print("Bulan depan adalah September")
elif bulan == "september":
    print("Bulan depan adalah Oktober")
elif bulan == "oktober":
    print("Bulan depan adalah November")
elif bulan == "november":
    print("Bulan depan adalah Desember")
elif bulan == "desember":
    print("Bulan depan adalah januari")
else:
    print("ini bukan nama bulan")