print('\n')
print('='*30)
print('Menghitung frekuensi getaran')
print('='*30)
print()

t = int(input('Masukan lama waktu : '))
n = int(input('Masukan jumlah getaran : '))
F = lambda t, n : n / t

print(f'Frekuensi getaran adalah : {F(t,n)} Hz')