#write the import statements for homework5 functions
from src.homework.homework5 import write_sales_data, read_sales_data

#With the functions created in homework5...
#Prompt user for number of sales records to input.
#Open a file for text writing.
#Iterate and prompt user for item name and price.
#Save item name and price to file in one line
#Calculate sum of price and write to file
#Calculate average price and write to file

#Open a file for text reading.
#Read the saved file and output table

def main():
    
    while True:
        try:
            sales = int(input('How many sales will you be inputing? '))
            break
        except ValueError:
            print('Invalid character please input a number of sales\n')
    sumPrice = 0
    average = 0
    file = open("items.txt","w")
    for i in range(1,sales+1):
      
        input_item = input("Please give item " + str(i) + " name: ")
        while True:
            try:
                input_price = float(input("please give price of " + str(input_item) +": "))
                break
            except ValueError:
                print('Please input valid number!\n')
        sumPrice += input_price
        average = sumPrice / i
        
        write_sales_data(file, input_item, input_price)

    file.write('\nTotal: ' + str(sumPrice))
    file.write('\nAvg Price: ' + str("%.2f" % average))
        
    file.close()
    
    print(' ')
    print(' ')
    read_sales_data('items.txt')
        
main()
    
