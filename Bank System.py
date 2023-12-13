import datetime
class Bank:
    def __init__(self):
        self._balance = 0
        self._rateOfInterest = 5 # setting the rate of Interest 5% per month 

    def deposit(self,deposit_amount):
        self._balance += deposit_amount

    def check_balance(self):
        print(self._balance)
    def withdrawl(self,withdraw_amount):
        if withdraw_amount > self._balance:
            print("Insufficient Balance")
        else:
            self._balance -= withdraw_amount 
            print("Remaining Balance : "+ str(self._balance))
    # Calculating the interest over a specified period of time.
    def calculate_interest(self,dt1,dt2):
        tot_days = abs(dt2-dt1).days
        months = tot_days // 30
        interest = ( self._rateOfInterest / 100 ) * self._balance * months
        print(interest)
   
b1 = Bank()
b1.deposit(1000)
b1.calculate_interest(datetime.date(2023,10,20),datetime.date(2023,12,20))
b1.withdrawl(500)
b1.withdrawl(500)
b1.withdrawl(100)
