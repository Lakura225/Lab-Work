"""
Does it work on files where no error checking is needed on the fields

>>> sumRows("rows1.csv") == {'tim': 36.0, 'bob': 11.0, 'anna': 54.0}
True

Does it ignore headers if requested?

>>> sumRows("rows1.csv", header=True) == {'tim': 36.0, 'anna': 54.0}
True

Is it returning the right type of result?
>>> type(sumRows("rows1.csv"))
<class 'dict'>

Does it work on files with empty fields or fields which aren't numbers?

>>> sumRows("rows2.csv") == {'tim': 24.0, 'bob': 11.0, 'anna': 13.0}
True

Does it sum columns correctly?
>>> sumColumns("columns.csv") == {'': 0, 'tim': 5.0, 'bob': 41.0, 'anna': 55.0}
True
"""

# *** DO NOT CHANGE CODE ABOVE THIS LINE ***
# *** DO NOT ADD ANY COMMENTS OF YOUR OWN IN THE SUBMITTED SOLUTION ***

import csv


def sumRows(filename, header=False):
    # Add code here
    dic = {}
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        if header:
            next(reader, None)
        for rows in reader:
            total = 0.0
            for num in range(1, len(rows)):
                if str(rows[num]).isdigit() and rows[num] != '':
                    total += float(rows[num])
            dic[rows[0]] = total

    return dic


def sumColumns(filename):
    # Add code here
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        names = next(reader)
        sums = [0 for _ in names]
        for line in reader:
            for i in range(len(sums)):
                sums[i] += int(0 if line[i] == '' else line[i])
        return dict(zip(names, sums))
