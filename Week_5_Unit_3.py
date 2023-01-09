def is_even(number):
    return number % 2 == 0
for i in range(100):
    if is_even(i) == True:
        print(f"{i} is even")
    else:
        print(f"{i} is not even")
