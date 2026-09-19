huruf = input("Masukkan salah satu huruf (a-z): ")

if huruf in "aiouo" :
    print (f"Huruf {huruf} ini termasuk kedalam huruf vokal ")
elif huruf.isdigit():
    print (f"ini bukan huruf")
else:
    print (f"huruf {huruf} ini termasuk kedalam konsonan")