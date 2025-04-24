import unittest
import challenge as challenge
import csv as csv

class TestUpdateEmployeeDatabase(unittest.TestCase):
    def test_update_employee_database(self):
        # Call the function to update the employee database
        challenge.update_employee_database()

        # Verify that Jane Smith's last name has been updated
        with open('employee.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == 'Jane Doe':
                    self.assertEqual(row[1], 'B67890')
                    self.assertEqual(row[2], '5')
                    self.assertEqual(row[3], '1985-10-20')
                    break
            else:
                self.fail("Jane Doe not found in the employee database")

        # Verify that the new employee has been added
        with open('employee.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == 'Bill Murray':
                    self.assertEqual(row[1], 'F12345')
                    self.assertEqual(row[2], '0')
                    self.assertEqual(row[3], '1984-09-13')
                    break
            else:
                self.fail("Bill Murray not found in the employee database")

        print("Test successfully completed!")

if __name__ == '__main__':
    unittest.main()