import csv

file_path = r"D:\csv file reader\global_cars_data.csv"

with open(file_path, "r") as file:
    csv_reader = csv.DictReader(file)
    
    print("Vehicle Details:\n")
    
    for row in csv_reader:
        for key, value in row.items():
            print(f"{key}: {value}")
        print("-" * 30)
    