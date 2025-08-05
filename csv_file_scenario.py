import csv

FILENAME = "track_of_everything"

def initialize_csv(filename):
    try:
        with open(filename, 'x') as f:
            r = csv.reader(f)
            for row in r:
                print(row)



    
