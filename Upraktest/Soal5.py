#buatlah program dengan suatu pertanyaan dengan dengan hasil
import os
os.system('cls')
print("Berapa hasil pertambahan 4 * 50")
jawaban = ["A. 100", 
            "B. 200", 
            "C. 50",
            "D. 75",
            "E. 80"]
kunci1 = jawaban[1]
for i in jawaban:
    print(i, end=" ")
print()
nama = str(input("masukkan jawaban(A/B/C/D/E): ")).upper()

if nama == "B":
    print (f"Jawaban anda benar")
else:
    print (f"jawaban anda salah jawaban yang benar adalah {kunci1}")
print()