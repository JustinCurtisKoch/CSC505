# Module 1: Critical Thinking Assignment
# Get familiar with Python programming and PyCharm (IDE) by writing a simple Python script.

# FizzBuzz. For an integer n, for every positive integer i <= n, the task is to print:
# “Fizz” if i is divisible by 3.
# “Buzz” if i is divisible by 5.
# “FizzBuzz” if i is divisible by 3 and 5.
# “i” as a string, if none of the conditions are true.

def FizzBuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)


FizzBuzz(45)
