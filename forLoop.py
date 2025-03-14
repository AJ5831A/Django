# for letter in "BRICKS_LMS":
#     print(letter)

# array = ["Aryan" , "Jakhar"]

# for name in array:
#     for letter in name:
#         print(name + " : " + letter)

my_dict = {
    "name": "Aryan",
    "age": 18,
    "gender": "male",
    "friends": ["physics", "chemistry", "maths"]
}

for key in my_dict:
    print(key)
    
    # Check if the value is a list (or another iterable except string)
    if isinstance(my_dict[key], list):
        for value in my_dict[key]:
            print(value)
    else:
        print(my_dict[key])  # Print directly if not iterable
