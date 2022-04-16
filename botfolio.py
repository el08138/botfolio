"""
Created on Tue Sep 28 18:36:49 2021
Investment portfolio bot
@author: Stamatis
"""

""" import libraries """
from collections import defaultdict

class Botfolio:
    def __init__(self):
        self.investment_accounts = ['InvAccount1']
        self.retirement_accounts = ['RetAccount1', 'RetAccount2']
        self.crypto_accounts = ['CptAccount1', 'CptAccount2']
        self.savings_accounts = ['SavAccount1']
        self.securities = ['Stocks Index', 'Bonds', 'Crypto', 'Cash', 'SecClass5']
        self.retirement_accounts_rates = dict()
        for acc in self.retirement_accounts:
            self.retirement_accounts_rates[acc] = []
            self.retirement_accounts_rates[acc].append(int(input('Please enter the stocks allocation rate for your {} account (in %): \n'.format(acc))) / 100)
            self.retirement_accounts_rates[acc].append(int(input('Please enter the bonds allocation rate for your {} account (in %): \n'.format(acc))) / 100)
        
    def read_targets(self):
        self.securities_rates = dict()
        for sec in self.securities:
            self.securities_rates[sec] = int(input('Please enter your target {} allocation rate (in %): \n'.format(sec))) / 100
        
    def read_balances(self):
        self.securities_balances = defaultdict(int)
        self.total_balance = 0
        for acc in self.investment_accounts:
            print('\n\n\n##############################')
            print(acc)
            print('##############################\n\n\n')
            for sec in self.securities:
                temp_balance = int(input('Please enter your {} balance for your {} account (in $): \n'.format(sec, acc)))
                self.securities_balances[sec] += temp_balance
                self.total_balance += temp_balance
                
        for acc in self.retirement_accounts:
            print('\n\n\n##############################')
            print(acc)
            print('##############################\n\n\n')
            temp_balance = int(input('Please enter your total balance for your {} account (in $): \n'.format(acc)))
            self.total_balance += temp_balance
            self.securities_balances['Stocks Index'] += temp_balance * self.retirement_accounts_rates[acc][0]
            self.securities_balances['Bonds'] += temp_balance * self.retirement_accounts_rates[acc][1]
            
        for acc in self.crypto_accounts:
            print('\n\n\n##############################')
            print(acc)
            print('##############################\n\n\n')
            temp_balance = int(input('Please enter your crypto balance for your {} account (in $): \n'.format(acc)))
            self.total_balance += temp_balance
            self.securities_balances['Crypto'] += temp_balance
            
        for acc in self.savings_accounts:
            print('\n\n\n##############################')
            print(acc)
            print('##############################\n\n\n')
            temp_balance = int(input('Please enter your cash balance for your {} account (in $): \n'.format(acc)))
            self.total_balance += temp_balance
            self.securities_balances['Cash'] += temp_balance
            
    def adjust_balances(self):
        for sec in self.securities:
            adjustment_amount = int(self.securities_rates[sec] * self.total_balance - self.securities_balances[sec])
            print('\nAdjust your {} holdings by \n{}$\n'.format(sec, adjustment_amount))
                       
if __name__ == '__main__':
    StamBotfolio = Botfolio()
    StamBotfolio.read_targets()
    StamBotfolio.read_balances()
    StamBotfolio.adjust_balances()