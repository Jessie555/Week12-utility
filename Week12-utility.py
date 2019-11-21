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
    c = string1.find(string,(len(string)-1))
    print(c)
