def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    # Write code here
    m=min_votes
    C=global_mean
    result=[]
    for item in items:
        v = item[1]
        R = item[0]
        confiance_part = v/(v+m)
        prudence_part = m/(v+m)
        WR = confiance_part*R + prudence_part*C
        result.append(WR)
    return result
        
        
        
        