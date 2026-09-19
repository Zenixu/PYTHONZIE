INCHI = 39
KAKI = 3
YARD = 1

meter = int(input("masukkan panjang sebuah benda (meter): "))
inchi = int(meter / INCHI)
meter = meter % INCHI
kaki = int(meter / KAKI)
meter = meter % KAKI
yard = int(meter / YARD)

print (f"{inchi} inchi {kaki} kaki {round (yard, 0)} yard\n")