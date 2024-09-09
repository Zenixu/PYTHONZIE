print("\033[97m=========================")
print("MENGHITUNG PANJANG TEROPONG")
print("=========================")

fob = int(input("\033[1;35mmasukan nilai lensa objektif: "))
fp = int(input("masukan nilai lensa pembalik: "))
fok = int(input("masukan nilai lensa okuler: "))

d = fob + (4*fp) + fok

print (f"\n\033[93mPanjang Teropong = {round (d, 2)}")

print("\033[97m=========================")