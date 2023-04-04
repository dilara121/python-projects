from time import time


import time
card_password = 5687
right_of_entry = 2
total_balance = 1500

while True:
    password = int(input("Enter password : "))
    time.sleep(2)
    if card_password == password:
        print("Your password is right. Welcome to the system...")
        
        while True:
            print("1)Deposit\n"
                  "2)Withdraw\n"
                  "3)Money Transfer\n"
                  "4)Balance\n")
            transaction = int(input("Enter the transaction number: "))
            time.sleep(3)
            if islem == 1:
                amount_determination = int(input("Amount Determination: "))
                print("Put the money in ATM\nAmount Determination  {}\n".format(amount_determination))
                new_balance = total_balance + amount_determination
                print("New balance : {} $".format(new_balance))
                a = input("Press the 'Q' key to exit the ATM and the 'X' key to return to the transaction menu: ")
                if a == 'Q':
                    print("Leaving the ATM. Have a nice day. We hope you come again...")
                    break
                elif a == 'X':
                    continue
            if transaction == 2:
                amount_withdrawn = int(input("Enter the amount you want to withdraw: "))
                if total_balance - amount_withdrawn < 0:
                    print("You cannot withdraw that much money....")
                else:
                    print("Your transaction is being processed...\nGet your money.\nAmount withdrawn {}' $".format(
                        amount_withdrawn))
                available_balance = total_balance - amount_withdrawn
                if available_balance >= 0:
                    print("Available balance : {} $".format(available_balance))
                else:
                    print("Total Balance : {} TL".format(total_balance))
                a = input("Press the 'Q' key to exit the ATM and the 'X' key to return to the transaction menu: ")
                if a == 'Q':
                    print("Leaving the ATM. Have a nice day. We hope you come again...")
                    break
                elif a == 'X':
                    continue
            if transaction == 3:
                i_ban = input("Enter the IBAN number of the account you want to transfer money to.: ")
                amount_transferred = int(input("Enter the amount you want to transfer: "))
                print("Your transaction is being processed...")
                available_balance = total_balance - amount_transferred
                print("Available balance : {}$".format(available_balance))
                a = input("Press the 'Q' key to exit the ATM and the 'X' key to return to the transaction menu: ")
                if a == 'Q':
                    print("Leaving the ATM. Have a nice day. We hope you come again...")
                    break
                elif a == 'X':
                    continue
            if transaction == 4:
                print("Total Balance {}' $ ".format(total_balance))
        break
    else:
        print("Your password is wrong. You have {} login left.".format(giris_hakki))
        right_of_entry -= 1
    if right_of_entry >= 0:
        continue
    print("You have used all your access rights. Your card has been blocked. You can make it available again from the nearest branch. HAVE NICE DAY... ")
    break
