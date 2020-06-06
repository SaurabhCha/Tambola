import random
import numpy as np
from tabulate import tabulate
    
def generateRandomNumber():
    allNumbers = list(range(1,91))
    selectedNumbers = np.zeros((9,10), dtype=int)
    while True:
        x = input()
        if(x==""):
            if(len(allNumbers)==0):
                print("Done with all the numbers")
                break
            selectedNumber = random.choice(allNumbers)
            allNumbers.remove(selectedNumber)
            print()
            print(f'Please cross {selectedNumber}')
            print()
            c=str(selectedNumber)
            if(len(c)==1):
                c="0"+c
                c=list(map(int,list(c)))
                if(c[1]==0):
                    selectedNumbers[c[0]][9]=selectedNumber
                else:
                    selectedNumbers[c[0]][c[1]-1]=selectedNumber
            else:
                c=list(map(int,list(c)))
                if(c[1]==0):
                    selectedNumbers[c[0]-1][9]=selectedNumber
                else:
                    selectedNumbers[c[0]][c[1]-1]=selectedNumber
            selectedNumbers = selectedNumbers.astype('str') 
            selectedNumbers[selectedNumbers=="0"]=" "
            print(tabulate(selectedNumbers,tablefmt="grid", numalign="center"))
        elif(x=="end"):
            break

    
def main():
    print("Hello All, Welcome to Tambola")
    print()
    print("These are the winning Combinations:")
    print("  *  Top line")
    print("  *  Middle line")
    print("  *  Bottom line")
    print("  *  Full house")
    generateRandomNumber()

if __name__=="__main__":
    main()
