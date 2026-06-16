class BankAccount:
    # Class Attributes
    bank_name = "Vietcombank"
    transaction_fee = 2000

    def __init__(self, account_number, account_name):
        self.account_number = account_number
        self.__balance = 0
        self.__account_name = ""
        self.account_name = account_name  # gọi setter
    @property
    def balance(self):
        return self.__balance
    @property
    def account_name(self):
        return self.__account_name

    @account_name.setter
    def account_name(self, new_name):
        new_name = new_name.strip()

        if not new_name:
            print("Tên tài khoản không được để trống")
            return

        self.__account_name = new_name.upper()
    @staticmethod
    def validate_account_number(account_number):
        return account_number.isdigit() and len(account_number) == 10
    @classmethod
    def update_transaction_fee(cls, new_fee):
        cls.transaction_fee = new_fee
    def deposit(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False

        self.__balance += amount
        print(f"Nạp tiền thành công: +{amount:,} VND")
        return True
    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False
        total = amount + BankAccount.transaction_fee
        if self.__balance < total:
            print(
                "Giao dịch thất bại. Số dư không đủ để thanh toán số tiền và phí giao dịch")
            return False
        self.__balance -= total
        print(f"Rút tiền thành công: -{amount:,} VND")
        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")
        return True
    def display_info(self):
        print("\n--- THÔNG TIN TÀI KHOẢN ---")
        print(f"Ngân hàng: {BankAccount.bank_name}")
        print(f"Số tài khoản: {self.account_number}")
        print(f"Tên chủ tài khoản: {self.account_name}")
        print(f"Số dư hiện tại: {self.balance:,} VND")
        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")


def main():
    current_account = None

    while True:
        choice = input("""
===== VIETCOMBANK DIGIBANK SIMULATOR =====
1. Mở tài khoản mới
2. Xem thông tin tài khoản
3. Giao dịch Nạp / Rút tiền
4. Cập nhật Tên chủ tài khoản
5. Đổi phí giao dịch hệ thống
6. Thoát chương trình
==========================================
Chọn chức năng (1-6): """)

        match choice:
            case "1":
                print("\n--- MỞ TÀI KHOẢN MỚI ---")
                while True:
                    account_number = input(
                        "Nhập số tài khoản 10 chữ số: ")
                    if BankAccount.validate_account_number(
                            account_number):
                        break
                    print("Số tài khoản không hợp lệ!")
                    print("Số tài khoản phải gồm đúng 10 chữ số.")
                account_name = input(
                    "Nhập tên chủ tài khoản: "
                )
                current_account = BankAccount(
                    account_number,
                    account_name
                )
                print("Mở tài khoản thành công!")
                print(
                    f"Số tài khoản: {current_account.account_number}"
                )
                print(
                    f"Tên chủ tài khoản: {current_account.account_name}"
                )
            case "2":
                if current_account is None:
                    print(
                        "Hệ thống chưa có thông tin tài khoản"
                    )
                    print(
                        "Vui lòng mở tài khoản ở Chức năng 1 trước."
                    )
                else:
                    current_account.display_info()
            case "3":
                if current_account is None:
                    print(
                        "Hệ thống chưa có thông tin tài khoản"
                    )
                    continue

                print("\n--- GIAO DỊCH NẠP / RÚT TIỀN ---")
                print("1. Nạp tiền")
                print("2. Rút tiền")

                action = input(
                    "Chọn loại giao dịch (1-2): "
                )

                try:
                    amount = int(
                        input(
                            "Nhập số tiền giao dịch: "
                        )
                    )

                    if action == "1":
                        current_account.deposit(amount)

                    elif action == "2":
                        current_account.withdraw(amount)

                    else:
                        print("Lựa chọn không hợp lệ")

                    print(
                        f"Số dư mới: {current_account.balance:,} VND"
                    )

                except ValueError:
                    print(
                        "Vui lòng nhập số tiền hợp lệ"
                    )
            case "4":
                if current_account is None:
                    print(
                        "Hệ thống chưa có thông tin tài khoản"
                    )
                    continue

                print(
                    "\n--- CẬP NHẬT TÊN CHỦ TÀI KHOẢN ---"
                )

                old_name = current_account.account_name

                new_name = input("Nhập tên mới: ")

                current_account.account_name = new_name

                if current_account.account_name != old_name:
                    print(
                        f"Cập nhật thành công. Tên mới: {current_account.account_name}"
                    )
            case "5":
                print(
                    "\n--- ĐỔI PHÍ GIAO DỊCH HỆ THỐNG ---"
                )

                print(
                    f"Phí giao dịch hiện tại: {BankAccount.transaction_fee:,} VND"
                )

                try:
                    new_fee = int(
                        input(
                            "Nhập phí giao dịch mới: "
                        )
                    )

                    if new_fee < 0:
                        print(
                            "Phí giao dịch không được âm"
                        )
                        print(
                            f"Phí giao dịch hiện tại vẫn là {BankAccount.transaction_fee:,} VND"
                        )
                    else:
                        BankAccount.update_transaction_fee(
                            new_fee
                        )

                        print(
                            f"Đã cập nhật phí giao dịch toàn hệ thống thành {BankAccount.transaction_fee:,} VND"
                        )

                except ValueError:
                    print( "Phí giao dịch không hợp lệ")
            case "6":
                print( "Cảm ơn bạn đã sử dụng Vietcombank Digibank!")
                break
            case _:
                print("Vui lòng chọn từ 1 đến 6")
if __name__ == "__main__":
    main()