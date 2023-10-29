# FIRST PERIOD
class MScDSB:
    def __init__(self):
        # Data members or properties or attributes
        self.name = "MSc DS B"
        self.students = ["A", "B", "C"]

obj = MScDSB()
print(obj.name)
print(obj.students)

# SECOND PERIOD

class MScDSB:
    def __init__(self): # Member Function
        # Data members or properties or attributes
        self.name = "MSc DS B"
        self.students = ["A", "B", "C"]
    
    def printStudents(self): # Member Function
        for student in self.students:
            print(student)
    
    def printClass(self): # Member Function
        for class_name in self.name:
            print(class_name)

obj = MScDSB()
obj.printStudents()
obj.printClass()

# THIRD PERIOD

class car:

    def __init__ (self, mfg, mdl, yr):
        self.Manufacturer = mfg
        self.Model = mdl
        self.Year = yr
        
bmw = car("BMW", "F SERIES", 2022)
mercedes = car("MERCEDES", "Mercedes Benz", 2023)
tesla = car("TESLA", "X CLASS", 2019)
print(bmw.Manufacturer)
print(bmw.Year)
print(tesla.Model)
print(mercedes.Year)
print(mercedes.Manufacturer)

# FOURTH PERIOD

# Create a class restaurant, that accepts
# Item name & quantity as input
# Inside your class you are having the item
# And its price as a dictionary
# Create a function that calculate total cost
# That prints the item name, quantity and total cost

class restaurant:

    def __init__ (self,itemname, qty):
        self.itemname = itemname
        self.qty = qty
        self.menuItems = {
            "RICE": 30,
            "CHICKEN": 100,
            "DAL": 40,
            "CHAPATHI": 15
        }
    
    def totalCost(self):
        print("TOTAL COST OF THE ORDER")
        print("Item\t\t:",self.itemname)
        print("Quantity\t:",self.qty)
        total = self.qty * self.menuItems[self.itemname]  
        print("Total\t\t:",total)      

order = restaurant("RICE", 4)
order.totalCost()  
order = restaurant("DAL", 5)
order.totalCost()
order = restaurant("CHICKEN", 5)
order.totalCost()             