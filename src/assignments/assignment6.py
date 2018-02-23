def get_count_A_C_G_and_T_in_string(dna_string):
    '''
    Create a function named get_count_A_C_G_and_T_in_string with a parameter named dna_string.

    :param dna_string: a DNA string
    :return: the count of As, Cs, Gs, and Ts in the dna_string
    '''

    dna_string = dna_string.upper()
    
    tfind = dna_string.count('T')
    #print("There are:",tfind, "'t's")

    afind = dna_string.count('A')
    #print("There are:",afind, "'a's")

    cfind = dna_string.count('C')
    #print("There are:",cfind, "'c's")
    
    gfind = dna_string.count('G')
    #print("There are:",gfind, "'g's")

    return afind,gfind,cfind,tfind






    

