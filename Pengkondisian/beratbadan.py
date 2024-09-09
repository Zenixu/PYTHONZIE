tb = int(input("masukkan tinggi badan: "))
bb = int(input("masukkan berat badan: "))

bb_ideal = (tb-100)-((tb-100) * 0.1)
selisih = (bb-bb_ideal)

if selisih <= 2:
    print ("Berat badan ideal")
else:
    print ("Berat badan tidak ideal")