n = int(input("number to check: "))

# write a function that checks if a number is prime or not


def prime_checker(number):

    if number % 2 == 1:
        if number / 3 != 1 or number / 7 != 1 or number / 5 != 1:

            print(f"{number} is a not prie nuber")
        else:
            print(f"{number} is  a prime number")


prime_checker(n)
