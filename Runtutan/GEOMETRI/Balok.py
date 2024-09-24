print ("==================================")
print ("=========GEOMETRI BALOK===========")
print ("==================================")

p = int(input("masukkan panjangnya: "))
l = int(input("masukkan lebarnya: "))
t = int(input("masukkan tingginya: "))

v = p * l * t
l = 2 * (p * l + p * t + l * t)
k = 4 * (p + l + t)

print(f'''
VOLUME BALOK: {v}
LUAS BALOK: {l}
KELILING BALOK: {k}
''')