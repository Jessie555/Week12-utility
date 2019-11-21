# Jessie555/Week12-utility
# Jessie Fehrenbach
# CSCI 102 - Section C
# Week 11 - Part B

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
