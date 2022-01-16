from atexit import register
from banking_pkg import account


def atm_menu(name):

    print("")
    print("          === Automated Teller Machine ===          \n")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

# Task 2 - Registration


print("          === Automated Teller Machine ===          \n")

while True:

    name = input("Enter name to register: ")
    if len(name) > 10:
        print("The maximum length is 10 characters. Please try again.")
    elif len(name) == 0:
        print("You must enter a name. Please try again.")
    else:
        break

while True:
    pin = input("Enter PIN: ")
    if len(pin) < 4 or len(pin) > 4:
        print("PIN must contain 4 numbers.  Please try again.")
    else:
        break

print(f"{name} has been registered with a starting balance of $0.0\n")


# Task 3 - Log in and prompt for menu option

print("          === Automated Teller Machine ===          \n")

while True:
    print("LOGIN")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login sucessful!")
        break
    else:
        print("Invalid credentials!")

balance = float(0)

while True:

    atm_menu(name)
    option = int(input("Choose an option: "))
    # Task 4 - Using the banking package
    if option == 1:
        account.show_balance(balance)
    elif option == 2:
        balance = account.deposit(balance)
        print(f"Your current balance is:${balance:.2f} ")
    elif option == 3:
        balance = account.withdraw(balance)
        print(f"Your current balance is:${balance:.2f} ")
    else:
        account.logout(name)
        break
