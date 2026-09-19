def balok():
    print ("==================================")
    print ("=========GEOMETRI BALOK===========")
    print ("==================================")

    p = int(input("masukkan panjangnya: "))
    l = int(input("masukkan lebarnya: "))
    t = int(input("masukkan tingginya: "))

    v = lambda p,l,t : p * l * t
    ls = lambda p,l,t : 2 * (p * l + p * t + l * t)
    k = lambda p,l,t : 4 * (p + l + t)

    print(f'''
    VOLUME BALOK: {v(p,l,t)}
    LUAS BALOK: {ls(p,l,t)}
    KELILING BALOK: {k(p,l,t)}
    ''')
balok()