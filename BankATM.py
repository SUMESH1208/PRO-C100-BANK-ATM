balance = 50000

class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

 

    def check_balance(self):
        print(balance)

    def withdrawl(self,amount):
        new_amount = balance - amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))

    def deposit(self,depositing_amount):
        print("You have deposited - " + str(depositing_amount) + " .Your new balance is " + str(balance + depositing_amount) )


def main():
    Card_number = input("insert your card number:- ")
    pin_number  = input("enter your pin number:- ")

    new_user =  Atm(Card_number ,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdrawl  3.Deposit")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount that you need to withdraw:- "))
        new_user.withdrawl(amount)
    elif (activity == 3):
        depositing_amount = int(input("Enter the amount you want to deposit:- "))
        new_user.deposit(depositing_amount)

    else:
        print("enter a valid number")

if __name__ == "__main__":
    main()