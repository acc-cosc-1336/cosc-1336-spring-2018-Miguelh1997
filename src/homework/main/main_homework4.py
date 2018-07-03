#write the import statements to bring in homework 4 functions
#valid_letter_grade, get_credit_points, get_grade_points, and get_grade_point_average
from src.homework.homework4 import (valid_letter_grade, get_credit_points,
                       get_grade_points, get_grade_point_average)
'''
Use the functions from homework4 to...
Write code to prompt the user for number of students and grades.
Create a nested loop to collect letter grades and credit hours for each student.
Vaidate the letter grade is in accepted range if not prompt user for letter again.
From the letter grade, get the credit points for that class.
Calculate grade points (How? Research GPA calculation).
Sum grade points and credit hours for each student.
Calculate GPA for each student.
Display Student 1(etc) GPA is 3.77. Format the GPA to two values.
'''

#WRITE YOUR CODE IN THE MAIN FUNCTION BELOW
# Function below is used to calculate gpa using other functions
def main():
    num_students = int(input('Number of students: '))
    total_credit = 0
    total_grade_points = 0

    #Running a loop for each of the students that was entered by the user.

    for i in range(1,num_students+1):
        course = int(input('How many classes did student ' + str(i) + ' take: '))
        total_credit = 0
        total_grade_points = 0

        #Running a loop that will ask for a grade and number of credits
        #for each course in student[i] given by the user.
        
        for x in range(1,course+1):
            grade = input('Enter letter grade for class #' + str(x) + ': ' )

            #Validating that the letter given agrees with Valid_letter_grade function

            
            while valid_letter_grade(str(grade)) != True:
                grade = input('Please give a valid letter! (a,b,c,d,f) ')
                
            grade = get_credit_points(grade)
            credit_hour = int(input('How many credits was class #' +str(x) + ': ' ))
            total_credit += credit_hour 
            grade_points = get_grade_points(credit_hour, grade)
            total_grade_points += grade_points
            gpa = get_grade_point_average(total_credit, total_grade_points)
        print('\nStudent ' +str(i) + ' GPA is: ' + "%.01f\n" % gpa)
                   
          
main()
                 

                            
    
            
                
                        
            
        
    






#CALL THE MAIN FUNCTION
