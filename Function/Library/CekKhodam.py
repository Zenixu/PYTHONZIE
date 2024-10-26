import random
import tkinter as tk

def generate_khodam():
    nama = entry.get()
    kata1 = ["Naga", 'Kuda', 'Gajah', 'Singa', 'Harimau', 'Tapir', "Monyet", 'Kucing', 'T-Rex', "Semut", 'Pohon', 'Kudanil', 'Kuman', 'Kelapa', 'Kutu', 'Buaya', 'Koala', 'Panda']
    kata2 = ['Kawin', 'Hamil', 'Ngesot', 'Melahirkan', 'Ngoding', 'Main Catur', 'Raja Judi', 'Pembalap', 'Roblox', 'Kayang', 'Ngaji', 'Umroh', 'Bakar', 'Rebus', 'Nge GYM', 'Gamers', 'Dagang']
    result = f"Khodam {nama} adalah {random.choice(kata1)} {random.choice(kata2)}"
    result_label.config(text=result)

root = tk.Tk()
root.title("Khodam Generator")
root.geometry("500x250")
root.configure(bg="grey")

entry_label = tk.Label(root, text="Masukkan nama yang ingin di cek:")
entry_label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Cek", command=generate_khodam)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=('Arial', 12))
result_label.pack(pady=10)
result_label.configure(bg="pink")


root.mainloop()
