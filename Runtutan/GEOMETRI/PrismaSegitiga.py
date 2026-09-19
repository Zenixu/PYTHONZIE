print ("==============================")
print ("===GEOMETRI PRISMA SEGITIGA===")
print ("==============================")

a = int(input("masukkan alasnya: "))
t = int(input("masukkan tingginya: "))
tp = int(input("masukkan tinggi prisma: "))

ls = 1/2 * a * t
vp = ls * tp

s = (a**2 + t**2)**(1/2)
ks = 3 * s

lp = 2 * ls + ks * tp 

print (f'''
volume Prisma segitiga: {vp}
luas Prisma segitiga  : {lp}
''')