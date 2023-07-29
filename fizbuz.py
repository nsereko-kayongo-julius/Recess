import random
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        continue
    elif i % 3 == 0:
        print("Fizz")
        continue
    elif i % 5 == 0:
        print("Buzz")
        continue
    else:
        print(i)

# rando pasword generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E',
           'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
           ]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
caracters = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("welcome to password generator")
myletters = int(input("how many letters would you want in your pasword \n"))
mysybols = int(input("how many symbols would you want in your pasword \n"))
number = int(input("how many numbers would you want in your pasword \n"))


for letters in random.randint(1, myletters+1):
    print(random.choice(letters))

# generated_pasword =
