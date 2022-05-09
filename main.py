import random


def fizzbuzz():
    # sourcery skip: lift-duplicated-conditional, remove-redundant-continue
    user_range = int(input("Range from 1 to "))
    print("\n")

    for fizzbuzz in range(1, user_range+1):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("FizzBuzz")
            continue
        elif fizzbuzz % 3 == 0:
            print("Fizz")
            continue
        elif fizzbuzz % 5 == 0:
            print("Buzz")
            continue
        else:
            print(fizzbuzz)


def info():
    print("=== FizzBuzz Python Coding Challenge ===\n")
    print("======================================================================================================================")
    print('''If the number is divisible by both 3 and 5, the program will print FizzBuzz. 
If it's divisible only by 3, the program will print Fizz, if it's divisible only by 5, the program will print Buzz.
If the number is not divisible by neither 3 nor 5, the program will print the number itself.''')
    print("======================================================================================================================\n")


if __name__ == "__main__":
    info()
    fizzbuzz()
