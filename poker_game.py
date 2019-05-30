#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 11:23:25 2019

@author: renazhong
"""

#%%
import random

def poker(number_of_players):
    
    ranks = [2,3,4,5,6,7,8,9,10,'J', 'Q', 'K', 'A']
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

        #pdict[name] = pcards
        pdict[name] = prank
        
    return pdict #returns hands of all the players in the game

    # easy version
    
    
    
    
print(poker(5))

