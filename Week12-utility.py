# Jessie555/Week12-utility
# Jessie Fehrenbach
# CSCI 102 - Section C
# Week 11 - Part B
import string
def PrintOutput(string):
    print('OUTPUT ', string)

def LoadFile(file):
    lines = []
    with open(file, 'r') as f:
        newlist = f.read()
        lines.append(newlist)
        print('OUTPUT ', lines)
def UpdateString(string, c , n):
    string1 = string[:n] + c + string[n:]
    print(string1)
def FindWordCount(string, string1):
    c = string1.count('string')
    print(c)
def ScoreFinder(players, scores, player):
    
    for i in range(len(players)):
        lower = players[i].lower()
        print(lower)
        if (player == players[i]) or (player == lower):
            break
    if player in players or player in lower:    
        print('OUTPUT',player, 'got a score of', scores[i])
    else:
        print('OUTPUT player not found')
