class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass   # private

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345", "12ewe")

acc1.reset_pass()   

# print(acc1.__acc_pass) ❌ error