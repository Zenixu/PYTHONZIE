print("\n")
print("\t\t ","="*30)
print("\t\t\tSoal Soal Looping")
print("\n")

#!1
i = 1 
while i < 4:
    print(i, '-Hello ', end='')
    i = i + 1
print( )

#!2
j = 3
while j > 0:
    print(j, '-Hello ', end='')
    j = j - 1
print( )

#!3
k = 1
while k < 6:
    print(k, '-Hello ', end='')
    k = k + 2
print( )

#!4
l = 0
while l < 7:
    print(l, '-Hello ', end='')
    l = (l + 1) * 2
print( )

#!5
m = 10
while m < 101:
    print(m, end=' ')
    m = m + 10
print( )

#!6
n = 2000
while n < 2006:
    print(n, end=' ')
    n = n + 1
print( )

#!7
BARIS = 5
for a in range(BARIS):
    for b in range(BARIS-a):
        print("", end="")
    for c in range(a+1):
        print("*", end="")
    print('')
BARIS1 = 4
for d in range(BARIS1):
    for d in range(BARIS1-d):
        print(end='')
    for e in range(d+1):
        print("*", end='')
    print()

print('\n')

z = 5
for i in range(1, z+1):
    for x in range (1, i + 1):
        print ("*", end="")
    print ("")
print()

zz = 5
while 0 < zz:
    print("*"*zz)
    zz -= 1
print("")


zx = 5
for i in range(1, zx+1):
    for xx in range (1, i + 1):
        print ("*", end="")
    print ("")
xz = 4
while 0 < xz:
    print("*"*xz)
    xz -= 1
print("")

zx = 4
for i in range(1, zx+1):
    for xx in range (1, i + 1):
        print ("*", end="")
    print ("")
xyz = 6
print ("*"*7)
xz = 4
while 0 < xz:
    print("*"*xz)
    xz -= 1
print("")

baris = 5
for i in range (baris):
    for a in range (baris - i - 1):
        print (" ", end="")
    for b in range (2 * i + 1):
        print ("*", end="")
    print ("")
print()
angka = 1
while angka < 6:
    print(angka)
    angka = angka + 1
print('------+')
print(15)

print('\n')

angka = 1
while angka < 6:
    print(angka, end=' ')
    angka = angka + 1
print('= 15')

angka = 3
print(1, end='')
while angka < 6:
    print(' +', angka, end='')
    angka = angka + 2
print(' = 9')

angka = 4
print(2, end='')
while angka < 11:
    print(' +', angka, end='')
    angka = angka + 2
print(' = 30')

angka = 2
print(1, end='')
while angka < 6:
    print(' +', angka, end='')
    angka = angka + 1
print(' = 15')