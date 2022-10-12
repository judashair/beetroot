class Product:
    def __init__(self, type_: str, name: str, price: float):
        self.type_ = type_
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = {}
        self.category = {}
        self.income = 0

    def add(self, product, amount):
        self.products[product.name] = {"amount": amount, "price": product.price * 1.3, "discount": 0,
                                       "type": product.type_}

        if self.category.get(product.type_):
            if product.name not in self.category[product.type_]:
                self.category[product.type_].append(product.name)
        else:
            self.category[product.type_] = [product.name]

    def get_income(self):
        '''
        Returnsamount of money earned by ProductStore instance.
        '''
        print("Product store total income:", round(self.income, 2))

    def get_income_from_sell(self, product_name, amount):
        '''
        Returns amount of many earned by ProductStore instance.
        '''
        provider_price = self.products[product_name]['price'] / 1.3
        current_product_price = self.products[product_name]['price'] * (
                    100 - self.products[product_name]['discount']) / 100
        current_product_price = round(current_product_price, 2)
        income = (current_product_price - provider_price) * amount
        self.income += income

    def sell_product(self, product_name, amount):
        if product_name in self.products:
            store_product_amount = self.products[product_name]["amount"]
            if store_product_amount >= amount:
                self.products[product_name]["amount"] -= amount
                self.get_income_from_sell(product_name, amount)
            else:
                raise Exception(f"Amount in store is {store_product_amount} and you tried to sell {amount}")
        else:
            raise Exception(f"There is no {product_name} in store")

    def get_all_products(self):
        for index, product_name in enumerate(self.products, start=1):
            print(f"""
                №{index}
                Product name: {product_name}
                Produtct type: {self.products[product_name]["type"]}
                Price: {self.products[product_name]["price"]}
                Discount: {self.products[product_name]["discount"]}
                Amount in store: {self.products[product_name]["amount"]}
                """.replace(" " * 16, ""))  # 16 - number of spaces before phrace replaced on ""

    def get_product_info(self, product_name):
        if product_name in self.products:
            amount = self.products[product_name]["amount"]
            return (product_name, amount)

    def set_discount(self, identifier, percent, identifier_type="name"):
        if not 0 <= percent < 100:
            raise Exception(f"You cannot apply such discount: {percent}")

        if (identifier_type == "name") or (identifier_type == "category"):
            if identifier_type == "name":

                if not identifier in self.products:
                    raise Exception(f"No {identifier} in products")

                self.products[identifier]["discount"] = percent

            else:

                if not identifier in self.category:
                    raise Exception(f"No {identifier} in category")

                product_names = self.category[identifier]
                for product_name in product_names:
                    self.products[product_name]["discount"] = percent

        else:
            raise Exception(f"No such identifier type: '{identifier_type}'")


s = ProductStore()
p1 = Product('Food', 'Ramen', 10)
p2 = Product('Food', 'Mivina', 5)
s.add(p1, 10)
s.add(p2, 30)
s.get_income()
s.set_discount("Food", 15, identifier_type="category")
s.sell_product("Ramen", 6)
s.get_income()
s.get_all_products()
s.get_product_info("Ramen")