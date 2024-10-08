def bola():
    print ("==============================")
    print ("========GEOMETRI BOLA=========")
    print ("==============================")

    PHI = 3.14
    r = int(input("masukkan jari jarinya: "))

    lb = lambda r: 4 * PHI * r * r
    vb = lambda r: 4/3 * PHI * r * r * r

    print(f'''
    LUAS BOLA  : {lb(r)}
    VOLUME BOLA: {vb(r)}
    ''')
bola()