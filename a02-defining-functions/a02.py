## IMPORTS GO HERE
from math import pi
## END OF IMPORTS


#### YOUR CODE FOR get_area GOES HERE ####
def get_area(r):
    a = pi * r * r
    print("The area of the circle with radius ", r, "is ", a)
#### End OF MARKER


#### YOUR CODE FOR output_parameter GOES HERE ####
def output_parameter(r):
    p = 2 * pi * r
    print("The parameter of the circle with radius ", r, "is ", p)
#### End OF MARKER




if __name__ == '__main__':
    get_area(2)
    output_parameter(1.0)
