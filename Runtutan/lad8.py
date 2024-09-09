#MENGHITUNG KALOR JENIS ES, KALOR LEBUR ES DAN KALOR JENIS AIR
print("\033[97m*****************************")
m = int(input("masukan berat/massa benda: "))
suhu1 = int(input("masukan suhu pertama: "))
suhu2 = int(input("masukan suhu kedua: "))
dt = (suhu2 - suhu1)
c = 2100
l = 336000
ca = 4200

#-----------------------------------------------
q1 = m * c * dt
q2 = m * l
q3 = m * ca * dt

print("\033[95m=============================")
print("\033[1m   ====KALOR JENIS ES====")
print("\033[95m=============================")
print(f"jadi kalor Jenis es = {round(q1,2)} J\n")
print("\033[91m=============================")
print("\033[1m   ====KALOR LEBUR ES====")
print("=============================")
print(f"jadi kalor lebur Es = {round(q2, 2)} J\n")
print("\033[92m=============================")
print("\033[1m  ====KALOR JENIS AIR=====")
print("=============================")
print(f"Jadi kalor jenis Air = {round(q3, 2)} J\n")
print("\033[92m=============================")