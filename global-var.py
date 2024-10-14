#  USING THE GLOBAL KEYWORD - USE RARELY!

# balance = 0 

# def main():
#     print("Balance:", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance:", balance)

# def deposit(n):
#     global balance
#     balance += n

# def withdraw(n):
#     global balance
#     balance -= n

# if __name__ == "__main__":
#     main()

class Account: 
    def __init__(self):
        # Using _balance since we're using @property, which might cause collisions with instance variables
        # Indicates that it's "private" even tho not technically enforced by Python 
        # Other code should not touch this, JUST functions in this class. 
        self._balance = 0

    @property
    def balance(self):
        return self._balance 
    
    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n 

def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)

if __name__ == "__main__":
    main()