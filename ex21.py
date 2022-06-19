def add(a, b):
    return (a + b)

def subtract(a, b):
    return (a - b)

def multiply(a, b):
    return (a * b)

def divide(a, b):
    return (a / b)

age = add(15, 3)
height = subtract(74, 3)
weight = multiply(35, 2)
iq = divide(1000, 5)

print("Age: {}, Height : {}, Weight : {}, IQ : {}".format(age, height, weight, round(iq)))

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print(what)