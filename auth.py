from utils import read_json
from config import USERS_FILE

def login(role_expected):
    users = read_json(USERS_FILE)
    print(f"\n=== Login sebagai {role_expected} ===")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    for u in users:
        if u["username"] == username and u["password"] == password and u["role"].lower() == role_expected.lower():
            print(f"Login sukses sebagai {role_expected}.")
            return u

    print("Login gagal: username/password/role salah.")
    return None