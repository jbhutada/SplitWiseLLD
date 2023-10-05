from Modules.ExpenseManager.ExpenseManager import ExpenseManager

class BasicExpenseManager(ExpenseManager):
    '''
        Very Basic Expense Manager which works on Dict Data Objects for Expense Tracking.

    '''
    def __init__(self, data_obj):
        self.data_obj = data_obj

    def addNormalExpense(self, payee:str, amount:float, payers:dict) -> None:
        '''
        Add Normal Expense Splits.
        Eg: 
            payee='u1', payers={'u2': 100, 'u3': 200}
            u2 owes u1 100
            u3 owes u2 200
        '''
        payee_expense = self.data_obj.get_user_expense(payee)
        for payer, amount in payers.items():
            payer_expense = self.data_obj.get_user_expense(payer)
            payer_expense[payee] -= amount
            payee_expense[payer] += amount
            self.data_obj.set_user_expense(payer, payer_expense)
        self.data_obj.set_user_expense(payee, payee_expense)



    def showUserStatus(self, user:str, printStatus:bool = True) -> list:
        '''
        Show current standings of user.
        Prints if required.  
        Returns the current standings. 
        '''
        user_data = self.data_obj.get_user_expense(user)
        statuses = []
        for u, amt in user_data.items():
            if amt > 0:
                statuses.append(f"{u} owes {user}: {abs(amt)}")
            if amt < 0:
                statuses.append(f"{user} owes {u}: {abs(amt)}")
        if len(statuses) == 0:
            print("No Balances")

        if printStatus:
            for s in statuses:
                print(s)

        return statuses
                
    def showAllStatus(self) -> None:
        '''
        Reports all the expenses of all the users currently owing something. 
        '''
        all_statuses = []
        for user in self.data_obj.get_all_users():
            all_statuses += self.showUserStatus(user, printStatus=False)
        if not all_statuses:
            print('No Balances')
        for status in set(all_statuses):
            print(status)
