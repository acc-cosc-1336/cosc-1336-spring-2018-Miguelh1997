#write import statement for reverse string function
from exam import reverse_string


'''
10 points
Write a main function to ....
Loop as long as user types y.
Prompt user for a string (assume user will always give you good data).
Pass the string to the reverse string function and display the reversed string

'''
def main():

    n = 'Y'
    while n == 'Y':

        string1 = input('Please input a string: ')
        new = reverse_string(string1)
        print(new)
        


        n = input("Press 'y' to enter another string... ")
        n = n.upper()
