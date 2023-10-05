SplitWise LLD

Assumptions:

Input Given is correct. (In case of wrong input.)
All the users in input are known to us.
Components:

Driver Code: Code which gives input, parses and processes them.
SplitWise Service: Interacts with the SplitWise Application. Initialises the DataObject, ExpenseManager and SplitWise Application.
DataObjects: The database we want to use. Currently it is defaulted to defaultdict, but it can be anything.
ExpenseManager: Deals with all expense related tasks. Interacts with DataObject.
SplitWise: Deals with all the SplitWise Activities. (Eg: Add User, Add Groups etc.)
Note:

DataObjects can be implemented in any form given the Abstract class.
ExpenseManager can be basic or advanced (having simplify splits functionality.)
Splitwise can use any ExpenseManager/DataObjects. It is a plug and play model.
What to run ? DriverCode.py
