# writing to csv

import csv

fields = ['Journal title', 'ISSN', 'Year', 'Total pdf downloads']

rows = [['Oncology', '1234-4321', '2021', '999'],
        ['Lung cancer', '3333-4444', '2021', '657'],
        ['Palliative care', '4532-7896', '2021', '345'],
        ['Ovarian cancer', '9854-3765', '2021', '475']]

filename = "journalusage.csv"

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
