from Modules.ExpenseManager.ExpenseManager import ExpenseManager


class AdvancedExpenseManager(ExpenseManager):
    '''
    Advanced Expense Manager having different expense spliting calculations. 
    Can have a different Data Object to store.
    If required, it can simplify Splitings. 
    '''
    def __init__(self, doa):
        super().__init__(doa)

    def addNormalExpense(payee, payer):
        pass

    def showUserStatus(self, user):
        pass

    def showAllStatus(self):
        pass

    def simplifySpliting(self):
        pass

    def addGroupExpense(group_id, payee, payer):
        pass