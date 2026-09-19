pixel = int(input("Masukkan nilai pixel: "))

if pixel < 0:
    pixel = 0
elif pixel > 255:
    pixel = 255

print(f"nilai pixel setelah dipotong adalah {pixel}")