
class Account:

#Constructor
    def __init__(self, filepath): 
        self.filepath = filepath
        with open (filepath, 'r') as file:
            self.balance = int(file.read()) #current balance
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        print('you withdrew $', amount)
        Account.commit(self) #calling the commit method to write it to the file
        print('your current balance is', self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print('you deposited $', amount)
        Account.commit(self)
        print('your current balance is', self.balance)

    #Write changes to the file
    def commit (self):
        with open (self.filepath, 'w') as file:
            file.write(str(self.balance))



class Checking (Account):

    """ This class generates checking accounts """

    type = "checking" #class variables like static in java

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath) #(checking account is everything above + other methods)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee



#instantiating an account of Account class
#account = Account("/Users/andrewyip/Desktop/udemy_python/intro_stuff/app5withbankacct/balance.txt")
#account.deposit(900)

#Inheritance Practice
checking = Checking("/Users/andrewyip/Desktop/udemy_python/intro_stuff/app5withbankacct/balance.txt",1)
checking.transfer(110)
print(checking.balance)
checking.commit() #commit the changes

