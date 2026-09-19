print("\n")
print("\t\t ","="*40)
print("\t\tInputan Jumlah Perkalian Dengan Rata-Ratanya")
print("\n")
n = int(input("\t\tMasukkan jumlah nilai yang ingin dijumlah: "))

total = 0

for i in range(n):
    nilai = int(input(f"\t\tMasukkan nilai ke {i+1}: "))
    total += nilai

rata_rata = total / n
print("\t\t","="*35)
print(f"\t\tjumlah total nilai: {round(total)}")
print(f"\t\tRata-rata nilai: {round(rata_rata)}")