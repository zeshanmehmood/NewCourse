## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ###
def calculate_sgpa(x):
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
    }
    if isinstance(x, list):
        total_grade_points = 0
        for i in x:
            if not i in grade_table: return None
            total_grade_points += grade_table[i]
        sgpa = total_grade_points / len(x)
        return round(sgpa, 2)

    if isinstance(x, str):
        if not x in grade_table:
            return None
        sgpa = grade_table[x]
        return sgpa

    if x is None: return None
#### End OF MARKER


### YOUR CODE FOR calculate_sgpa_weighted() FUNCTION GOES HERE ###
def calculate_sgpa_weighted(grades, credits):
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
        }
    if len(grades) != len(credits): return None
    numerator = 0
    denominator = 0
    for g, c in zip(grades, credits):
        if not g in grade_table: return None
        numerator += grade_table[g]*c
    for c in credits:
        denominator += c
    if denominator == 0: return None
    sgpa = numerator / denominator
    return round(sgpa, 2)
#### End OF MARKER


if __name__ == '__main__':
    print(calculate_sgpa(['A+']))
    # print(calculate_sgpa(['A+', 'B', 'C+', 'A-', 'D+', 'B-']))
    print(calculate_sgpa_weighted(['A+'], [4]))
    # print(calculate_sgpa_weighted(['A+', 'B+', 'C-', 'D'], [3, 2, 4, 1]))
