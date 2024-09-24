print ("==============================")
print ("===GEOMETRI LIMAS SEGIEMPAT===")
print ("==============================")

ls = int(input("masukkan luas: "))
la = int(input("masukkan luas alas: "))
t = int(input("masukkan tinggi: "))

l = ls + ls + ls + ls
v = 1/3 * la * t

print(f'''
LUAS LIMAS SEGITIGA: {l}
VOLUME LIMAS SEGITIGA: {v}
''')
