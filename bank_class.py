class Bank:

    account_num = ""
    balance = 0
    min_bal = 0
    pan_num = ""

    def __init__(self, act_num, bal, min, pan):
        self.min_bal = min
        self.account_num = act_num
        self.balance = bal
        self.min_bal = min
        self.pan_num = pan

    def deposit(self,amount):
        self.balance = self.balance + amount

    
