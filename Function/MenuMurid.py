murid = []

def lihat_nama():
    if len(murid) == 0:
        print("\t\tTidak ada data Murid.")
    else:
        print('\t','='*45)
        print('\t\t\tDaftar Nama Murid')
        print('\t','='*45)
        for i, nama in enumerate(murid):
            print(f"\t {i+1}. {nama}")

def tambah_nama():
    print()
    murid_baru = str(input("Masukkan nama Murid baru: "))
    if murid_baru in murid:
        print('Nama udah ada coba masukkan nama lain')
    else:
        murid.append(murid_baru)
        print(f"Nama {murid_baru} telah ditambahkan.")

def edit_nama():
    lihat_nama()
    print()
    indeks = int(input("Masukkan nama Murid yang ingin diedit: ")) - 1
    if 0 <= indeks < len(murid):
        murid_baru = input("Masukkan nama baru: ")
        murid[indeks] = murid_baru
        print("Nama Murid berhasil diedit.")
    else:
        print("Indeks tidak valid")

def hapus_nama():
    print()
    lihat_nama()
    indeks = int(input("Masukkan nama murid yang ingin dihapus: ")) - 1
    if 0 <= indeks < len(murid):
        murid.pop(indeks)
        print("Nama murid berhasil dihapus.")
    else:
        print("Indeks tidak valid")

def cari_nama():
    print()
    nama_cari = str(input("Masukkan nama murid yang ingin dicari: "))
    if nama_cari in murid:
        print(f"Nama {nama_cari} ditemukan.")
    else:
        print("Nama tidak ditemukan.")

def menu():
    print('\n')
    print('\t','='*40)
    print('\t\t\tMain Menu')
    print('\t','='*40)
    print()

    daftar_menu = [
        'Liat',
        'Tambah',
        'Edit',
        'Hapus',
        'Cari',
        'Keluar'
    ]

    i = 1
    for data in daftar_menu:
        print('\t',i,':', data)
        i = i + 1
    print()

    pilihan = int(input("Pilih menu (1/6): "))
    print()

    if pilihan == 1:
        lihat_nama()
    elif pilihan == 2:
        tambah_nama()
    elif pilihan == 3:
        edit_nama()
    elif pilihan == 4:
        hapus_nama()
    elif pilihan == 5:
        cari_nama()
    elif pilihan == 6:
        print("Hatur Nuhun")
        exit()
    else:
        print("Pilihan tidak Ada.")

while True:
    menu()