def display_histogram():
    filename = "survey.dat"
    file = open(filename,"r")
    for i in file:
        print(i,'*'*int(i))
    
