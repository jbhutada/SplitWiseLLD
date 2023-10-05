SplitWise LLD

Assumptions: 
1) Input Given is correct. (In case of wrong input.)
2) All the users in input are known to us. 

Components:
1) Driver Code: Code which gives input, parses and processes them. 
2) SplitWise Service: Interacts with the SplitWise Application. Initialises the DataObject, ExpenseManager and SplitWise Application.
3) DataObjects: The database we want to use. Currently it is defaulted to defaultdict, but it can be anything.  
4) ExpenseManager: Deals with all expense related tasks. Interacts with DataObject.
5) SplitWise: Deals with all the SplitWise Activities. (Eg: Add User, Add Groups etc.)


Note:
1) DataObjects can be implemented in any form given the Abstract class. 
2) ExpenseManager can be basic or advanced (having simplify splits functionality.)
3) Splitwise can use any ExpenseManager/DataObjects. It is a plug and play model.


What to run ? 
DriverCode.py

