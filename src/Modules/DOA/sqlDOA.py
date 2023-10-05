from abc import ABC
from Modules.DOA.AbstractDOA import DataObjectAccess
from collections import defaultdict

class SQLDataObjectAccess(DataObjectAccess):
    def __init__(self):
        self._data_object = "SQL SERVER"

    def get_user_expense(self, user):
        pass

    def set_user_expense(self, user, updated_data):
        pass

    def get_all_users(self):
        pass    

