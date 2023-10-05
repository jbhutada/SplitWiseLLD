from abc import ABC
from Modules.DOA.AbstractDOA import DataObjectAccess
from collections import defaultdict

class DictDataObjectAccess(DataObjectAccess):
    def __init__(self):
        self._data_object = defaultdict(lambda: defaultdict(int))

    def get_user_expense(self, user):
        return self._data_object[user]

    def set_user_expense(self, user, updated_data):
        self._data_object[user] = updated_data

    def get_all_users(self):
        return self._data_object.keys()
    

