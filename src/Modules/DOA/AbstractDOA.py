'''
Abstract Data Object we want to use to store expense for users. 
'''

from abc import ABC

class DataObjectAccess(ABC):
    def __init__(self):
        self._data_object = None

    def get_user_expense(self, user):
        pass

    def set_user_expense(self, user):
        pass

