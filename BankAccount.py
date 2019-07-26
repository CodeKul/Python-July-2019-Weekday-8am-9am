class Account:

    def __init__(self, no, name, balance):
        self.no = no
        self.name = name
        self.__balance = balance
        print("id of balance:", id(self.__balance))

    def deposite(self, amt):
        self.__balance += amt

    def withdraw(self, amt):
        self.__balance -= amt

    def show_balance(self):
        print("Balance:", self.__balance)
        print("id of balance:", id(self.__balance))
    
    def account_info(self):
        print("Account no:", self.no)
        print("Name:", self.name)
        print("Balance:", self.__balance)


acc1 = Account(1234, "ABC", 1000)
acc1.account_info()
# acc1.deposite(1000)
acc1.show_balance()

acc1.__balance = 100000
print("id of acc1.__balance:", id(acc1.__balance))

acc1.show_balance()
