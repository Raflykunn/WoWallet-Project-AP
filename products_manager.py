from utils import read_json, write_json, now_iso
from config import PRODUCTS_FILE
from datetime import datetime

def list_products():
    return read_json(PRODUCTS_FILE)

def save_products(products):
    write_json(PRODUCTS_FILE, products)

def get_next_product_id(products):
    if not products:
        return 1
    return max(p["id"] for p in products) + 1

def add_product():
    products = list_products()
    pid = get_next_product_id(products)
    name = input("Nama produk: ").strip()
    try:
        harga_modal = float(input("Harga modal: ").strip())
        harga_jual = float(input("Harga jual: ").strip())
        stok = int(input("Stok awal: ").strip())
    except ValueError:
        print("Input angka tidak valid. Tolong isi dengan benar.")
        return

    product = {
        "id": pid,
        "name": name,
        "harga_modal": harga_modal,
        "harga_jual": harga_jual,
        "stok": stok,
        "created_at": now_iso()
    }
    products.append(product)
    save_products(products)
    print(f"Produk ditambahkan: {product['name']}")

def view_all_products():
    products = list_products()
    if not products:
        print("Belum ada produk.")
        return

    print("\nDaftar Produk:")

    col_id = 4
    col_name = 20
    col_modal = 10
    col_jual = 10
    col_stok = 8

    header = ["ID", "Nama", "Modal", "Jual", "Stok"]
    header_format = f"| {{:<{col_id}}} | {{:<{col_name}}} | {{:>{col_modal}}} | {{:>{col_jual}}} | {{:>{col_stok}}} |"

    separator = "+" + "-" * (col_id + 2) + "+" + "-" * (col_name + 2) + "+" + "-" * (col_modal + 2) + "+" + "-" * (col_jual + 2) + "+" + "-" * (col_stok + 2) + "+"

    print(separator)
    print(header_format.format(*header))
    print(separator)

    for p in products:
        print(f"| {{:<{col_id}}} | {{:<{col_name}}} | {{:>{col_modal}.2f}} | {{:>{col_jual}.2f}} | {{:>{col_stok}}} |".format(p["id"], p["name"], p["harga_modal"], p["harga_jual"], p["stok"]))
    print(separator)
    print()

def find_product_by_id(pid):
    products = list_products()
    for p in products:
        if p["id"] == pid:
            return p
    return None

def edit_product():
    products = list_products()
    try:
        pid = int(input("Masukkan ID produk yang ingin di-edit: ").strip())
    except ValueError:
        print("ID tidak valid.")
        return

    found_product = None
    for p in products:
        if p["id"] == pid:
            found_product = p
            break
    else:
        print("Produk tidak ditemukan.")
        return

    print("Biarkan kosong jika tidak ingin mengubah field tersebut.")

    new_name = input(f"Nama ({found_product['name']}): ").strip()
    new_harga_modal = input(f"Harga modal ({found_product['harga_modal']}): ").strip()
    new_harga_jual = input(f"Harga jual ({found_product['harga_jual']}): ").strip()
    new_stok = input(f"Stok ({found_product['stok']}): ").strip()

    if new_name:
        found_product["name"] = new_name
    if new_harga_modal:
        try:
            found_product["harga_modal"] = float(new_harga_modal)
        except ValueError:
            print("Harga modal tidak valid; tidak diubah.")
    if new_harga_jual:
        try:
            found_product["harga_jual"] = float(new_harga_jual)
        except ValueError:
            print("Harga jual tidak valid; tidak diubah.")
    if new_stok:
        try:
            found_product["stok"] = int(new_stok)
        except ValueError:
            print("Stok tidak valid; tidak diubah.")

    save_products(products)
    print("Produk berhasil diupdate.")

def delete_product():
    products = list_products()
    try:
        pid = int(input("Masukkan ID produk yang ingin dihapus: ").strip())
    except ValueError:
        print("ID tidak valid.")
        return

    products = [p for p in products if p["id"] != pid]
    save_products(products)
    print("Produk dihapus (jika ID ada).")

def input_stock_masuk():
    products = list_products()
    try:
        pid = int(input("Masukkan ID produk untuk stok masuk: ").strip())
        qty = int(input("Jumlah stok masuk: ").strip())
    except ValueError:
        print("Input tidak valid.")
        return

    for p in products:
        if p["id"] == pid:
            p["stok"] += qty
            save_products(products)
            print(f"Stok produk {p['name']} bertambah {qty}. Stok sekarang: {p['stok']}")
            return

    print("Produk tidak ditemukan.")