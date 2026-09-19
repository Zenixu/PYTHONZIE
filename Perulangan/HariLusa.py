print("\n")
print("="*30)
print("Hari Lusa")
print("="*30)

hari = input("Masukan nama hari : ")

if hari == "senin":
    print("Lusa adalah rabu")
elif hari == "selasa":
    print("Lusa adalah kamis")
elif hari == "rabu":
    print("Lusa adalah jumat")
elif hari == "kamis":
    print("Lusa adalah sabtu")
elif hari == "jumat":
    print("Lusa adalah minggu")
elif hari == "sabtu":
    print("Lusa adalah senin")
elif hari == "minggu":
    print("Lusa adalah selasa")
else:
    print("ini bukan nama hari")