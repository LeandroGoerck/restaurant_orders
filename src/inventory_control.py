class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.orders = []

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_quantities_to_buy(self):

        list_with_quantity_zero = dict()
        for item in self.MINIMUM_INVENTORY:
            list_with_quantity_zero.update({item: 0})

        products_to_buy = list_with_quantity_zero

        for order in self.orders:
            product = order[1]

            for item in self.INGREDIENTS[product]:
                products_to_buy[item] += 1

        return products_to_buy
