def recMC(coinVolnelist,change,knowresults):
    minCoin=change
    if(change in coinVolnelist):
        knowresults[change]=1
        return 1
    elif(knowresults[change]>0):
        return  knowresults[change]
    else:
        for i in [c for c in coinVolnelist if (c<=change)]:
            numCoin=1+recMC(coinVolnelist,change-i,knowresults)
            if(numCoin<minCoin):
                minCoin=numCoin
                knowresults[change]=minCoin
    return minCoin

a=recMC([1,5,10,25,50],40,[0]*41)
print(a)