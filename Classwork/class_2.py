class expenseTracker:
    def _init_(self):
        self.expenseDict = {
            "income": [],
            "expense": [],
        }

    def store_transactions(self, type, amt, category, date, details):
        trans = {
            "Amount": amt,
            "Category": category,
            "Date": date,
            "Details": details,
        }
        if type == "income":
            self.expenseDict['income'].append(trans)
        else:
            self.expenseDict['expense'].append(trans)

    def view_transactions(self):
        print("Your Income:")
        for item in self.expenseDict['income']:
            print(item)
        print("Your Expenses:")
        for item in self.expenseDict['expense']:
            print(item)

    def calculate_transactions(self):
        total_income = 0
        for item in self.expenseDict['income']:
            total_income += item["Amount"]
        print("Total Income\t:\t", total_income)

        total_expense = 0
        for item in self.expenseDict['expense']:
            total_expense += item["Amount"]
        print("Total Expenses\t:\t", total_expense)

    def export_to_csv(self, filename):
        try:
            with open(filename, mode='w') as file:
                file.write("Type,Amount,Category,Date,Details\n")
                for item in self.expenseDict['income']:
                    file.write(f"Income,{item['Amount']},{item['Category']},{item['Date']},{item['Details']}\n")
                for item in self.expenseDict['expense']:
                    file.write(f"Expense,{item['Amount']},{item['Category']},{item['Date']},{item['Details']}\n")
            print(f"Data has been exported to {filename} successfully.")
        except Exception as e:
            print(f"An error occurred while exporting data: {e}")

    def collectInput(self):
        amt = int(input("Enter the amount: "))
        category = input("Enter Category: ")
        date = input("Enter Date (DD/MM/YYYY): ")
        details = input("Enter description: ")
        return amt, category, date, details


myexpense = expenseTracker()

while True:
    print("...MY EXPENSE TRACKER...")
    print("1. Record Income")
    print("2. Record Expense")
    print("3. View Records")
    print("4. View My Spendings")
    print("5. Export to CSV")
    print("6. Exit")

    choice = int(input("Enter your choice: ").strip())

    if choice == 1:
        print("Enter the details of income")
        amt, category, date, details = myexpense.collectInput()
        myexpense.store_transactions("income", amt, category, date, details)
    elif choice == 2:
        print("Enter the details of expense")
        amt, category, date, details = myexpense.collectInput()
        myexpense.store_transactions("expense", amt, category, date, details)
    elif choice == 3:
        myexpense.view_transactions()
    elif choice == 4:
        myexpense.calculate_transactions()
    elif choice == 5:
        filename = input("Enter the CSV filename to export data: ")
        myexpense.export_to_csv(filename)
    elif choice == 6:
        exit()
    else:
        print("Invalid choice")