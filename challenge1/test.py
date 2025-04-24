import challenge as challenge
import csv as csv

def test_update_employee_database():
    # Call the function to update the employee database
    challenge.update_employee_database()

    # Verify that Jane Smith's last name has been updated
    with open('/Users/adampintoro/Code/PythonCodingChallenges/challenge1/employee.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == 'Jane Doe':
                assert row[1] == 'B67890'
                assert row[2] == '5'
                assert row[3] == '1985-10-20'
                break
        else:
            assert False, "Jane Doe not found in the employee database"
    
    # Verify that the new employee has been added
    with open('/Users/adampintoro/Code/PythonCodingChallenges/challenge1/employee.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == 'Bill Murray':
                assert row[1] == 'F12345'
                assert row[2] == '0'
                assert row[3] == '1984-09-13'
                break
        else:
            assert False, "Bill Murray not found in the employee database"
    
    print("Test successfully completed!")

test_update_employee_database()