balance = 0
valid_options = (1, 2, 3, 4)

print("-------------------------------")
print("Welcome to your Bank!")
print("-------------------------------")

while True:

    while True:
        try:
            print("Please select an option:")
            print("1. Show Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            print("-------------------------------")
            option = int(input("Enter here: "))
            if option in valid_options:
                break
            else:
                print("Please enter a valid option (1-4).")
        except ValueError:
            print("Please enter a number.")

    if option == 1:
        print("-------------------------------")
        print(f"Your balance is currently: £{balance:.2f}")
        print("-------------------------------")
        continue

    elif option == 2:

        while True:
            deposit_amount = input("How much would you like to deposit? £")
            deposit_transactions.append(deposit_amount)
            try:
                deposit_amount = float(deposit_amount)
                if deposit_amount <= 0:
                    print("Please enter a valid number.")
                    continue
                break
            except ValueError:
                print("Please enter a number.")
                continue

        balance += deposit_amount
        print("-------------------------------")
        print(f"You have deposited £{deposit_amount:.2f}")
        print("-------------------------------")
        print(f"Your updated balance is now: £{balance:.2f}")
        print("-------------------------------")
        continue


    elif option == 3:

        if balance == 0:
            print("Error! You have £0 in your account. Please deposit funds before you can withdraw.")
            continue

        while True:
            withdraw_amount = input(f"Your current balance is £{balance:.2f}. How much would you like to withdraw? £")
            withdraw_transactions.append(withdraw_amount)
            try:
                withdraw_amount = float(withdraw_amount)
                if withdraw_amount < 0:
                    print("Please enter a valid number.")
                    continue
                elif withdraw_amount > balance:
                    print("You do not have enough in your account.")
                    continue
                elif withdraw_amount == 0:
                    print("Nothing withdrawn.")
                    break

                balance -= withdraw_amount
                print(f"You have chosen to withdraw £{withdraw_amount:.2f}.")
                print("-------------------------------")
                print(f"Your updated balance is now £{balance:.2f}.")
                print("-------------------------------")
                break

            except ValueError:
                print("Please enter a number.")
                continue

    elif option == 4:
        break

print("-------------------------------")
print("Thank you for visiting, come again soon.")
print("-------------------------------")
