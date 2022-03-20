# Python:     Ver 3.10.2
#
# Author:     Fox Addams
#
# Purpose:    Demonstrating encapsulation via use of Protected
#             and Private variables.
#
# Tested OS:  This code was written and tested with Windows 10.


# Parent class
class Asset:

    def __init__(self, title, stable, ready, handler, identity):
        self.title = title
        self.stable = stable
        self.ready = ready
        self.protectedHandler = handler
        self.__privateID = identity      
    
    def info(self):
        msg = "\nTitle: {}\nStability: {}\nMission Ready: {}\n".format(self.title,self.stable,self.ready)
        return msg

    def getPrivate(self):
        print("TOP SECRET: {}'s identity is {}".format(self.title,self.__privateID))

    def setPrivate(self, private):
        self.__privateID = private
        
# Instantiating an object
ws = Asset("Winter Soldier", "Questionable", True, "Brock Rumlow", "James Buchanan Barnes")


if __name__ == "__main__":
      print(ws.info())
      print("{}'s current Handler: {}".format(ws.title,ws.protectedHandler))
      ws.getPrivate()
      ws.setPrivate("James 'Bucky' Buchanan Barnes")
      ws.getPrivate()
