from abc import ABC
from typing import Dict
from Modules.Users import User

class SplitWise():
    def __init__(self, expenseManager):
        self.splitWiseUsers = {}
        self.numUsers = 0
        self.expenseManager = expenseManager

    def getSplitWiseUsers(self) -> Dict[str, User]:
        return self.splitWiseUsers

    def setTempUsers(self, numUsers:str = 10) -> None:
        tempUsers = {f"u{i}": User(f"User{i}") for i in range(numUsers)}
        self.splitWiseUsers = tempUsers
        self.numUsers = len(tempUsers)

    def addUser(self) -> None: 
        userName = f"U{self.numUsers + 1}"
        newUser = User(userName)
        self.splitWiseUser[userName: newUser]
        self.numUsers += 1

    def deleteUser(self) -> bool:
        pass
    