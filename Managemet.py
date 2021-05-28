"""
This program works as an ATM management
Assume that balance money as 100000
"""
balance_money = 100000
deposit_money = 0
withdraw_money = 0

def validate_card():
    """This function validate the inserted card """
    print("Please insert your card")
    card = int(input("Please enter 1 if you entered your card"))
    return card


def validate_pin():
    """This function validate the pin entered by the user"""
    print("Please enter your 4 digits pin")
    pin_list = []
    pin_list2 = []
    for i in range(4):
        pin = int(input())
        pin_list.append(pin)
    print("Please re-enter your pin to confirm")
    for i in range(4):
        pin = int(input())
        pin_list2.append(pin)
    set1 = set(pin_list)
    set2 = set(pin_list2)
    if set1 == set2:
        print("Validating pin completed")
        return 1
    print("Validating pin failed")
    return 0


def cash_withdrawal(amt):
    """This function used for cash withdrawal
    and update the balance accordingly
    """
    global withdraw_money
    global balance_money
    withdraw_money = amt
    print("Amout enetered : ", withdraw_money)
    balance_money = balance_money - withdraw_money
    print("Withdraw success")


def balance_money_check():
    """This function print the balance in that account"""
    print(balance_money)


def deposit_money_check(amt):
    """This function works to deposit money
    and change the balance amount accordingly
    """
    global balance_money
    print("Deposit money is : ", amt)
    balance_money = balance_money + amt


print("Wlecome To ATM Machine")
ret = validate_card()
if ret == 1:
    print("Validating card success")
else:
    flow_flag = 0
    print("Validating card failed")
    exit()
    ret = validate_pin()
    if ret == 1:
        print("Validating pin completed")
    else:
        flow_flag = 0
        print("Validating pin failed")
while 1:
    print("Select the option")
    print("1: Withdraw Money")
    print("2. Check your Balance")
    print("3. Deposit Money")
    option = int(input())
    if 1 == option:
        amt = int(input("Enter the Amount to withdraw"))
        cash_withdrawal(amt)
        print("Press 1 if u want to go back to menu & 0 to exit")
        val = int(input())
        if 1 == val:
            continue
        else:
            exit()
    elif 2 == option:
        balance_money_check()
        print("Press 1 if u want to go back to menu & 0 to exit")
        val = int(input())
        if 1 == val:
            continue
        else:
            exit()
    elif 3 == option:
        amt = int(input("Enter the Amount to deposit"))
        deposit_money_check(amt)
        print("Press 1 if u want to go back to menu & 0 to exit")
        val = int(input())
        if 1 == val:
            continue
        else:
            exit()
    else:
        print("Invalid option")
        print("Press 1 if u want to go back to menu & 0 to exit")
        val = int(input())
        if 1 == val:
            continue
        else:
            exit()

    exit()
