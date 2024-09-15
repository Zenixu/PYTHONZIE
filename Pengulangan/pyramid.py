n = 1
while n<6:
    print ("1 2 3 4 5")
    n = n + 1
print()
z = 1
for a in range (5):
    print ("a a a a a")
    z = z + 1


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
print ("*"*6)
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

baris = 7
for i in range(1, baris + -1):
    spasi = baris - i
    print(" " * spasi, end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
for i in range(baris - 1, 0, -1):
    spasi = baris - i
    print(" " * spasi, end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

for xyz in ("abcde"):
    print (5*xyz)