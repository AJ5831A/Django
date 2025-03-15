from new import Student
class Person(Student):
    pass # this will create an empty class and will not throw any error
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age

# p1 = Person("Aryan" , 18)
# print(p1.name , p1.age)
p1 = Person()
print(p1.name)