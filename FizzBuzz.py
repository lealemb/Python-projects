#if the given number is divisible by 3 is Fizz and divisible by 5 is Buzz 
# and divisible by both is FizzBuzz
for i in range(1,30):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
            print ("Fizz")
    elif i % 5 == 0:
            print("Buzz")
    else:
            print (i)
