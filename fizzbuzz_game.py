for number in range(1,101):
    if number % 3 == 0  and number % 5 == 0:
        print("FizzBuzz")
    if number % 3 == 0 :
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else :
        print(f"{number}")

#  Always keep the condition which is intersection of two other condition above them