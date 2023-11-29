import csv

def write_to_csv_file(data):
    with open('test.csv', 'w', newline='Hello') as file:
        csv_writer = csv.writer(file)
        for row in data:
            csv_writer.writerow(row)
            
write_to_csv_file()
