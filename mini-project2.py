class Account:
    def __init__(self, name, balance, passkey):
        self.name = name
        self.balance = balance
        self.passkey = passkey
        
    def check_pin(self, confirm_pin):
        if confirm_pin == self.passkey:
            print("Authentication Successful!")
            return True
        else:
            print("Authentication Failed!")
            return False

class ATM(Account):
    def __init__(self, name, balance, passkey):
        super().__init__(name, balance, passkey)

    def display_menu(self):
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")
    
    def initiate_process(self, select_option):
        if select_option == 1:
            print(f"Your Current Balance: {self.balance:.2f}")
        elif select_option == 2:
            withdrawal = float(input("Enter amount to withdraw: "))
            if withdrawal <= self.balance:
                self.balance -= withdrawal
                print(f"Withdrawal successful! New Balance: {self.balance:.2f}")
            else:
                print("Insufficient funds.")
        elif select_option == 3:
            deposit = float(input("Enter amount to deposit: "))
            self.balance += deposit
            print(f"Deposit successful! New Balance: {self.balance:.2f}")
        elif select_option == 4:
            print("Exiting...")
            return False
        else:
            print("Invalid choice! Please choose between 1-4.")
        return True

def validate_pin(pin):
    if isinstance(pin, str) and len(pin) == 4 and pin.isdigit():
        return True
    else:
        print("Invalid PIN! The PIN must be exactly 4 digits.")
        return False

def main():
    owner = input("\nEnter your name: ")
    
    pin = int(input("\nSet your 4-digit PIN: "))
    while not validate_pin(pin):
        pin = int(input("\nSet your 4-digit PIN: "))
    
    account_details = Account(owner, 1000.00, pin)
    
    for attempt in range(3):
        input_pin = input("Enter your 4-digit PIN: ")
        
        while not validate_pin(input_pin):
            input_pin = input("Enter your 4-digit PIN: ")
        
        if account_details.check_pin(input_pin):
            atm = ATM(owner, account_details.balance, account_details.passkey)  # Create ATM instance using Account details
            
            while True:
                atm.display_menu()
                try:
                    select_option = int(input("Choose an Option between 1-4: "))
                    if not atm.initiate_process(select_option):  # If exit option is chosen, stop the loop
                        break
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 4.")
            break
        else:
            print(f"You have {2 - attempt} attempt(s) left.")
            
    else:
        print("Too many failed attempts. Access denied.")

if __name__ == "__main__":
    main()
