#In the early development of the AI, the order that the blocks fall will remain the same as a controlled variable
# 0 = blockI
# 1 = blockO
# 2 = blockT
# 3 = blockJ
# 4 = blockL
# 5 = blockS
# 6 = blockZ

import io
import random

def blockSpawn(number):
    name = "listof"+(str(number)+".txt") #Names .txt file based on the number of numbers
    f = open(name,"w")
    for i in range(number):
        f.write(str(random.randint(0,6)))

def main():
    blockSpawn(10000000)
