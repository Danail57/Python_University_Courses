"""
2. Да се състави програма, която съхранява в масив
следната информация за лекарствата в една
аптека

наименование - низ до 20 знака;
цена - реално число;
налично количество - цяло число;
дата, до която е годно за употреба

и извършва следните операции, избирани от меню:

- добавя към масива  данните на ново лекарство;
- извежда всички въведени данни;
- извежда общата стойност на лекарствата в аптеката
с цена над 10 лв.;
- създава нов масив с данните на лекарствата
с цена над 15 лв;
- създава нов масив с имената и цените на лекарствата
 с изтичащ срок на годност на зададена дата.
"""
from datetime import datetime

class Pharmacy:
    def __init__(self, name: str, price: float, quantity: int, expiry_date: datetime)->None:
        self.name = name
        self.price = price
        self.quantity = quantity
        self.expiry_date = expiry_date

    def __str__(self):
        return (f"Medicine name: {self.name},"
                f"price: {self.price:.2f},"
                f"quantity: {self.quantity},"
                f"expiration date: {self.expiry_date}")
medicine_inventory = []

# Functions
def add_medicine():
    name = input("Medicine name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    date = input("Expiry date: (YYYY-MM-DD)")
    expiry_date = datetime.strptime(date, "%Y-%m-%d")
    new_medicine = Pharmacy(name, price, quantity, expiry_date)
    medicine_inventory.append(new_medicine)

def show_medicines():
    if not medicine_inventory:
        print("No medicine found")
    else:
        for medicine in medicine_inventory:
            print(medicine)

def get_expiring_on_date():
    target_date_str = input("Write a date for a check (YYYY-MM-DD): ")
    target_date = datetime.strptime(target_date_str, "%Y-%m-%d")
    expiring_medicines = [{"name": medicine.name,
                           "price": medicine.price}
                          for medicine in medicine_inventory
                          if medicine.expiry_date == target_date]
    if not expiring_medicines:
        print(f"No medicines that are expiring on {target_date_str}")
    else:
        for medicine in expiring_medicines:
            print(f"Medicine name {medicine['name']},"
                  f"Price: {medicine['price']}")
    return expiring_medicines

def calculate_total_price_over_10():
    total = sum(medicine.price * medicine.quantity for medicine in medicine_inventory if medicine.price > 10.0)
    print(f"Total price: {total:.2f}")

def get_medicines_over_15():
    expensive_medicines = [medicine for medicine in medicine_inventory if medicine.price > 15.0]
    if not expensive_medicines:
        print("No medicines with price above 15")
    else:
        for medicine in expensive_medicines:
            print(medicine)
    return expensive_medicines

def menu():
    while True:
        print("\nPharmacy Menu\n")
        print("1. Add medicine\n")
        print("2. Display all data\n")
        print("3. Show medicines over 15$\n")
        print("4. Calculate total price over 10$\n")
        print("5. Expiring medicines on a given date\n")
        print("6. Exit\n")
        choice = input("Choice: ")

        match choice:
            case "1":
                add_medicine()
            case "2":
                show_medicines()
            case "3":
                get_medicines_over_15()
            case "4":
                calculate_total_price_over_10()
            case "5":
                get_expiring_on_date()
            case "6":
                break
            case _:
                print("Invalid choice")
menu()
