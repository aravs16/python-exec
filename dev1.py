from bank_class import Bank

# from bike import Bike

c1 = Bank("act1", 0, 10, "pan1")
c2 = Bank("act2", 0, 100, "pan2")

c1.deposit(1000)

print(c1.balance, c2.balance)


# harley       = Bike("Harley", 750, 30, "blue")
# splendor     = Bike("Splendor", 150, 90, "red" )

# print(harley.mileage > splendor.mileage)

