class SportsMart:
    def __init__(self):
        self.inventory = {}
        self.orders = {}

    def createOrder(self,OrderId, ItemName, Quantity, Price):
        temp = {
            "orderID" : OrderId,
            "ItemName" : ItemName,
            "Quantity" : Quantity,
            "Price" : Price,
        }
        self.orders[OrderId] = temp

    def craete_inventoryItems(self, ProductID, ProductName, Quantity, Price):
        temp = {
            "Product ID" : ProductID,
            "Product Name" : ProductName,
            "Quantity" : Quantity,
            "Price" : Price,
        }
        self.inventory[ProductID] = temp

    def printOrders(self):
            print(self.orders)

    def printInventory(self):
            print(self.inventory)

trinity = SportsMart()
orders = open("orders.csv","r")
orders_header = orders.readlines()
orders_orders = orders.readlines()
for item in orders_orders:
    temp = item.strip().split(',')
    # print(temp)
    trinity.createOrder(temp[0],temp[1],temp[2],temp[3])

trinity.printOrders()