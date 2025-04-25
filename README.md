# PythonCodingChallenges

Welcome to PythonCodingChallenges! This repository contains a collection of coding challenges for Python.

## Instructions

To utilize the challenges, follow these steps:

1. Clone or download this repository to your local machine.
2. Navigate to the challenge directory you want to work on (e.g., `challenge1`).
3. Open the `challenge.py` file in the chosen challenge directory.
4. Edit the code in the `challenge.py` file to solve the challenge.
5. Save the changes.

## Validation

To validate your solution, follow these steps:

1. Open the `test.py` file in the same challenge directory.
2. Run the `test.py` file to execute the test cases against your solution.
3. Check the output to see if your solution passes the tests.

## Challenges

Here is an index of all the challenges available in this repository:

### Challenge 1


In this challenge you will write a function called update_employee_database() to parse a CSV file that includes an employee database (stored at employee.csv). This database has five columns:
    * Employee Name (String)
    * Employee ID (alphanumeric String)
    * Employee Tenure (integerr indicating years of service)
    * Employee Birth Date (date in YYYY-MM-DD format)

Write a function that delivers the following:
- Open up the employee.csv file and update Jane Smith's last name to indicate her recent marriage to John Doe.
- Append a new employee to the database with the following information:
    * Bill Murray
    * F12345
    * 0
    * 1984-09-13


### Challenge 2



In this challenge you will write a function called test_https(). test_https will take two parameters:
    1. port_list which is a list of TCP ports that the function will test
    2. target_host which is a string that identifies the target host.

The function should return a list of tuples. Each tuple should contain the port number and a boolean value indicating whether the port is open or closed.

*** BONUS POINTS *** 

SEnsure the function correctly validates IP addresses before attempting to connect to them.



### Challenge 3



Write a function called "find_action_movies() that searches the json db located at moviedb.json and returns a list of tuples including the Title and Year of all movies in the horror genre.

### Challenge 4

Write a function called analyze_logs() that will analyze the json webserver logs in the access_logs.log file. This file is stuctured data in the JSON format. Return a list of all log entries where the timestamp occurs before January 3 2015.

Feel free to explore each challenge and have fun coding!