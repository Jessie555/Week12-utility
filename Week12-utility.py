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
        
