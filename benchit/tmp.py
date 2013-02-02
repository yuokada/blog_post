def _fizzbuzz(x):
    if   x % 15 == 0: return "FizzBuzz"
    elif x % 5  == 0: return "Buzz"
    elif x % 3  == 0: return "Fizz"
    else: return str(x)
print [_fizzbuzz(x) for x in range(1, 30 +1)]
