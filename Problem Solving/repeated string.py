def repeatedString(s, n):
    
    coeff = int(n/len(s))
    count_a = s.count('a') * (coeff)
    count_a += (s[:n - coeff*len(s)]).count('a')
    return count_a
