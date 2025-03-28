from Банк import BankAccount


def get_out():
    return False


def play_with_bank():
    bank_account = BankAccount()
    main_menu = {
        "1": lambda: bank_account.check_balance(),
        "2": lambda: bank_account.add_to_balance(),
        "3": lambda: bank_account.withdraw()
    }

    flag = True
    while flag:
        option = input("1. Посмотреть баланс\n2. Внести\n3. Снять\n4. Выход\nВаш выбор: ")
        if option == "4":
            flag = get_out()
        elif option in main_menu:
            main_menu[option]()
        else:
            print("Такого в меню нет.")


play_with_bank()
