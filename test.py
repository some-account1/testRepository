class Clothes:

    def __init__(self, name):
        self.name = name

    def buy(self):
        print("Thank you for buying this" + self.name)

        shirt = Clothes("shirt")
        shirt.buy()
