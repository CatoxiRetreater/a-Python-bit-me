import csv

def append_to_csv_file(data):
    
    with open('test.csv', 'a', newline='') as file:
        
        csv_writer = csv.writer(file)
        csv_writer.writerow(data)
        data='Hello' 
append_to_csv_file()
