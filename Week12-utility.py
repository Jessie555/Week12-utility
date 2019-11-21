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
        if (player == players[i]) or (player == lower):
            break
    if player in players or player in lower:    
        print('OUTPUT',player, 'got a score of', scores[i])
    else:
        print('OUTPUT player not found')
def Union(list1, list2):
    final = list1 + list2
    return final
def Intersection(list1, list2):
    inter = []
    for i in list1:
        for n in list2:
            if n==i:
                inter.append(n)
    print("OUTPUT " , inter)
def NotIn(list1, list2):
    list3 = []
    for i in list1:
        if i not in list2:
            list3.append(i)
    return list3
                
    
