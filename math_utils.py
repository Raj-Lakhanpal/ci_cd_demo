# math_utils.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def med(digits):
    counter = 0
    total = 0

    for i in digits:
        counter +=1
        total+=i;
    return  total/counter


def bill_after_discount(total_Price, discount_percentage):
    discount_price = total_Price * (discount_percentage / 100)
    return  total_Price - discount_price
