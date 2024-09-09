#Menghitung Luas dan Keliling Segitiga
while True:
    print("==========================")
    print("Untuk mengukur Luas")

    a = int(input("Masukan Alas: "))
    t = int(input("Masukan Tinggi: "))

    print("==========================")
    print("Untuk mengukur Keliling")

    sisi_a = int(input("Masukan sisi 1: "))
    sisi_b = int(input("Masukan sisi 2: "))
    sisi_c = int(input("Masukan sisi 3: "))

    l = 0.5 * a * t
    k = (sisi_a + sisi_b + sisi_c)

    print("==========================")
    print(f"Luas Segitiga = {l} cm²")

    print(f"Keliling Segituga = {k} cm\n")