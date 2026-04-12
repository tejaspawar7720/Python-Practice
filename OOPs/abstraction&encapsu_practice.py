class Bank:
    

    def __init__(self):
        balance = 15000
        account_no = 145648154
        self.debit = False
        self.credit = False
        
        
    def debit(self):
        self.debited = self.balance - amount_to_debit
        print("Total amount debit from account no: ", self.account_no, "is ",self.debited)
    
    def credit(self):
        self.credited = amount_to_credit + self.balance
        print("Total amount debit from account no: ", self.account_no, "is ", self.credited )

    def total_balance(self):
        self.tb = self.balance

s1 = Bank()

sum = input("Select Debit or Credit or Bank Balance: ")

if sum == "Debit" or "debit":
    amount_to_debit = int(input("Enter amount to Debit: "))
    print(s1.debited)
elif sum == "Credit" or "credit":
    amount_to_credit = int(input("Enter Amount to credit: "))
    print(s1.credited)
else:
    print("Your total balance is: ", s1.total_balance)



        
