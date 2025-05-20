'''
A command-line tool to hide, unhide, and password-protect files 👀🔐

Perfect mix of:

Python + OS interaction

Basic security logic

Practical daily use

🎯 What It Can Do:
🔑 Set a password

📁 Add files to vault (it "hides" them)

🔓 Unlock (show) hidden files after entering the correct password

❌ Lock again

'''

import os
import getpass

VAULT_DIR = "vault"
PASSWORD = "tamashii"  # You can enhance with secure storage

def setup():
    if not os.path.exists(VAULT_DIR):
        os.makedirs(VAULT_DIR)
    print("🔐 File Vault Initialized.")

def add_file():
    file_path = input("Enter full path of file to vault: ")
    if os.path.exists(file_path):
        os.rename(file_path, os.path.join(VAULT_DIR, os.path.basename(file_path)))
        print("✅ File moved to vault.")
    else:
        print("❌ File not found.")

def list_files():
    files = os.listdir(VAULT_DIR)
    if files:
        print("🔐 Vault contains:")
        for f in files:
            print(" -", f)
    else:
        print("🕸️ Vault is empty.")

def unlock_vault():
    entered = getpass.getpass("Enter password to unlock vault: ")
    if entered == PASSWORD:
        files = os.listdir(VAULT_DIR)
        if not files:
            print("Vault is empty.")
            return
        for f in files:
            dest_path = os.path.join(os.getcwd(), f)
            os.rename(os.path.join(VAULT_DIR, f), dest_path)
        print("🔓 Vault unlocked. Files restored.")
    else:
        print("❌ Incorrect password.")

def show_menu():
    print("\n🔐 File Vault Menu:")
    print("1. Add File to Vault")
    print("2. View Vaulted Files")
    print("3. Unlock Vault")
    print("4. Exit")

def main():
    setup()
    while True:
        show_menu()
        choice = input("Choose: ")

        if choice == "1":
            add_file()
        elif choice == "2":
            list_files()
        elif choice == "3":
            unlock_vault()
        elif choice == "4":
            print("Bye Bye, Tamashii Warrior ⚔️")
            break
        else:
            print("❗ Invalid choice")

if __name__ == "__main__":
    main()
