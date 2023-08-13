## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR find_cumulative_marks() FUNCTION GOES HERE ###
def find_cumulative_marks(list):
    if list is None: return None
    new_record = []
    for record in list:
        if record is None: return None
        id = record[0]
        name = record[1]
        total_marks = 0
        for marks in record[2:]:
            if marks is None:
                total_marks += 0
            else:
                total_marks += marks
        new_record.append((id, name, total_marks))
    return new_record
#### End OF MARKER


### YOUR CODE FOR find_top_student() FUNCTION GOES HERE ###
def find_top_student(list):
    new_list = find_cumulative_marks(list)
    max_total_marks = max(record[2] for record in new_list)
    top_student = [(record[0], record[1]) for record in new_list if record[2] == max_total_marks]
    return top_student
#### End OF MARKER


if __name__ == '__main__':
    results = [
        ('p101111', 'Ali Khayam', 64, 78.5, 89, 25, 99),
        ('p101112', 'Mudasser Farooq', 14, 28.5, 83, 76),
        ('p101113', 'Tamleek Ali', 87, None, 1.6)
    ]

    results1 = [
        ('p101111', 'Ali Khayam', 64, 10),
        ('p101112', 'Mudasser Farooq', 50, 24),
        ('p101113', 'Tamleek Ali', 10, 20)
    ]


    print(find_cumulative_marks(results1))
    # output: [('p101111', 'Ali Khayam', 355.5), ('p101112', 'Mudasser Farooq', 201.5), ('p101113', 'Tamleek Ali', 88.6)]

    print(find_top_student(results1))
    # output: ('p101111', 'Ali Khayam')
