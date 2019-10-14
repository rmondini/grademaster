# grademaster

### Project to manage grades of a class (e.g. freshman-level physics class) given input file of students' names and IDs.    

The code is written in Python 2. The chosen data structure is a list where each element of the list is an object of the class StudentRecord and represents a student. Each StudentRecord object contains all the relevant information for that student (name, ID, grades etc).  

The code is organized as follows:  
- "StudentRecord.py" contains the definition and implementation of the StudentRecord class.
- "lib_grademaster.py" contains functions that are used in the main file.
- "grademaster.py" is the main file. Contains the main function and some global variables.  

Different input files (in csv format) are provided:  
- "grade_dummy_file.csv" represents the class at the end of the semester (each student has completed 10 homeworks, 2 midterms, and the final exam).
- "grade_dummy_file_short.csv" is the same as "grade_dummy_file.csv" but with only 11 students in the class.
- "grade_dummy_file_short_nofinal.csv" represents the (smaller) class before the final exam is taken.
- "grade_dummy_file_short_nohw.csv" represents the class at the beginning of the semester, i.e. contains only students' names and IDs.
- "grade_dummy_file_short_nomt2.csv" represents the class before the second midterm is taken.
- "grade_dummy_file_short_notests.csv" represents the class before the first midterm is taken and only 8 homework assignments have been completed.

The code is run by executing the main file with one of the input files. For instance:  
./grademaster.py grade_dummy_file.csv  

It generates the output file "output.csv", which is an updated version of the input file containing total grades and letter grades for all students.  

Features of the code:  
- Computes total grade for each student given specified weight of each grade component (homeworks, midterm 1, midterm 2, final) (the weight of each component can be modified at the beginning of the "grademaster.py" file)  
- Given input file, determines how far into the semester the class is and computes total grades accordingly 
- Ranks students in the class and assigns letter grades based on a specified curve (the curve can be modified in the "rank_students" function)
- Determines numerical-grade-to-letter-grade conversion after class ranking and letter-grade assignment  
- Writes out updated file in csv format containing total grades and letter grades 
- Can compute class average (for midterms, final, or total grade) 
- Can draw histogram of grades (for midterms, final, or total grade)
- Can look up students by student ID and print out their student record
- Handles exceptions/errors (e.g. no input file, incomplete input file, no match for student ID etc)
