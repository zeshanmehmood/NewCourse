## IMPORTS GO HERE
from module.a05 import is_prime
## END OF IMPORTS


### YOUR CODE FOR output_prime_factors() FUNCTION GOES HERE ###
def output_prime_factors(num):
    num = round(num)
    if num <= 1: return None
    for x in range(2, num):
        if num % x == 0:
            if is_prime(x): print(x)
#### End OF MARKER


### YOUR CODE FOR get_nth_prime() FUNCTION GOES HERE ###
def get_nth_prime(n):
    if isinstance(n, int) and n >= 1:
        primes = []
        num = 2
        while len(primes) < n:
            if is_prime(num): primes.append(num)
            num += 1
        return primes[-1]
#### End OF MARKER


if __name__ == '__main__':
    output_prime_factors(23)
    print(get_nth_prime(4))
