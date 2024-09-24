t = int(input("masukkan tinggi: "))
a = int(input("masukkan sisi A: "))
b = int(input("masukkan sisi B: "))
c = int(input("masukkan sisi C: "))
d = int(input("masukkan sisi D: "))

l = 1/2 * (a + b) * t
k = a + b + c + d

print(f'''
Luas Trapesium: {l}
Keliling Trapesium: {k}
''')