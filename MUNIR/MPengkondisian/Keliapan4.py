air = (input("kondisi air di dalam ketel?: ")).lower()
if air == "mendidih":
    print ("matikan ketel ")
elif air == "tidak mendidih":
    print ("tidak perlu mematikan kompor")
else: 
    print ("pilihan ini tidak ada")

suhu = int(input("masukan suhu ruangan : "))
if suhu >= 50:
    print (f"suhu ruangan diatas {suhu} maka nyalakan alarm tanda bahaya")
elif suhu <= 50:
    print (f'tidak perlu menyalakan alarm ')
else:
    print ("pilihan ini tidak ada")

mobil = (input('apakah mobil rusak y/g: ')).lower
if mobil == 'y':
    print ('mobil rusak dan kamu naik angkot')
elif mobil == 'g':
    print ('mobil tidak rusak')
else:
    print ("pilihan ini tidak ada")

x = int(input("masukan nilai x: "))
if x % 2 == 0:
    print(f"{x} adalah bilangan genap")
elif x % 2 == 1:
    print (f"{x} adalah bilangan ganjil")
else:
    print ("tidak ada pilihan ini")