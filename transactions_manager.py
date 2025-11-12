from utils import read_json, write_json, now_iso
from config import TRANSACTIONS_FILE
from products_manager import list_products, save_products, find_product_by_id, view_all_products
from datetime import datetime

def list_transactions():
    return read_json(TRANSACTIONS_FILE)

def save_transactions(txns):
    write_json(TRANSACTIONS_FILE, txns)

def generate_transaction_id(txns):
    if not txns:
        return 1
    return max(t["id"] for t in txns) + 1

def sell_product(logged_user):
    products = list_products()
    if not products:
        print("Tidak ada produk untuk dijual.")
        return

    view_all_products()

    try:
        pid = int(input("Masukkan ID produk yang dibeli: ").strip())
        qty = int(input("Masukkan jumlah beli: ").strip())
    except ValueError:
        print("Input tidak valid.")
        return

    p = find_product_by_id(pid)

    if not p:
        print("Produk tidak ditemukan.")
        return

    if qty <= 0:
        print("Jumlah harus > 0.")
        return

    if p["stok"] < qty:
        print(f"Stok tidak cukup. Stok sekarang: {p['stok']}")
        return

    total = qty * p["harga_jual"]
    profit = qty * (p["harga_jual"] - p["harga_modal"])

    p["stok"] -= qty
    save_products(products)

    txns = list_transactions()
    tid = generate_transaction_id(txns)

    txn = {
        "id": tid,
        "time": now_iso(),
        "product_id": p["id"],
        "product_name": p["name"],
        "qty": qty,
        "total": round(total, 2),
        "profit": round(profit, 2),
        "cashier": logged_user["username"]
    }
    txns.append(txn)
    save_transactions(txns)

    print("=== Transaksi Sukses ===")
    print(f"Produk: {p['name']}")
    print(f"Jumlah: {qty}")
    print(f"Total harga: Rp {total:.2f}")
    print(f"Profit transaksi: Rp {profit:.2f}")
    print(f"Stok tersisa: {p["stok"]}")


