''' 1.  Да се състави програма, която съхранява в масив следната информация за лекарствата в една
аптека:
 - наименование - низ до 20 знака;
 - цена - реално число;
 - налично количество - цяло число;
 - дата, до която е годно за употреба
и извършва следните операции, избирани от меню:
 - добавя към масива  данните на ново лекарство;
 - извежда всички въведени данни;
 - извежда имената на лекарствата с цена над 5 лв;
 - създава нов масив с данните на лекарствата с налични количества под 10 броя;
 - създава нов масив с имената количествата на лекарствата с изтичащ срок на годност на
зададена дата '''

from datetime import datetime
from unittest import case

MEDICINE_PRICE = 5.0
MEDICINE_QUANTITY = 10

class Pharmacy:
    def __init__(self, name: str, price: float, quantity: int, expiry_date: datetime) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        self.expiry_date = expiry_date

    def __str__(self):
        return f"Medicine name: {self.name},\n Price {self.price:.2f}$, \n Quantity {self.quantity}, \n Expiry date {self.expiry_date.strftime('%d/%m/%Y')}"

pharmacy_inventory = []

def add_medicine():
    name = input("Medicine name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    date = input("Expiry date: (YYYY-MM-DD): ")
    expiry_date = datetime.strptime(date, "%Y-%m-%d")
    new_medicine = Pharmacy(name, price, quantity, expiry_date)
    pharmacy_inventory.append(new_medicine)

def show_medicines():
    if not pharmacy_inventory:
        print("No medicine found")
    for medicine in pharmacy_inventory:
        print(medicine)

def print_expensive_medicines():
    found = False
    for medicine in pharmacy_inventory:
        if medicine.price > MEDICINE_PRICE:
            print(f"- {medicine.name} ({medicine.price:.2f} $.)")
            found = True
    if not found:
        print("No medicine found")

def low_stock_array():
    low_stock = [medicine for medicine in pharmacy_inventory if medicine.quantity < MEDICINE_QUANTITY]
    if not low_stock:
        print("No medicines below the quantity of 10")
    else:
        for medicine in low_stock:
            print(medicine)
        return low_stock


def expiring_array():
    date_str = input("Expiry date: (YYYY-MM-DD): ")
    target_date = datetime.strptime(date_str, "%Y-%m-%d")

    expiring_medicines = [{"name" : medicine.name,
                           "quantity" : medicine.quantity}
                          for medicine in pharmacy_inventory
                          if medicine.expiry_date == target_date]
    if not expiring_medicines:
        print(f"No medicines that are expiring on {date_str}")
    else:
        for medicine in expiring_medicines:
            print(f"Medicine name {medicine['name']},"
                  f"Quantity {medicine['quantity']}")
    return expiring_medicines

def menu():
    while True:
        print("\nPharmacy Menu\n")
        print("1. Add medicine\n")
        print("2. Display all data\n")
        print("3. Show medicines with price above 5$\n")
        print("4. Show medicines with quantity below 10\n")
        print("5. Expiring medicines on a given date\n")
        print("6. Exit\n")
        choice = input("Choice: ")


        match choice:
            case "1":
                add_medicine()
            case "2":
                show_medicines()
            case "3":
                print_expensive_medicines()
            case "4":
                low_stock_array()
            case "5":
                expiring_array()
            case "6":
                break
            case _:
                print("Invalid choice")
menu()
