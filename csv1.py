import csv

def read_csv_file():
    with open('test.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
            
read_csv_file()
