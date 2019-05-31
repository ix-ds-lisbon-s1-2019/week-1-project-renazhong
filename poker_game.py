#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 11:23:25 2019

@author: renazhong
"""

#%%
import sys
import random

first_input = int(sys.argv[1]) #here we use int() to convert the string input into an integer

# now we can use first_input
print(first_input)


def poker(first_input):
    
    ranks = ['2','3','4','5','6','7','8','9','10','J', 'Q', 'K', 'A']
    suits = ['clubs', 'spades', 'hearts', 'diamonds']
    pdict = {}
    drawn = []
    
    for n in range(first_input):
        name = input("What's your name? ")
        pcards = []
        prank = []
        track = 0; 
        while track < 5:
            rank = random.choice(ranks)
            suit = random.choice(suits)
            card = (rank, suit)
            if card not in drawn:
                pcards.append(card)
                drawn.append(card)
                prank.append(rank)
                track += 1
            else:
                continue
        pdict[name] = prank

    # easy version
    newdict = {}
    windict = {}
    conv = {"1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9,
            "10":10,
            "J":11,
            "Q":12,
            "K":13,
            "A":14}
    
    for n in pdict.keys(): #every player 
        intvals = []
        for v in pdict[n]: #hands
            intvals.append(conv[v])
        intvals.sort(reverse = True)
        newdict[n] = intvals
    print("everyone's hands: ", newdict)
    
    winner = ""
    largest = 0;
    for k in newdict.keys():
        mn = newdict[k][0]
        if mn > largest: 
            largest = mn
            winner = k
        elif mn < largest: 
            pass
        else:
            larger = 0;
            for l in newdict.keys():
                mn = newdict[l][1]
        
    return winner

print(poker(first_input))










