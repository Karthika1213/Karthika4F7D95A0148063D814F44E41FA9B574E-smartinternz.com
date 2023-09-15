￼Class Bank Account :
def_init_(self account_number,account_holder_name, 
   initial balance=0.0):
self. _account_number= account _ number
self. _account_holder_name =account_holder_name
self._account_balance= initial_balance

def deposite(self,amount):
 If amount < 0:
  self. account_balance +=￼amount print("Deposite ₹{}. New balance :₹
  {}. format(amount, self. _account_balance))
  else:
  print(" Invalid deposite amount. please deposite a positive amount")
  def withdraw(self, amount):
  if amount > 0 and amount <= self. _account_balance:
  self. _account_balance-= amount
  print("withdraw ₹{}. New balance"):₹
  {}. format(amount, self. _account_balance)) 
  else:
  print("Invalid withdraw amount or insufficient balance. ")
  def display_ balance.(self):
  print("Account balance for{} (Account # {}) : ₹
  {}. format(self. _account_holder_name, self. account_number, self. _account_balance)) 
  # create an Instance of the bank
  account class
  account=BankAccount(account_number=" 123456789",account_holder_name="divya", initial_balance5000.0) 

  #Test deposite and withdrawal functionality
  account. display_balance(
  account. deposite(500.0)
  account.withdraw(200.0
  account. Withdraw(20000.0)
  account. display _account_balance()