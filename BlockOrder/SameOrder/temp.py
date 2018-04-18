#This code takes a large list and makes a new .txt file with the first x digits.
#Used as a controlled variable during testing phase
import io
def con(number):
    new_file = "listof"+str(number)+".txt"
    new = open(new_file,"w") 
    with open("listof10000000.txt") as f: #the file to be opened should have the most data
        for line in f:
            for i in range(number):
                new.write(line[i])
