def jajargenjang():
    print ("==============================")
    print ("====GEOMETRI  JAJARGENJANG====")
    print ("==============================")

    a = int(input("masukan alasnya: "))
    t = int(input("masukkan tingginya: "))

    ljg = lambda a,t : a * t
    kjg = lambda a,t : 2 * (a + t)

    print(f'''
    LUAS JAJARGENJANG    : {ljg(a)}
    KELILING JAJARGENJANG: {kjg(t)}
    ''')
jajargenjang()