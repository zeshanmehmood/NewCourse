## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR is_prime() FUNCTION GOES HERE ####
def is_prime(num):
    y = int(num)
    if y < 1: return False
    if y == 1: return True
    if y == 2: return True
    x = 2
    while x < y:
        if y%x == 0: return False
        x += 1

    return True
#### End OF MARKER


#### YOUR CODE FOR output_factors() FUNCTION GOES HERE ####
def output_factors(num):
    y = int(num)
    for x in range(1, y+1):
        if y%x == 0: print(x)
#### End OF MARKER


#### YOUR CODE FOR get_largest_prime() FUNCTION GOES HERE ####
def get_largest_prime(num):
    y = int(num)
    if y <= 1: return None
    for x in range(y, 1, -1):
        if is_prime(x): return x
    return None
#### End OF MARKER


if __name__ == '__main__':
    print(is_prime(499))  # should return True

    print(get_largest_prime(10))  # should return 7
    # print get_largest_prime(100000)  # bonus, try with 100k

    output_factors(10)  # should output -- 1 2 5 10 -- one on each line
