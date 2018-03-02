#write the import for function for assignment7 sum_list_values
from src.assignments.assignment7 import sum_list_values


def process_list(list):
    print(list,'sum: ',sum_list_values(list))

def main():
    n = 'Y'
    while n == 'Y':
        list2=[]
        name = input('Enter a name: ')
 #       list2.append(name)
        num = int(input('How many numbers will you be inputing? '))
        list2=[] * num

        for n in range(0,num):
            value = input('Give number value: ')
            list2.append(value)
        list2 = [name] + list2
        print(list2)



        n = input("Press 'y' to enter another list..")
        n = n.upper()
main()

    
'''
Create a function named process_list that calls the sum_list_values function.
Prints the list values and the sum of the element in the list as follows:
joe 10 15 20 30 40 sum: 115

Create a main function.
In the function loop as long as user wants to add another list.
Prompt the user for name and append to the list.
Prompt the user for number of numeric values in the list.
Iterate the number of times the user enters and prompt end-user for n numeric values.

Call the main function
--------------------
joe 10 15 20 30 40
bill 23 16 19 22
sue 8 22 17 14 32 17 24 21 2 9 11 17
grace 12 28 21 45 26 10
john 14 32 25 16 89

'''
