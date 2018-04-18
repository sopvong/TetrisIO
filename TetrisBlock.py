import pygame

class TetrisBlock(object):

    KeyStroke = None    #Starts with None, therefore falls down at a constant rate

    BlockType =         #Determines whether it is a
                        # 0 = blockI
                        # 1 = blockO
                        # 2 = blockT
                        # 3 = blockJ
                        # 4 = blockL
                        # 5 = blockS
                        # 6 = blockZ

    def __init__(self):


    def move(self,KeyStroke): #Move includes: rotating (KeyUp), increase drop speed (KeyDown) AND left (KeyLeft) and right (KeyRight)
        if (KeyStroke == KeyUp):
            #rotating code goes here
        if (KeyStroke == KeyDown):
            #Increasing drop speed goes here
        if (KeyStroke == KeyLeft):
            #Block moving to the left code goes here
        if (KeyStroke == KeyRight):
            #Block moving to the right code goes here