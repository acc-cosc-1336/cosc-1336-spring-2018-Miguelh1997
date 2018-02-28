#write import statements for homework 6 functions
from src.homework.homework6 import (get_point_mutation, get_dna_complement, transcribe_dna_into_rna, get_gc_content)

def menu_options():
    print()
    print('1) Point Mutations')
    print('2) DNA Complement')
    print('3) DNA to RNA')
    print('4) GC Content')
    print('5) DNA motif')
    print('6) Most likely Ancestor')
    print('7) Exit')
    print()

def run_menu():

    option = -1

    while option != 7:
        menu_options()
        option = int(input("Enter menu choice: "))

        while option < 1 or option > 7:
            print("Valid menu range 1-7")
            option = int(input("Enter menu choice: "))

        if option == 1:
            handle_option_1()
        elif option == 2:
            handle_option_2()
        elif option == 3:
            handle_option_3()
        elif option == 4:
            handle_option_4()
        elif option == 5:
            handle_option_5()
        elif option == 6:
            handle_option_6()


def handle_option_1():
   
    n = 'Y'
    while n == 'Y':
        string1 = input("Enter a 10 character DNA string in range (A,C,G,T): ")
        string2 = input("Enter another 10 character DNA string in range (A,C,G,T): ")
        result = get_point_mutation(string1.upper(),string2.upper())
        print(result)
        n = input("Press 'y' to enter another set of information... ")
        n = n.upper()
    

def handle_option_2():
  
    file = open('dna_complement.dat','r')
    for n in file:
        result = get_dna_complement(n)
        print(result)

def handle_option_3():
   
    file = open('transcribe_dna_to_rna.dat','r')
    for n in file:
        result = transcribe_dna_into_rna(n)
        print(result)

def handle_option_4():
   
    file = open('compute_gc_content.dat','r')
    for n in file:
        result = get_gc_content(n)
        print(result)
    

def handle_option_5():
    pass #optional 

def handle_option_6():
    pass #optional
