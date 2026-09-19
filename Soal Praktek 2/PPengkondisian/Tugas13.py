x = int(input("Masukan nilai x: "))
y = int(input("Masukan nilai y: "))
z = int(input("Masukan nilai z: "))

if x >= y >= z:
    print ("Maka nilai X adalah yang paling besar dan Z berarti nilai terkecil")
elif x >= z >= y:
    print ("Maka nilai X adalah yang paling besar dan Y berarti nilai terkecil")
elif y >= x >=z:
    print ("maka nilai Y adalah yang paling besar dan Z berarti nilai terkecil ")
elif y >= z >=x:
    print ("maka nilai Y adalah yang paling besar dan X berarti nilai terkecil ")
elif z >= x >=y:
    print ("maka nilai Z adalah yang paling besar dan Y berarti nilai terkecil ")
elif z >= y >=x:
    print ("maka nilai Z adalah yang paling besar dan X berarti nilai terkecil ")
