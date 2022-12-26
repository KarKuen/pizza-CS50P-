import sys
from tabulate import tabulate
import csv

if len(sys.argv) == 2:
    if sys.argv[1].endswith('.csv'):
        try:
            with open (sys.argv[1]) as file:
                rows = csv.DictReader(file)
                menu = []
                for row in rows:
                    menu.append(row)
                print(tabulate(menu, headers = 'keys', tablefmt='grid'))

        except FileNotFoundError:
            sys.exit('File does not exist')
    else:
        sys.exit('Not a CSV file')


elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')

else:
    sys.exit('Too few command-line arguments')