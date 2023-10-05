from collections import defaultdict

class User:
    def __init__(self, userName):
        self.userName = userName


# Temp Helper Function
def getTempUsers(numUsers: int=10):
    tempUsers = [User(f"U{i}") for i in range(numUsers)]
    return tempUsers

    
