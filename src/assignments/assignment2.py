def faculty_evaluation_result(nev, rar, som, oft, voft, alw):
    

    total = alw + voft + oft + som + rar + nev
    alw_ratio = alw / total
    voft_ratio = voft / total
    oft_ratio = oft / total
    som_ratio = som / total
    rar_ratio = rar / total
    nev_ratio = nev / total




    
    if (alw_ratio + voft_ratio) >= .9:
        return 'Excellent'
    elif (alw_ratio + voft_ratio + oft_ratio) >= .8:
        return 'Very Good'
    elif (alw_ratio + voft_ratio + oft_ratio + som_ratio) >= .7:
        return 'Good'
    elif (alw_ratio + voft_ratio + oft_ratio + som_ratio + rar_ratio) >= .6:
        return 'Needs Improvement'
    else:
        return 'Unacceptable'
    
    




    
def get_ratings(nev,rar,som, oft,voft, alw):
    '''
    Students aren't expected to know this material yet!
    '''
    ratings = []
    total = nev + rar + som + oft + voft + alw

    ratings.append(round(alw / total, 2))
    ratings.append(round(voft / total, 2))
    ratings.append(round(oft / total, 2))
    ratings.append(round(som / total, 2))
    ratings.append(round(rar / total, 2))
    ratings.append(round(nev / total, 2))

    return ratings
    

    
