#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 11:23:25 2019

@author: renazhong
"""

#%%
import random

def poker(number_of_players):
    
    ranks = ['2','3','4','5','6','7','8','9','10','J', 'Q', 'K', 'A']
    suits = ['clubs', 'spades', 'hearts', 'diamonds']
    pdict = {}
    drawn = []
    
    for n in range(number_of_players):
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
        
        print (pdict)

    # easy version
    windict = {}
    valdict = {
            "1":1,
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
            "A":14            
            }
    
    for n in pdict.keys(): #every player 
        max = 0
        for v in pdict[n]: #hands
            if valdict[v] >= max:
                max = valdict[v]
        windict[n] = max 
        
    winner = ""
    most = 0
    for k in windict.keys():
        if windict[k] > most:
            most = windict[k]
            winner = k
        elif  windict[k] == most:
            
    return winner
    
print(poker(2))
















