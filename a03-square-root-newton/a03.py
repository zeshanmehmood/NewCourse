## IMPORTS GO HERE

## END OF IMPORTS


#### YOUR CODE FOR sqrt() FUNCTION GOES HERE ####
def sqrt(x, a=1.0,):
    epsilon = 1e-5
    while abs(a*a - x) > epsilon:
        a = improve_guess(a, x)

    return a

#### End OF MARKER


#### YOUR CODE FOR average() FUNCTION GOES HERE ####
def average(n1, n2):
    ave = (n1 + n2) / 2
    return ave
#### End OF MARKER


#### YOUR CODE FOR improve_guess() FUNCTION GOES HERE ####
def improve_guess(a, x):
    a = average(a, x / a)
    return a
#### End OF MARKER


if __name__ == '__main__':
    print(sqrt(36))
