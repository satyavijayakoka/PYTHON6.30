# bank 
# class level variable - country
# constructor  - fn , ln , accNo , balance, transactions
# deposit() , withdrawl()
# static - total accounts
# class level for name change

# class Bank:
#     country = "India"
#     count = 0

#     def __init__(self,fn,ln,acc,bal):
#         self.firstName = fn
#         self.lastName = ln
#         self.accNo = acc
#         self.balance = bal
#         self.transactions = []
#         Bank.count = count+1

#     def deposit(self,amount):
#         self.balance = self.balance + amount
#         self.transactions.append(amount)
    
#     def withdrawl(self,amount):
#         if(self.balance > amount):
#             self.balance = self.balance - amount
#             self.transactions.append(-amount)
#         else:
#             print("insufficient balance")
    
#     def lastFiveTranscations(self,x):
#         return self.transactions[-x::]
    
#     @classmethod
#     def changeCountry(cls,cnty):
#         cls.coumtry = cnty
    
#     @staticmethod
#     def objCount():
#         return Bank.count

class Bank:
    country = "India"
    count = 0
    def __init__(self,fn,ln,acc,bal):
        self.firstName = fn
        self.lastName = ln
        self.accNo = acc
        self.balance = bal
        self.transactions = []
        Bank.count = Bank.count + 1

    def deposit(self,amount):
        self.balance = self.balance + amount
        self.transactions.append(amount)
    
    def withdrawl(self,amount):
        if(self.balance > amount):
            self.balance = self.balance - amount
            self.transactions.append(-amount)
        else:
            print("insufficient balance")
    
    def lastFiveTranscations(self,x):
        return self.transactions[-x::]
    
    @classmethod
    def changeCountry(cls,cn):
        cls.country = cn
    
    @staticmethod
    def objCount():
        return Bank.count
    
satya = Bank("satya","koka",1234,100000)
sai = Bank("sai","madireddy",12345,1000000)
shiva = Bank("shiva","koka",123456,1000000)
koshika = Bank("koshika","koka",1234567,1000)
jathin = Bank("jathin","koka",123,100)

print(Bank.objCount())
satya.withdrawl(300)
satya.deposit(3000)
satya.deposit(30)
satya.deposit(322)
satya.deposit(20)
print(satya.lastFiveTranscations(3))













