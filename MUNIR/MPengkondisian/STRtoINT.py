huruf = str(input("masukan angka 1-9: "))

if huruf >= '0' and huruf <= '9':
    integer = int(huruf)
else:
    integer = -99
print (f"angka integer adalah {integer}")