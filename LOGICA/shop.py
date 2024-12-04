from LOGICA.item import Item


class Shop:
    def __init__(self):
        self.items = [
            Item('Special', 9999999),
            Item('New SFX', 500),
            Item('New Music', 500),
            Item('New Level', 500),
            Item('Level Creator', 500),
            Item('New Wallpaper', 1000),
        ]
        self.money = 0
        self.purchased_items = []
        self.load_data()

    def addMoney(self, amount):
        self.money += amount
        self.save_data()

    def buy(self, index):
        if index < len(self.items) and self.money >= self.items[index].price:
            item = self.items[index]
            if item not in self.purchased_items:
                self.money -= item.price
                self.purchased_items.append(item)
                self.save_data()
                return True
        return False

    def save_data(self):
        with open("data.txt", "w") as file:
            file.write(f"Money:{self.money}\n")
            for item in self.purchased_items:
                file.write(f"{item.name},{item.price}\n")

    def load_data(self):
        try:
            with open("data.txt", "r") as file:
                lines = file.readlines()
                self.money = int(lines[0].strip().split(":")[1])
                self.purchased_items = []
                for line in lines[1:]:
                    name, price = line.strip().split(',')
                    for item in self.items:
                        if item.name == name:
                            self.purchased_items.append(item)
                            break
        except FileNotFoundError:
            pass

    def is_item_purchased(self, item_name):
        return any(item.name == item_name for item in self.purchased_items)
