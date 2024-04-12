def divide(a, b):
    assert b != 0, "Zero division error"
    return a / b


result = divide(10, 2)
print(result)

result = divide(10, 0)

###########


def square(x):
    return x * x


assert square(2) == 4
assert square(3) == 9
assert square(4) == 15


###########

def get_age(age):
    assert age >= 0, "Age cannot be negative"
    return age


age = get_age(25)
print(age)

age = get_age(-5)


###########

def get_first_element(lst):
    assert len(lst) > 0, "List is empty"
    return lst[0]


numbers = [1, 2, 3]
first = get_first_element(numbers)
print(first)

empty_list = []
first = get_first_element(empty_list)
