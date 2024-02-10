x = ("chinese food", "homestyle food", "jamaican food")
y = list(x)
y[1] = "italian food"
x = tuple(y)

print(x)
