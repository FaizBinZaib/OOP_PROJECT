# Car Rental System

def display_menu():
    print("\nCar Rental System")
    print("1. Reserve a Car")
    print("2. Check Car Availability")
    print("3. Return a Car")
    print("4. Display All Cars")
    print("5. Exit")

def add_car(cars, car_id, model):
    cars[car_id] = {"Model": model, "Available": True}

def reserve_car(cars):
    car_id = input("Enter Car ID to reserve: ").strip()
    if car_id not in cars:
        print("Car ID not found.")
        return
    if not cars[car_id]["Available"]:
        print("Car is already reserved.")
        return
    cars[car_id]["Available"] = False
    print(f"Car {car_id} ({cars[car_id]['Model']}) has been reserved successfully.")

def check_availability(cars):
    print("\nAvailable Cars:")
    available_cars = [car_id for car_id, details in cars.items() if details["Available"]]
    if not available_cars:
        print("No cars available.")
        return
    for car_id in available_cars:
        print(f"Car ID: {car_id}, Model: {cars[car_id]['Model']}")

def return_car(cars):
    car_id = input("Enter Car ID to return: ").strip()
    if car_id not in cars:
        print("Car ID not found.")
        return
    if cars[car_id]["Available"]:
        print("Car is already available.")
        return
    cars[car_id]["Available"] = True
    print(f"Car {car_id} ({cars[car_id]['Model']}) has been returned successfully.")

def display_all_cars(cars):
    if not cars:
        print("No cars in the system.")
        return
    print("\nAll Cars:")
    print("ID	Model		Availability")
    print("-" * 40)
    for car_id, details in cars.items():
        status = "Available" if details["Available"] else "Reserved"
        print(f"{car_id}	{details['Model']}	{status}")

def main():
    cars = {}

    # Adding some sample cars
    add_car(cars, "C001", "Toyota Camry")
    add_car(cars, "C002", "Honda Civic")
    add_car(cars, "C003", "Ford Mustang")

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            reserve_car(cars)
        elif choice == "2":
            check_availability(cars)
        elif choice == "3":
            return_car(cars)
        elif choice == "4":
            display_all_cars(cars)
        elif choice == "5":
            print("Exiting the Car Rental System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()