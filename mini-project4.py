import os
from datetime import datetime


def initialize_csv(filename):
    if not os.path.exists(filename):
        with open(filename, mode='w') as file:
            file.write("Date,Category,Amount,Description\n")
        print(f"CSV file created: {filename}")
    else:
        print(f"CSV file already exists: {filename}")

def record_expense(filename="expenses.csv"):
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter expense category (e.g., Food, Travel, Entertainment): ")
    amount = float(input("Enter amount spent: "))
    description = input("Enter a brief description (optional): ")

    expense_data = f"{date},{category},{amount},{description}\n"
    
    # Append the data to the CSV file
    with open(filename, mode='a') as file:
        file.write(expense_data)
    
    print("Expense recorded successfully!")


# Function to generate a monthly report
def generate_monthly_report(filename):
    current_month = datetime.now().strftime("%Y-%m")
    total_expenses = 0
    category_expenses = {}
    
    try:
        with open(filename, mode='r') as file:
            lines = file.readlines()  
            header_skipped = False 

            for line in lines:
                # Skip the header row
                if not header_skipped:
                    header_skipped = True
                    continue

                row = line.strip().split(',')
                if len(row) < 4:
                    continue

                date, category, amount, description = row
                
                if date.startswith(current_month):
                    total_expenses += float(amount)
                    
                    # Accumulate expenses by category
                    if category in category_expenses:
                        category_expenses[category] += float(amount)
                    else:
                        category_expenses[category] = float(amount)
        
        # Display the report
        print(f"\nMonthly Report for {current_month}:")
        print(f"Total Expenses: ${total_expenses:.2f}")
        
        if category_expenses:
            print("Expenses by Category:")
            for category, amount in category_expenses.items():
                print(f"{category}: ${amount:.2f}")
        else:
            print("No expenses recorded for this month.")
    
    except FileNotFoundError:
        print("Error: CSV file not found. Please record expenses first.")
        

def main_menu():
    filename = r"C:\Users\harip\expenses.csv"
    initialize_csv(filename)
    
    while True:
        print("\n-- Daily Expense Tracker --")
        print("1. Record a new expense")
        print("2. View monthly report")
        print("3. Exit")
        
        choice = input("Please choose an option (1/2/3): ")
        
        if choice == '1':
            record_expense(filename)
        elif choice == '2':
            generate_monthly_report(filename)
        elif choice == '3':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()

#line = " 2024-12-03,Food,20.5,Lunch\n"
#row = line.strip().split(',')
#print(row)

#['2024-12-03', 'Food', '20.5', 'Lunch']
