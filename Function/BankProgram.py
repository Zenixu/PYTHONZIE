#python bank
def tunjukan_saldo(saldo):
    print("*********************")
    print(f"Isi saldo kamu Rp.{saldo:.3f}")
    print("*********************")
def setoran():
    print("*********************")
    amount = float(input("Masukkan jumlah yang akan disetorkan: "))
    print("*********************")
    if amount < 0:
        print("*********************")
        print("Itu bukan jumlah yang valid")
        print("*********************")
    else:
        return amount

def menarik(saldo):
    print("*********************")
    amount = float(input("Masukkan jumlah yang akan di tarik"))
    print("*********************")
    if amount > saldo:
        print("*********************")
        print("Dana tidak mencukupi")
        print("*********************")
        return 0
    elif amount < 0:
        print("*********************")
        print("jumlah harus lebih besar dari 0")
        print("*********************")
        return 0
    else:
        return amount

def main():
    saldo = 0
    is_running = True

    while is_running:
        print("*********************")
        print("     Bank Program    ")
        print("*********************")
        print("1.Tunjukan Saldo")
        print("2.Setoran")
        print("3.Menarik")
        print("4.Keluar")
        print("*********************")
        choice = input("Ketik Pilihanmu(1-4): ")

        if choice == '1':
            tunjukan_saldo(saldo)
        elif choice == '2':
            saldo +=setoran()
        elif choice == '3':
            saldo -=menarik(saldo)
        elif choice == '4':
            is_running  = False
        else:
            print("*********************")
            print("pilihan ini tidak valid")
            print("*********************")
    print("*********************")
    print("Makasih kang udah datang dibank")
    print("*********************")
    
if __name__ == '__main__':
    main()