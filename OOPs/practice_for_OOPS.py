class Account:
    def __init__(self, bal, acc):
         self.balance = bal
         self.account_no = acc
    
    def debit(self,amount_to_debit):
         self.remain = self.balance - amount_to_debit
         print("Your Remaining Balance after Debit is $",self.remain)

    def credit(self, amount_to_credit):
        self.remain = self.remain + amount_to_credit
        print("Total amount after crediting is ",self.remain)

    def balance1(self):
         print("You total Balance is : ", self.remain)
        
    
Account1= Account(1500,14587984654)
Account1.debit(500)
Account1.credit(1500)
Account1.balance1()