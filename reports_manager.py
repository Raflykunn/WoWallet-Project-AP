from utils import read_json
from config import LOW_STOCK_THRESHOLD
from transactions_manager import list_transactions
from products_manager import list_products
from datetime import datetime, date, timedelta
from collections import defaultdict, Counter

def total_profit_all_time():
    txns = list_transactions()
    return sum(t["profit"] for t in txns)

def total_transactions_today():
    txns = list_transactions()
    today = date.today()
    return sum(1 for t in txns if datetime.fromisoformat(t["time"]).date() == today)

def most_sold_products_last_days(days=7, top_n=3):
    txns = list_transactions()
    cutoff = datetime.now() - timedelta(days=days)
    counter = Counter()
    for t in txns:
        if datetime.fromisoformat(t["time"]) >= cutoff:
            counter[t["product_name"]] += t["qty"]
    return counter.most_common(top_n)

def print_low_stock():
    products = list_products()
    low = [p for p in products if p["stok"] < LOW_STOCK_THRESHOLD]
    if low:
        print("Produk menipis (stok < 5):")
        for p in low:
            print(f" - {p['name']} (stok {p['stok']})")
    else:
        print("Tidak ada produk menipis.")

def product_with_smallest_total_profit():
    txns = list_transactions()
    if not txns:
        return None

    profit_by_product = defaultdict(float)
    for t in txns:
        profit_by_product[t["product_name"]] += t["profit"]

    smallest_profit_product = None
    min_profit = float('inf')

    for product_name, profit in profit_by_product.items():
        if profit < min_profit:
            min_profit = profit
            smallest_profit_product = (product_name, profit)
            
    return smallest_profit_product

def dashboard():
    print("\n=== DASHBOARD ===")
    print(f"Total profit semua waktu: Rp {total_profit_all_time():.2f}")
    print(f"Total transaksi hari ini: {total_transactions_today()}")
    print_low_stock()
    top_weekly = most_sold_products_last_days()
    print("Produk paling laris minggu ini:")
    for name, cnt in top_weekly:
        print(f" - {name}: {cnt} terjual")

    smallest = product_with_smallest_total_profit()
    if smallest:
        print(f"Produk dengan total profit terkecil: {smallest[0]} (Rp {smallest[1]:.2f})")
    print("=================\n")


