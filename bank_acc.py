class BankAccount:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"Deposited {amount} in your account")
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance !")
        else:
            self.balance = self.balance-amount
            print(f"Withdrawed {amount} from your account")
    def __str__(self):
        return f"Account holder name : {self.name} \nBalance : {self.balance}"

obj=BankAccount("prasanth",20000000)
print(obj)
obj.deposit(500)
print(obj)
obj.withdraw(1000)
print(obj)