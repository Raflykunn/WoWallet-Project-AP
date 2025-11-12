from products_manager import add_product, view_all_products, edit_product, delete_product, input_stock_masuk
from transactions_manager import sell_product
from reports_manager import dashboard

def admin_menu(user):
    while True:
        print("\n--- MENU ADMIN ---")
        print("1. Tambah Produk")
        print("2. Lihat Semua Produk")
        print("3. Edit Produk")
        print("4. Hapus Produk")
        print("5. Input Stok Masuk")
        print("6. Transaksi Penjualan")
        print("7. Dashboard")
        print("0. Logout")
        choice = input("Pilih: ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            view_all_products()
        elif choice == "3":
            edit_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            input_stock_masuk()
        elif choice == "6":
            sell_product(user)
        elif choice == "7":
            dashboard()
        elif choice == "0":
            print("Logout...")
            break
        else:
            print("Pilihan tidak valid.")

def kasir_menu(user):
    while True:
        print("\n--- MENU KASIR ---")
        print("1. Transaksi Penjualan")
        print("2. Lihat Semua Produk")
        print("3. Dashboard Ringkas")
        print("0. Logout")
        choice = input("Pilih: ").strip()

        if choice == "1":
            sell_product(user)
        elif choice == "2":
            view_all_products()
        elif choice == "3":
            dashboard()
        elif choice == "0":
            print("Logout...")
            break
        else:
            print("Pilihan tidak valid.")