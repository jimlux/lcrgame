#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Simulate LRC game
Actually called Left, Center, Right - LCR Dice game.

https://www.georgeandcompany.co/collections/left-center-right

Playing with standard dice and poker chips:
https://bicyclecards.com/how-to-play/left-center-right/

Created on Mon Dec 27 10:33:26 2021

@author: jimlux
"""
import random
import matplotlib.pyplot as plt
import numpy as np

def printall():
    """ utility function to create a string of all the Money contents """
    s=""
    for d in Money:
        s += " %d"%d
    return (s)

Nplayers = 8

plt.figure()        # for the game progress

rounds = []

ngames = 1000
for game in range(ngames):
    


    Money = np.zeros(Nplayers,dtype=int)
    for i in range(Nplayers):
        Money[i]=4
    wallets  =np.zeros((1,Nplayers),dtype=int)
    wallets[0]=Money
    #print (wallets)
    center = 0
    printdetail = False
    nnzero=[]
    for round in range(30):
        s1  = "Round %2d - %3d - %s"%(round,center,printall())
        nzero = 0
        for player in range(Nplayers):
            
            if printdetail: 
                print ("Player %d - %d - %s"%(player,center,printall()))
                
            """ turn """
            ndice = min(3,Money[player])
            if ndice == 0:
                if printdetail: 
                    print("Pass")
                nzero += 1
            for i in range(ndice):
                
                dieside = random.randrange(6)
                if dieside == 0:  #LEFT
                    playerleft = player -1
                    if playerleft <0:
                        playerleft = Nplayers-1
                    Money[playerleft] += 1
                    Money[player] -= 1
                    if printdetail: 
                        print("L %s"%printall())
            
                if dieside == 1:    #RIGHT
                    playerright = player + 1
                    if playerright >= Nplayers:
                        playerright = 0
                    Money[playerright] += 1
                    Money[player] -= 1
                    if printdetail: 
                        print("R %s"%printall())
                    
                if dieside == 2:  #CENTER
                    Money[player] -= 1
                    center += 1
                    if printdetail: 
                        print("C %s"%printall())
            wallets=np.append(wallets,[Money],axis=0)
            #print(Money)
            #print (wallets)

        
        #print("%s nz %d"%(s1,nzero))
        nnzero.append(Nplayers-nzero)
        if nzero >= Nplayers-1:
            break
    plt.plot(nnzero)
    rounds.append(len(nnzero))

plt.ylabel('remaining players')
plt.xlabel('round')
plt.title("%d players"%len(Money))


plt.figure()
plt.hist(rounds,bins=range(max(rounds)+1),density=True)
plt.xlabel('Rounds')
plt.ylabel("Probability")
plt.title("%d players"%len(Money))



from matplotlib.ticker import MaxNLocator

ax = plt.figure().gca()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
for i in range(Nplayers):
    plt.plot(wallets)
leg  =[]
for i in range(Nplayers):
    leg.append("Player %d"%(i+1))
plt.legend(leg)
plt.ylabel('wallet contents')
plt.xlabel('roll #')
plt.grid()
