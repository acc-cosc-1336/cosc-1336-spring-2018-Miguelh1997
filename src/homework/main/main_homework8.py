'''
Write a main function to create an empty dictionary and
a user-controlled loop to prompt for a widget name and quantity.
Add the values to the dictionary as key(widget name) and value(quantity) pairs.

After user decides to exit write data to file .

'''


def main():
    dictionary = {}
    file = open('Dictionary.txt', 'w')
    n = 'Y'
    while n == 'Y':
        widget = input('Please input a widget name: ')
        quantity = int(input('What is the quantity of ' + widget + ': '))
        if widget in dictionary:
            dictionary[widget] += quantity
        else:
            dictionary[widget] = quantity
            


        n = input("Press 'y' to enter another widget.. ")
        n = n.upper()
    file.write(str(dictionary))
    file.close()

main()
