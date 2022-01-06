# brute force

def climbingLeaderboard(ranked, player):
    dict_ranking = dict()
    ranked_sort = sorted(list(set(ranked)),reverse = True)
    last_score = None
    for i,n in enumerate(ranked_sort) :
        if i == 0:
            dict_ranking[i+1] = range(n,1+10**9)
        else :
            dict_ranking[i+1] = range(n,last_score)
            if i == len(ranked_sort) -1 :
                dict_ranking[i+1+1] = range(0,n)
        last_score = n
        
    player_rank = []
    for i,n in enumerate(player) :
        for j in dict_ranking.keys() :
            if n in dict_ranking[j] :
                player_rank.append(j)
                break
    return player_rank
  
  # complexity reduced
  def climbingLeaderboard(ranked, player):

    leaderboard = sorted(set(ranked), reverse = True)
    l = len(leaderboard)
    
    rank = []
    for a in player:
        while (l > 0) and (a >= leaderboard[l-1]):
            l -= 1
        rank.append(l+1)
    return rank
