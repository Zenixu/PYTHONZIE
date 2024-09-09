bilangan = int(input("Masukkan bilangan angka: "))

if bilangan > 0:
    if bilangan % 4 == 0:
        print (f"{bilangan} adalah kelipatan 4")
    else:
        print (f"{bilangan} bukan kelipatan 4")
else:
    print (f"{bilangan} bukan bilangan positif")