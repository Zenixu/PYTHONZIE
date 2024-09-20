n = int(input("Masukkan Jumlah Perkalian: "))
for i in range (1, n+1):
    print(f"1 x {i} = {1*i}     2 x {i} = {2*i}")

print("="*40)

n = int(input("\nMasukkan jumlah nilai yang ingin dijumlah: "))

total = 0

for i in range(n):
    nilai = int(input(f"Masukkan nilai ke {i+1}: "))
    total += nilai

rata_rata = total / n
print("="*35)
print(f"jumlah total nilai: {round(total)}")
print(f"Rata-rata nilai: {round(rata_rata)}")

print("="*40)

n = int(input("Masukkan Jumlah Perkalian: "))

print("   *", end=" ")
for i in range(1, n+1):
    print(f"{i:4}", end=" ")
print()

print("  ", end="")
print("_____" * (n+1))

for i in range(1, n+1):
    print(f"{i:3} |", end=" ")

    for z in range(1, n+1):
        print(f"{i*z:4}", end=" ")
    print()