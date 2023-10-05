'''
Abstract Expense Manager. 
'''

from abc import ABC, abstractmethod

class ExpenseManager(ABC):
    '''
        Abstract Expense Manager that can be extended for following cases: 
            1) Different Data Storage Options (Eg: Dict/MySQL etc.)
            2) Added Functionalities like Group Expenses ETC.
            3) querry implementation variations. Eg: Simplify Expense.
        ExpenseManager uses the data Storage to be used. 
    '''
    def __init__(self, dataObj=None):
        self.userExpenses = dataObj

    @abstractmethod
    def addNormalExpense(self, payee, payer):
        pass
    
    @abstractmethod
    def showUserStatus(self, user):
        pass

    @abstractmethod
    def showAllStatus(self):
        pass
