from Modules.SplitWise.Splitwise import SplitWise
from Modules.ExpenseManager.basicExpenseManager import BasicExpenseManager
from Modules.DOA.dictDOA import DictDataObjectAccess


class SplitWiseService:
    '''
    Initializes Splitwise Application with given dataStorageType and expense Manager. (Currently defaulted.)
    
    '''
    def __init__(self, dataObject=None, expenseManager=None):

        self.dataObject = DictDataObjectAccess()
        self.expenseManager = BasicExpenseManager(self.dataObject)
        self.splitwise = SplitWise(self.expenseManager)
        self.splitwise.setTempUsers(10)

    def service_request(self, service_type, expenseParams):
        '''
        Add Expense depending on the Split Type
        Eg: paidUser="U1" , owedUsers = {"U2": 100, "U3": 200]}
        Assumptions: 
        1) paidUser and owedUsers are already Present.
        '''

        match service_type:
            case "EXPENSE": self.splitwise.expenseManager.addNormalExpense(*expenseParams)
            case "SHOW": self.splitwise.expenseManager.showUserStatus(expenseParams[0])
            case "SHOWALL": self.splitwise.expenseManager.showAllStatus()