import csv

# Define the column names
fieldnames = ['Employee Name', 'Employee ID', 'Employee Tenure', 'Employee Birth Date']

# Define the data rows
data = [
    ['John Doe', 'A12345', 3, '1990-05-15'],
    ['Jane Smith', 'B67890', 5, '1985-10-20'],
    ['Mike Johnson', 'C54321', 2, '1995-02-28'],
    ['Sarah Williams', 'D98765', 7, '1980-12-10'],
    ['David Brown', 'E24680', 4, '1992-08-05']
]

# Create a new CSV file
with open('employee.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the column names
    writer.writerow(fieldnames)
    
    # Write the data rows
    writer.writerows(data)