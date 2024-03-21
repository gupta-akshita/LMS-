class Product:
    def __init__(self, name, description, price, stockLevel):
        self.name = name
        self.description = description
        self.price = price
        self.stockLevel = stockLevel

    def __eq__(self, other):
        return (self.name == other.name and self.description == other.description and
                self.price == other.price and self.stockLevel == other.stockLevel)

    def __hash__(self):
        return hash((self.name, self.description, self.price, self.stockLevel))


class ShoppingCart:
    def __init__(self):
        self.products = []

    def addProduct(self, product):
        self.products.append(product)

    def removeProduct(self, product):
        self.products.remove(product)

    def totalCost(self):
        return sum(p.price for p in self.products)


class Customer:
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email

    def __eq__(self, other):
        return self.name == other.name and self.address == other.address and self.email == other.email

    def __hash__(self):
        return hash((self.name, self.address, self.email))


class Inventory:
    def __init__(self):
        self.products = {}

    def addProduct(self, product, stock):
        self.products[product] = stock

    def updateStock(self, product, stock):
        self.products[product] = stock

    def isInStock(self, product):
        return self.products.get(product, 0) > 0

    def restock(self, product, quantity):
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity


class Payment:
    def __init__(self, amount, paymentMethod):
        self.amount = amount
        self.paymentMethod = paymentMethod


class Shipping:
    def __init__(self, shippingMethod, shippingCost):
        self.shippingMethod = shippingMethod
        self.shippingCost = shippingCost


class Order:
    def __init__(self, customer, products, totalCost, payment, shipping):
        self.customer = customer
        self.products = products
        self.totalCost = totalCost
        self.payment = payment
        self.shipping = shipping

    def __eq__(self, other):
        return self.customer == other.customer and self.products == other.products and self.totalCost == other.totalCost


class Admin:
    def __init__(self):
        self.inventory = Inventory()
        self.products = []
        self.customers = []
        self.orders = []

    def addProduct(self, product):
        self.products.append(product)

    def updateProduct(self, product):
        for i, p in enumerate(self.products):
            if p == product:
                self.products[i] = product
                break

    def updateStockLevel(self, product, stockLevel):
        product.stockLevel = stockLevel  # Assuming you have access to modify the product directly

    def addOrder(self, order):
        self.orders.append(order)

    def updateOrder(self, order):
        for i, o in enumerate(self.orders):
            if o == order:
                self.orders[i] = order
                break

    def addCustomer(self, customer):
        self.customers.append(customer)

    def updateCustomer(self, customer):
        for i, c in enumerate(self.customers):
            if c == customer:
                self.customers[i] = customer
                break


if __name__ == "__main__":
    p1 = Product("iPhone", "New iPhone", 999.99, 10)
    inventory = Inventory()
    inventory.addProduct(p1, 10)

    c1 = Customer("John Smith", "123 Main St", "johnsmith@email.com")
    cart = ShoppingCart()
    cart.addProduct(p1)

    if inventory.isInStock(p1):
        print("Product is in stock")
    else:
        print("Product is out of stock")

    print(f"Total cost: Rs{cart.totalCost()}")

    payment = Payment(cart.totalCost(), "Credit Card")
    print(f"Payment amount: Rs{payment.amount}")
    print(f"Payment method: {payment.paymentMethod}")
