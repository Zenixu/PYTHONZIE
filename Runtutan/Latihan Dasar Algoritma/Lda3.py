#Menghitung Keliling lingkaran 
while True:
    print ("<=========================>")
    r = float(input("Masukan jari-jari: "))
    #Nilai pi ada 2 yaitu (3.14 dan 22/7)
    pi = 3.14

    l = (r * r * pi)
    k = (2 * pi * r)

    print ("\n==========================")
    print(f"Luas Lingkaran = {l} cm²")
    print ("==========================")
    print(f"Keliling Lingkaran = {k}cm\n")