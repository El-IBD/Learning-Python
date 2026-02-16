class Transaction:
    
    def __init__(self, transaction_id, date, amount, category, description, transaction_type):
        self.id = transaction_id
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description
        self.type = transaction_type

class Budget:
    def __init__(self, category, amount, month):
        self.category = category
        self.amount = amount
        self.month = month

class FinanceManager:  
    def __init__(self):
        self.transactions = []
        self.budgets = {}  # Key: "YYYY-MM:category"
        self.next_transaction_id = 1
    
    def add_transaction(self, date, amount, category, description, transaction_type):
        new_data = Transaction(
            self.next_transaction_id, date, amount, 
            category, description, transaction_type
        )
        self.transactions.append(new_data)
        self.next_transaction_id += 1
        print(f"\n Transaction added: {transaction_type} of {amount: } in {category}")

    def set_budget(self, category, amount, month):
        key = f"{month}:{category}"
        self.budgets[key] = Budget(category, amount, month)
        print(f"\n Budget set: {amount:} for {category} in {month}")

    def get_transactions_by_month(self, month):
        """Get all transactions for a specific month (YYYY-MM)"""
        result = []
        for t in self.transactions:
            if t.date[:7] == month:
                result.append(t)
        return result
    
    def generate_monthly_report(self, month):
        transactions = self.get_transactions_by_month(month)
        
        if not transactions:
            print(f"\n{'='*60}")
            print(f"Monthly Report for {month}")
            print(f"{'='*60}")
            print("No transactions found for this month.")
            return
        
        total_income = 0.0
        total_expenses = 0.0
        for t in transactions:
            if t.type == 'income':
                total_income += t.amount
            else:
                total_expenses += t.amount
        
        net_income = total_income - total_expenses

        print(f"MONTHLY FINANCIAL REPORT - {month}")

        print(f"\n SUMMARY")
        print(f"   Total Income:    {total_income: }")
        print(f"   Total Expenses:  {total_expenses: }")
        print(f"   Net Income:      {net_income: }")


def main_menu():
        print(" PERSONAL FINANCE MANAGER")
        print("1.  Add Income")
        print("2.  Add Expense")
        print("3.  Set Monthly Budget")
        print("4.  View Monthly Report")
        print("5. Exit")

def get_valid_amount():
    
        while True:
            try:
                amount_str = input("Enter amount: ").strip()
                amount = float(amount_str)
                if amount <= 0:
                    print("Amount must be positive.")
                    continue
                return amount
            except:
                print("Invalid amount. Please enter a number.")

def main():

    manager = FinanceManager()
        
    print("\n Welcome to Personal Finance Manager!")
    print("Starting fresh with no existing data.")
        
    while True:
        main_menu()
        choice = input("Select an option (1-10): ").strip()
            
        if choice == '1':  
            date = input("Enter Date: ")
            amount = get_valid_amount()
            category = input("Enter category (e.g., Salary, Freelance, Investment): ").strip()
            description = input("Enter description: ").strip()
            manager.add_transaction(date, amount, category, description, 'income')
            
        elif choice == '2':
            amount = get_valid_amount()
            category = input("Enter category (e.g., Food, Transport, Entertainment): ").strip()
            description = input("Enter description: ").strip()
            manager.add_transaction(date, amount, category, description, 'expense')
            
            
        elif choice == '3':  # Set Budget
            month = input("Enter Month: ")
            category = input("Enter category: ").strip()
            amount = get_valid_amount()
            manager.set_budget(category, amount, month)
            
        elif choice == '4': 
            month = input("Enter Month: ")
            manager.generate_monthly_report(month)
            
            
        elif choice == '5': 
            print("\n Thank you for using Personal Finance Manager!")
            break
            
        else:
            print("\n Invalid option selected")


if __name__ == "__main__":
    main()
