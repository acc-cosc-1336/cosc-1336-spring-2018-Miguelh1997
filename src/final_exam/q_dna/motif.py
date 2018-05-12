 def non_contigous_motif(val,list1):
    results = []
    s = ''.join(list1)
    l = len(val)

    for i in range(len(s)-l):


        if s[i:i+l] == val:
            results.append(i+1)
    return(results)
