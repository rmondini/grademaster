# grademaster

Project to manage grades of a class (e.g. freshman-level physics class) given input file of students' names and IDs.  
The code is organized as follows:  
- "StudentRecord.py" contains the definition and implementation of the StudentRecord class.
- "lib_grademaster.py" contains functions that are used in the main file.
- "grademaster.py" is the main file. Contains main function and some global variables.  

Features of the code:  
- Computes total grade of each student given specified weight of each grade component (homeworks, midterm 1, midterm 2, final)  
- Given input file, determines how far into the semester the class is and computes total grades accordingly 
- Ranks students in the class and assigns letter grades based on a specified curve 
- Determines numerical grade->letter grade conversion after class ranking and letter grade assignment  
- Computes class average (for midterms, final, or total grade) 
- Draws histogram of grades (for midterms, final, or totale grade)
- Looks up and prints out student record by student ID
- Writes out updated file in csv format containing total grades and letter grades 
- Handles exceptions/errors (e.g. no input file, incomplete input file, no match for student ID etc)