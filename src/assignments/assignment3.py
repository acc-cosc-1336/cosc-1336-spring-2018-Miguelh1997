def decimal_to_binary(number):
    binary = ''

    for i in range(7,-1,-1):
        value = 2 ** i

        if value <= number:
            binary += '1'
            number = number - value
        else:
            binary += '0'

    return binary


def sum_square_of_number(number):
    '''
    USE A FOR LOOP
    Given a number return the sum of all squared number from 1 to the number
    Example given number 3 returns 14.
    Number   Square
    1         1
    2         4
    3         9
    SUM:     14<-- return this value
    :param number:
    :return: the sum of all squares from 1 to the number
        WRITE YOUR CODE AFTER THE THREE QUOTES BELOW

    '''
    sum_of_squares = 0
    for num in range(1,number+1):
        square = num ** 2
        sum_of_squares += square
        
    

    return sum_of_squares

def is_prime(n):
    
    '''
    USE A FOR LOOP
    Given a number return true if prime or false if not prime
    :param number: Any whole number
    :return: True if prime False if not
    PSEUDOCODE
    if number equal 1 return false
    otherwise if number equal 2 return True
    otherwise iterate from 2 to the number itself(create a new variable current_number assign it value of 2)
    if the number divided by current_number remainder is 0 return False HINT: remainder operator
    increment the value of x
    After loop exits return True
    TYPE YOUR CODE AFTER THE THREE QUOTES BELOW
    DON'T FORGET RETURN STATEMENT AT THE END OF THE FUNCTION
    '''
    if n == 1:
        return False
    elif n == 2:
        return True
    
    for i in range(2,n):
        if (n % i) == 0:
            return False
        
    return True

def list_of_primes(n):
    '''
    USE A WHILE LOOP
    Given a number returns all the prime numbers up to the number
    Example given number 10 returns '2,3,5,7,'
    :param n:
    :return:
    Psuedocode:
    Create a new variable names primes and assign it value ''
    loop from 1 to the value of n create a variable current_number and assign it value of 1
    in the loop call is_prime function with an argument of current_number
    if the return value of is_prime is True append current_number to the primes string HINT: Concatenate string
    After loop exits return primes variable
    WRITE YOUR CODE AFTER THE THREE QUOTES BELOW
    '''
    primes = ''
    
    for x in range(1,n):

        if is_prime(x) == True:
            primes = primes + str(x) + ","

    return primes 
            



