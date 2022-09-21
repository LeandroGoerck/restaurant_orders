from multiset import Multiset


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        orders_by_customer = Multiset()
        for order in self.orders:
            person = order[0]
            product = order[1]

            if person == customer:
                orders_by_customer.add(product)

        return max(orders_by_customer.distinct_elements(),
                   key=lambda x: orders_by_customer[x])

    def get_never_ordered_per_customer(self, customer):
        all_orders = set()
        orders_by_customer = Multiset()
        for order in self.orders:
            person = order[0]
            product = order[1]

            if person == customer:
                orders_by_customer.add(product)
            all_orders.add(product)

        return (all_orders - orders_by_customer.distinct_elements())

    def get_days_never_visited_per_customer(self, customer):
        all_days = set()
        days_by_customer = Multiset()
        for order in self.orders:
            person = order[0]
            day = order[2]

            if person == customer:
                days_by_customer.add(day)
            all_days.add(day)

        return (all_days - days_by_customer.distinct_elements())

    def get_busiest_day(self):
        order_by_days = Multiset()
        for order in self.orders:
            day = order[2]

            if day not in order_by_days:
                order_by_days.add(day)

            order_by_days.add(day)

        return max(order_by_days.distinct_elements(),
                   key=lambda x: order_by_days[x])

    def get_least_busy_day(self):
        order_by_days = Multiset()
        for order in self.orders:
            day = order[2]

            if day not in order_by_days:
                order_by_days.add(day)

            order_by_days.add(day)

        return min(order_by_days.distinct_elements(),
                   key=lambda x: order_by_days[x])
