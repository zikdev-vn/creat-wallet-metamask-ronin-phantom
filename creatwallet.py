from nacl.signing import SigningKey
from base58 import b58encode
from eth_account import Account
import os

def create_phantom_wallets(num_wallets):
    wallets = []
    for i in range(num_wallets):
        signing_key = SigningKey.generate()
        verify_key = signing_key.verify_key

        public_key = b58encode(verify_key.encode()).decode('utf-8')
        private_key = b58encode(signing_key.encode()).decode('utf-8')

        wallets.append({
            'public_key': public_key,
            'private_key': private_key
        })
    return wallets

def create_metamask_wallets(num_wallets):
    wallets = []
    for i in range(num_wallets):
        account = Account.create()
        public_key = account.address
        private_key = account.key.hex()

        wallets.append({
            'public_key': public_key,
            'private_key': private_key
        })
    return wallets

def create_ronin_wallets(num_wallets):
    wallets = []
    for i in range(num_wallets):
        account = Account.create()
        address = account.address.replace('0x', 'ronin:')
        private_key = account.key.hex()

        wallets.append({
            'public_key': address,
            'private_key': private_key
        })
    return wallets

def save_wallets_to_file(wallets, wallet_type):
    filename = f"{wallet_type}_wallets.txt"
    with open(filename, "w", encoding="utf-8") as file:
        for i, wallet in enumerate(wallets):
            file.write(f"Ví {i+1}:\n")
            file.write(f"  Khóa công khai (Public Key): {wallet['public_key']}\n")
            file.write(f"  Khóa riêng tư (Private Key): {wallet['private_key']}\n")
            file.write("\n")
    print(f"Thông tin các ví đã được lưu vào tệp {filename}")

def main():
    print("Chọn loại ví muốn tạo:")
    print("1. Phantom")
    print("2. MetaMask")
    print("3. Ronin")

    choice = input("Nhập lựa chọn của bạn (1, 2, 3): ")
    num_wallets = int(input("Nhập số lượng ví muốn tạo: "))

    if choice == '1':
        wallets = create_phantom_wallets(num_wallets)
        save_wallets_to_file(wallets, "phantom")
    elif choice == '2':
        wallets = create_metamask_wallets(num_wallets)
        save_wallets_to_file(wallets, "metamask")
    elif choice == '3':
        wallets = create_ronin_wallets(num_wallets)
        save_wallets_to_file(wallets, "ronin")
    else:
        print("Lựa chọn không hợp lệ")

if __name__ == "__main__":
    main()
