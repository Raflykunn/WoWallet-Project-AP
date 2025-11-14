from utils import ensure_data_files
from auth import login
from menus import admin_menu, kasir_menu

def main():
    ensure_data_files()
    print("=== Selamat Datang di WoWallet ===")
    while True:
        print("\nPilih jenis login:")
        print("1. Login sebagai Admin")
        print("2. Login sebagai Kasir")
        print("0. Keluar")
        opt = input("Pilih: ").strip()

        if opt == "1":
            user = login("Admin")
            if user:
                admin_menu(user)
        elif opt == "2":
            user = login("Kasir")
            if user:
                kasir_menu(user)
        elif opt == "0":
            print("Keluar dari aplikasi. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Tolong masukkan 1 atau 2.")

if __name__ == "__main__":
    main()