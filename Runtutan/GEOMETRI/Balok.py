print ("==================================")
print ("=========GEOMETRI BALOK===========")
print ("==================================")

p = int(input("masukkan panjangnya: "))
l = int(input("masukkan lebarnya: "))
t = int(input("masukkan tingginya: "))

v = p * l * t
ls = 2 * (p * l + p * t + l * t)
k = 4 * (p + l + t)

print(f'''
VOLUME BALOK: {v}
LUAS BALOK: {ls}
KELILING BALOK: {k}
''')