# functions/yield_primes.py
"""
Function to yield primes
"""
def primes(limit):
    """
    Start checking for prime numbers from 2, the smallest prime number.
    The outer loop runs as long as i is less than the given limit.
    For each value of i, the inner loop checks 
    if i is divisible by any number j in the range 2 to i-1.
    If i is divisible by j (i.e., i % j == 0), then i is not a prime number.
    The break statement exits the inner loop early, skipping the else block.
    The else block is part of the for loop and executes only 
    if the loop completes without hitting a break.
    If the inner loop completes without finding any divisor (j) for i, then i is a prime number.
    The yield i statement produces the prime number i as part of the generator.
    After checking whether i is prime, increment i by 1 to check the next number.
    """
    i = 2
    while i < limit:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i
        i += 1
