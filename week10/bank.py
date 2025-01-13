class bank:
    def __init__(self,id,name,balance):
        self.id = id
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        if amount >= 100:
            self.balance += amount
        else:
            print('ใส่ยอดเงิน 100 บาทขึ้นไป')
    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance :
            self.__balance -= amount
        else :
            print('ยอดเงินไม่ถูกต้อง')
    def check(self):
        return self.__balance

id1 = bank(1,"Pond",5000)
id1.__balance += 5000
id1.withdraw(1000)
print(f'เงินของ{id1.name}มีอยู่{id1.balance}บาท')