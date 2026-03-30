# 캡슐화

class Account:
    def __init__(self, money):
        self.__balance = money
        

    def deposit(self, money):
        self.__balance += money
    def get_balance(self):
        return self.__balance
    



if __name__ == '__main__':
    myacc = Account(3000)
    print(myacc.get_balance())
    #print(myacc.balance) 캡슐화 안된 예시
    
