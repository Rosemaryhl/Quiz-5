#Rosemary Hoffman Quiz 5
#Problem 1
def tire_pressure(pres):
    if pres<28:
        print("Tire pressure is low.")
    else:
        return(None)
tire_pressure(29)
tire_pressure(27)
#Problem 2
def thermostat(temp):
    if temp<=52:
        print("The heater is on.")
    elif 52<=temp<=71:
        print("Heater and AC are off.")
    elif 71<=temp:
        print("AC is on")
    else:
        return(None)

thermostat(52)
thermostat(56)
thermostat(80)
#problem 3
def sweet(fruit):
    if fruit=="banana":
        print("Banana it is!")
    elif fruit=="cherry":
        print("I cherish you!")
    elif fruit=="apple":
        print("I applesolutely like you!")
    elif fruit=="orange":
        print("Orange you glad to see me?")
    elif fruit=="melon":
        print("You are one in a Melon.")
    else:
        return(None)

sweet("banana")
sweet("cherry")
sweet("apple")
sweet("orange")
sweet("melon")
sweet("grape")
