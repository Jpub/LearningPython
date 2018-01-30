class Lunch:
    def __init__(self):                          # Make/embed Customer, Employee
        self.cust = Customer()
        self.empl = Employee()
    def order(self, foodName):                   # Start Customer order simulation
        self.cust.placeOrder(foodName, self.empl)
    def result(self):                            # Ask the Customer about its Food
        self.cust.printFood()

class Customer:
    def __init__(self):                          # Initialize my food to None
        self.food = None
    def placeOrder(self, foodName, employee):    # Place order with Employee
        self.food = employee.takeOrder(foodName)
    def printFood(self):                         # Print the name of my food
        print(self.food.name)

class Employee:
    def takeOrder(self, foodName):               # Return Food, with desired name
        return Food(foodName)

class Food:
    def __init__(self, name):                    # Store food name
        self.name = name

if __name__ == '__main__':
    x = Lunch()                                  # Self-test code
    x.order('burritos')                          # If run, not imported
    x.result()
    x.order('pizza')
    x.result()
