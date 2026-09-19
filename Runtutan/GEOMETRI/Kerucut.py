print ("==================================")
print ("========GEOMETRI KERUCUT==========")
print ("==================================")

PHI = 3.14

r = int(input("masukkan jari-jarinya: "))
s = int(input("masukkan sisi kerucut: "))
t = int(input("masukkan tinggi kerucut: "))
ls = PHI * r * s
lp = (PHI * r * s) + (PHI * r * r)

v = 1/3 * PHI * r * r * t

print(f'''
LUAS ALAS KERUCUT     : {ls}
LUAS PERMUKAAN KERUCUT: {lp}
VOLUME KERUCUT        : {v}
''')