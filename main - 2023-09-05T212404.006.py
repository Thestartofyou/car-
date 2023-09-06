class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.year} {self.make} {self.model} - ${self.price:.2f}"


class CarInventory:
    def __init__(self):
        self.inventory = []

    def add_car(self, car):
        self.inventory.append(car)

    def view_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            for i, car in enumerate(self.inventory, start=1):
                print(f"{i}. {car}")

    def search_car(self, keyword):
        found_cars = []
        for car in self.inventory:
            if keyword.lower() in car.make.lower() or keyword.lower() in car.model.lower():
                found_cars.append(car)

        if found_cars:
            print(f"Found {len(found_cars)} cars matching '{keyword}':")
            for i, car in enumerate(found_cars, start=1):
                print(f"{i}. {car}")
        else:
            print(f"No cars found matching '{keyword}'.")


def main():
    inventory = CarInventory()

    while True:
        print("\nCar Inventory System")
        print("1. Add Car")
        print("2. View Inventory")
        print("3. Search for a Car")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            make = input("Enter the make of the car: ")
            model = input("Enter the model of the car: ")
            year = int(input("Enter the year of the car: "))
            price = float(input("Enter the price of the car: "))
            car = Car(make, model, year, price)
            inventory.add_car(car)
            print("Car added to inventory.")
        elif choice == '2':
            inventory.view_inventory()
        elif choice == '3':
            keyword = input("Enter a make or model to search for: ")
            inventory.search_car(keyword)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
