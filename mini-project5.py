class BikeRental:
    def __init__(self, stock, hrate, drate, wrate):
        self.stock = stock
        self.hourly_rate = hrate  # Rate per hour
        self.daily_rate = drate  # Rate per day
        self.weekly_rate = wrate  # Rate per week
        self.rented_bikes = {}  # To track rented bikes and their rental details
        self.rental_counter = 1  # Counter to generate unique rental IDs

    def display_menu(self):
        print("\n--- Bike Rental Shop ---")
        print("1. Display available bikes")
        print("2. Rent a bike (Hourly rate)")
        print("3. Rent a bike (Daily rate)")
        print("4. Rent a bike (Weekly rate)")
        print("5. Return a bike")
        print("6. Exit")

    def rent_bike(self, rental_type):
        if self.stock == 0:
            print("Sorry, no bikes available to rent.")
            return
        
        try:
            bike_count = int(input("How many bikes would you like to rent? "))
            if bike_count <= 0:
                print("Invalid input. You must rent at least 1 bike.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        
        if bike_count > self.stock:
            print("Sorry, not enough bikes available.")
            return
        
        # Family discount for renting between 3 to 5 bikes
        discount = 0
        if 3 <= bike_count <= 5:
            discount = 0.10  # 10% discount
        
        try:
            duration = int(input(f"Enter rental duration (in {'hours' if rental_type == 1 else 'days' if rental_type == 2 else 'weeks'}): "))
            if duration <= 0:
                print("Invalid input. Duration must be a positive number.")
                return
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

        self.stock -= bike_count  # Reduce stock of available bikes
        rental_id = f"bike-{self.rental_counter}"  # Unique rental ID based on counter
        self.rental_counter += 1  # Increment rental counter for the next rental
        self.rented_bikes[rental_id] = {"type": rental_type, "duration": duration, "count": bike_count}
        rate = self.get_rate(rental_type)
        total_cost = rate * duration * bike_count

        # Apply family discount if applicable
        if discount > 0:
            total_cost -= total_cost * discount
            print(f"Family discount applied! Your rental ID is {rental_id}. Total cost after discount is: ${total_cost:.2f}")
        else:
            print(f"Your rental ID is {rental_id}. Total rental cost for {bike_count} bike(s): ${total_cost:.2f}")

    def return_bike(self):
        rental_id = input("Enter rental ID of the bike you're returning: ")
        if rental_id not in self.rented_bikes:
            print("Invalid rental ID.")
            return

        rental_details = self.rented_bikes.pop(rental_id)
        rental_type = rental_details["type"]
        bike_count = rental_details["count"]
        original_duration = rental_details["duration"]
        
        try:
            actual_duration = int(input(f"How long did you actually rent the bike(s) for? Enter in {'hours' if rental_type == 1 else 'days' if rental_type == 2 else 'weeks'}: "))
            if actual_duration <= 0:
                print("Invalid input. Duration must be positive.")
                return
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

        extra_charge = 0
        reduce_charge = 0
        if actual_duration > original_duration:
            extra_duration = actual_duration - original_duration
            # Calculate extra charge
            extra_charge = extra_duration * self.get_rate(rental_type) * bike_count
            print(f"Bike(s) returned. Extra charge: ${extra_charge:.2f}")
        elif actual_duration < original_duration:
            reduce_duration = original_duration - actual_duration
            # Calculate reduce charge
            reduce_charge = reduce_duration * self.get_rate(rental_type) * bike_count
            print(f"Bike(s) returned. Reduced charge: ${reduce_charge:.2f}")
        
        while True:
            try:
                damaged_bikes = int(input(f"How many bikes were damaged out of {bike_count} bikes? "))
                if damaged_bikes < 0 or damaged_bikes > bike_count:
                    print(f"Error: You cannot report more than {bike_count} damaged bikes.")
                else:
                    break
            except ValueError:
                print(f"Error: Please enter a valid number of damaged bikes.")
        
        if damaged_bikes > 0:
            damage_charge = self.calculate_damage_charge(rental_type, damaged_bikes)
            print(f"Damage charge for {damaged_bikes} bike(s): ${damage_charge:.2f}")
        else:
            damage_charge = 0
            print("No damage charges.")
        
        # Return the bike(s)
        self.stock += bike_count  # Add back the bikes to the stock
        
        # Calculate final cost (consider both extra charges, reduce charges, and damage charges)
        final_cost = extra_charge + damage_charge - reduce_charge
        print(f"Final cost to pay (including extra and damage charge): ${final_cost:.2f}")
        
    def calculate_damage_charge(self, rental_type, damaged_bikes):
        try:
            damage_factor = float(input("Enter damage factor (e.g., 1.0 for minor damage, 2.0 for major damage): "))
            if damage_factor < 0:
                print("Invalid input. Damage factor must be a positive number.")
                return 0
        except ValueError:
            print("Invalid input. Please enter a valid damage factor.")
            return 0
        
        if rental_type == 1:  # Hourly rental
            return self.hourly_rate * damage_factor * damaged_bikes
        elif rental_type == 2:  # Daily rental
            return self.daily_rate * damage_factor * damaged_bikes
        elif rental_type == 3:  # Weekly rental
            return self.weekly_rate * damage_factor * damaged_bikes
        return 0

    def get_rate(self, rental_type):
        if rental_type == 1:
            return self.hourly_rate
        elif rental_type == 2:
            return self.daily_rate
        else:
            return self.weekly_rate

    def rental_process(self, choice):
        if choice == 1:
            print(f"We have currently {self.stock} bikes available.")
        elif choice == 2:  # Hourly rental
            self.rent_bike(1)
        elif choice == 3:  # Daily rental
            self.rent_bike(2)
        elif choice == 4:  # Weekly rental
            self.rent_bike(3)
        elif choice == 5:
            self.return_bike()
        elif choice == 6:
            print("Thank you for using the bike rental system!")
            return False  # Exit the loop
        else:
            print("Invalid choice. Please try again.")
        return True  # Continue the loop

class Main:
    def __init__(self):
        self.bike_rental = BikeRental(100, 5, 20, 60)  # Initialize BikeRental with stock and rates

    def start(self):
        while True:
            self.bike_rental.display_menu()
            try:
                select_option = int(input("Choose an option between 1-6: "))
                if not self.bike_rental.rental_process(select_option): # Exit loop
                    break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")

if __name__ == "__main__":
   main_instance = Main()
   main_instance.start()
