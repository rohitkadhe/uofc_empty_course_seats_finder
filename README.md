# Uofc Empty Course Seats Notifier

- Objective of this project automate the process of checking if courses at the University of Calgary (Uofc) have empty seats

## Prerequisites 

- Ensure you have python installed
- Ensure you have pip3 installed 
- Download selenium by using 'pip3 install selenium' 
- Ensure you have the correct 'chrome driver' installed which currently is for version 85.0

## Running the project
- Navigate to the courses folder and open the courses text file
- Terms have to be in the following format: "'year' (Fall, Winter, Spring, Summer)"
- Courses have to be in the follwing format: "'course code' 'course number'"
- Example courses file:<br/>
  Course Name, Term<br/>
  ENCM 467, 2020 Fall<br/>
  ENCM 511, 2020 Fall<br/>
  ENEL 471, 2021 Winter<br/>
- Open a terminal of choice in the project directory and type 'python3 empty_course_seats_notifier' to run the project
- A results text file will be generated and opened in the same folder. This file will let you know which courses have empty seats and which courses are full.
