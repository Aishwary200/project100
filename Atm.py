class Atm:
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber

    def cashWithdrawl(self):
        print("Withdraw Cash")

    def BalanceEngquiry(self):
        print("Balance Enquiry")

    def cashDeposit(self):
        print("Deposit Cash")


card = Atm('1000100010110', '2252')
print(card.cashWithdrawl())
print(card.cardNumber)
print(card.pinNumber)
