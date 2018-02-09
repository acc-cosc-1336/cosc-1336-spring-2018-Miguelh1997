from src.assignments.assignment4 import factorial
def main():
    while True:
        number = int(input("give a number to loop: "))
        result = factorial(number)
        print(result)
        n = input("Press 'y' if you want to keep looping: ")
        if n != 'y':
            break
    '''
    Create a loop that'll run until the user doesn't type the letter 'y'
    In the loop,
    Capture one number from the keyboard and validate for a range between 1 and 10.
    Call the factorial function.
    Save the result to a variable.
    Print the variable value.

    Ask the user if they want to continue.

    TO RUN YOUR PROGRAM GO TO IN PYTHON IDLE RUN->RUN MODULE.
    IN THE PYTHON SHELL TYPE main()

    DON'T ADD A RETURN STATEMENT TO THIS FUNCTION
    '''
#another option to run the program is to call the main() function below and Run->Run Module
