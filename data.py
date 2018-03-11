import sys


class newData:
    """Create obj to save and import data"""


    def __init__(self):
        self.deacons = []


    def addDeacons(self):
        print("Type In Each Deacon.  Press ENTER after each one\n.")
        print("Begin? Type YES to Begin.  Type NO if you want to keep the same list.")
        if input() == "YES" or "yes":
            print("-> ")
            self.deacons.clear()
            self.deacons.append(str(sys.stdin.readline()))
        else:
            print("no changes made")


obj = newData()
obj.addDeacons()