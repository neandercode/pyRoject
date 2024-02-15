car = {
    "brand": "Ford", 
    "model": "Mustang",
    "year": 1989
}

x = car.keys()

print(x) #before the change

car["color"] = "red"

print(x) #after the change