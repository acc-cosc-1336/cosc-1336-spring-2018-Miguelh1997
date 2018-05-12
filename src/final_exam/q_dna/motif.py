 def non_contigous_motif(val,list1):
    list1 = []

    i=0

    for d in dna:
        go = True
        while i < len(dna_list) and go:

            if d == dna_list[i]:
                list1.append(i+1)
                go = False

            i += 1

    return list1[0], list1[1], list1[2]
