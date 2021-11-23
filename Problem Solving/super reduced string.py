def superReducedString(s):
    
    def checkReduced(s) :
        s_copy = copy.deepcopy(s)
        for i in range(1,len(s_copy)) : 
            if s_copy[i] == s_copy[i-1] :
                l_copy = list(s_copy)
                del l_copy[i]
                del l_copy[i-1]
                s_copy = ''.join(l_copy)
                break
        return s_copy
    s_bis = copy.deepcopy(s)
    
    while checkReduced(s_bis) != s_bis :
        s_bis = checkReduced(s_bis)
    if s_bis == '' :
        return 'Empty String'
    else : 
        return s_bis
