## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR get_grade() FUNCTION GOES HERE ####
def get_grade(m):
    m = round(m)
    if m >= 90: return "A+"
    elif m >=86: return "A"
    elif m >= 82: return "A-"
    elif m >= 78: return "B+"
    elif m >= 74: return "B"
    elif m >= 70: return "B-"
    elif m >= 66: return "C+"
    elif m >= 62: return "C"
    elif m >= 58: return "C-"
    elif m >= 54: return "D+"
    elif m >= 50: return "D"
    elif m >= 0: return "F"
#### End OF MARKER


#### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ####
def calculate_sgpa(a, b, c):
    grade_table = {
        "A+" : 4.00,
        "A" : 4.00,
        "A-" : 3.67,
        "B+" : 3.33,
        "B" : 3.00,
        "B-" : 2.67,
        "C+" : 2.33,
        "C" : 2.00,
        "C-" : 1.67,
        "D+" : 1.33,
        "D" : 1.00,
        "F" : 0.00,
        "nothing" : 0.00
    }
    sgpa = (grade_table[a] + grade_table[b] + grade_table[c]) / 3
    return round(sgpa, 2)
#### End OF MARKER


if __name__ == '__main__':
    print(get_grade(50))
    print(calculate_sgpa('A', 'B', 'nothing'))
