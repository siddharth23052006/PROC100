class atm:
  def __init__(self, debitNo, pin, balance):
    self.debitNo = debitNo
    self.pin = pin
    self.balance = balance
  
  def cashWithdraw(self, amount):
    if self.debitNo == '' or self.pin == '':
      print("Please enter the right debit number and pin.")

    else:
      if amount <= self.balance:
        print("You have withdrawn " + str(amount) + " rupees.")
        self.balance = self.balance - amount
        print("You have a remaining balance of " + str(self.balance) + " rupees.")

      else:
        print("You cannot withdraw more money than you have.")

  def cashDeposit(self, amount):
    if self.debitNo == '' or self.pin == '':
      print("Please enter the right debit number and pin.")

    else:
      print("You have deposited " + str(amount) + " rupees.")
      self.balance = self.balance + amount
      print("Your new bank balance is " + str(self.balance) + " rupees.")

  def balanceEnquiry(self):
    if self.debitNo == '' or self.pin == '':
      print("Please enter the right debit number and pin.")

    else:
      print("You have a balance of " + str(self.balance) + " rupees.")

hdfc = atm('4650 5000 6754 6536', '1241', 2000000)
hdfc.cashDeposit(20000)
hdfc.cashWithdraw(32151)
hdfc.balanceEnquiry()