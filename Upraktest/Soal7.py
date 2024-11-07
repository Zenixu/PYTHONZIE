n1 = int(input("masukkan nilai pertama: ")) 
n2 = int(input("masukkan nilai kedua: ")) 
n3 = int(input("masukkan nilai ketiga: ")) 

if n1 >= n2 >= n3:
    print (f"nilai {n1} {n2} {n3}")
elif n1 >= n3 >= n2:
    print (f"nilai {n1} {n3} {n2}")
elif n2 >= n1 >= n3:
    print (f"nilai {n2} {n1} {n3}")
elif n2 >= n3 >= n1:
    print (f"nilai {n2} {n3} {n1}")
elif n3 >= n2 >= n1:
    print (f"nilai {n3} {n2} {n1}")
elif n3 >= n2 >= n1:
    print (f"nilai {n3} {n1} {n2}")