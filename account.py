# Task 4 - The banking package

def show_balance(balance):
    print(f"Your balance is: ${balance:.2f}")


def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    return amount + balance


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if balance < amount:
        print("Where are you going to get that kind of money?")
        print(f"Current balance:${balance:.2f}")
        return balance
    else:
        return balance - amount


def logout(name):
    print(f"Goodbye {name}!")
