class account:
    def __init__(self,acc,bal):   
        self.bal=bal
        self.acc=acc

    def debit(self,amount):
        self.bal-=amount
        print("Rs.", amount, "was debited")
        print("total balance= ",self.get_balance())


    def credit(self,amount):
        self.bal+=amount
        print("Rs.", amount, "was credited")
        print("total balance= ",self.get_balance())

    def get_balance(self):
        return self.bal
    

acc1=account(10000,12345)
acc1.credit(500)
acc1.debit(1000)