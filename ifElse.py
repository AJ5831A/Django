x = int(input("Enter a number: "))

# if x%2 ==0 and x%3 == 0:
#     print(x,"is divisible by 2, 3 and 6")
# elif x%2 == 0:
#     print(x,"is divisible by 2")
# elif x%3 == 0:
#     print(x,"is divisible by 3")
# else:
#     print(x,"is not divisible by 2, 3 and 6")

count = 0

for i in range (1,x+1):
    if x%i == 0:
        count = count + 1

if count == 2:
    print(x,"is prime")
else:
    print(x,"is not prime")    

