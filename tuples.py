# tuples are immutable

three_numbers = (1,2,3)
print(three_numbers)
#three_numbers[0] = 4    # this will throw an error as tuples are immutable

print(len(three_numbers))
print(three_numbers[1])

# tuple unpacking
first, second, third = three_numbers
print(first)
print(second)
print(third)