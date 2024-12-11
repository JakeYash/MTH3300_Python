#******************************************************************************
# bank.py
#******************************************************************************
# Name: Jake
#******************************************************************************
# Collaborators/outside sources used
#(IMPORTANT! Write "NONE" if none were used):
#
# NONE
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
# I used programiz.com online python interpreter as opposed to spyder
# spyder has not been working for me recently
# I think withdrawal and transfer functions would do well with reutrn values
# or printed messages upon completion
# I think not accounting for (-) values might be weird on transfer as well, but still works
# I renamed withdrawal to withdraw, just made more sense considering what methods are and the name of every other method

class Bank:
    """
    A class that has objects that contain the name of a bank, and a dictionary with every account at that bank
    """
    
    def __init__(self, name):
        """
        Counstructor takes input for name of bank, sets accounts equal to empty dictionary
        """
        self._name = name
        self._accounts = {}
        
    def createaccount(self, name, checking = 0, saving = 0):
        """
        Makes an account with given name and checking and saving account amounts, by default 0
        """
        self._accounts[name] = {"CHECKING":checking,"SAVING":saving}
        
    def display(self, name):
        """
        Takes the name of an account as input, prints out the information of their account
        """
        print(name,':',self._accounts[name])
    
    def deposit(self,name,amount):
        """
        Takes name of an account, and amount of money, adds that amount to checking unless its negative, in which case an error message will print.
        """
        if (amount < 0):
            print("You can't deposit negative money!")
        else:
            self._accounts[name]["CHECKING"] += amount
        
    def withdraw(self, name, amount):
        """
        Takes name of account and amount to withdraw as input, if amount is negative or more than amount in checking, error message is printed, otherwise that amount is subtracted from checking
        """
        if (amount < 0):
            print("You can't withdraw negative money!")
        elif (self._accounts[name]["CHECKING"] < amount):
            print("Not enough to withdraw!")
        else:
            self._accounts[name]["CHECKING"] -= amount
            
    def transfer(self,name,amount,acc1 = "CHECKING", acc2 = "SAVING"):
        """
        Takes name of account, amount to transfer, and from which part to which part (by default from checking to saving). If amount exceeds initial account, error message is printed, otherwise transfers to destination account.
        """
        if (amount > self._accounts[name][acc1.upper()]):
            print("Not enough money in",acc1, "!")
        else:
            self._accounts[name][acc1.upper()] -= amount
            self._accounts[name][acc2.upper()] += amount