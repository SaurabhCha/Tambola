import numpy as np
import random
from tabulate import tabulate

def getTicket():
    
    ticket_matrix = np.zeros((3, 9), dtype=int)
    total_indices = [(i, j) for i in range(3) for j in range(9)]
    # Rule 1: Each Row must have 5 elements
    random_indices = []
    random_indices.extend(random.sample(total_indices[:9], 5))
    random_indices.extend(random.sample(total_indices[9:18], 5))
    random_indices.extend(random.sample(total_indices[-9:], 5))
    #Rule 2: Each column must have numbers within a specified range
    #Example column 2(index=1) will have numbers between 11 to 20
    listOfRangedNumbers = [list(range(1,11)),list(range(11,21)),list(range(21,31)),list(range(31,41)),list(range(41,51)),list(range(51,61)),list(range(61,71)),list(range(71,81)),list(range(81,91))]
    for num in random_indices:
        col = num[1]
        number = random.choice(listOfRangedNumbers[col])
        ticket_matrix[num] = number
        listOfRangedNumbers[col].remove(number)
    #Rule 3: In each column, numbers must be arranged in ascending order from top to bottom
    for col in range(9):
        if(ticket_matrix[0][col] != 0 and ticket_matrix[1][col] != 0 and ticket_matrix[2][col] != 0):
            l=[ticket_matrix[0][col],ticket_matrix[1][col],ticket_matrix[2][col]]
            l.sort()
            ticket_matrix[0][col]=l[0]
            ticket_matrix[1][col]=l[1]
            ticket_matrix[2][col]=l[2]
        elif(ticket_matrix[0][col] != 0 and ticket_matrix[1][col] != 0 and ticket_matrix[2][col] == 0):
            if ticket_matrix[0][col] > ticket_matrix[1][col]:
                temp = ticket_matrix[0][col]
                ticket_matrix[0][col] = ticket_matrix[1][col]
                ticket_matrix[1][col] = temp
        elif(ticket_matrix[0][col] != 0 and ticket_matrix[1][col] == 0 and ticket_matrix[2][col] != 0):
            if ticket_matrix[0][col] > ticket_matrix[2][col]:
                temp = ticket_matrix[0][col]
                ticket_matrix[0][col] = ticket_matrix[2][col]
                ticket_matrix[2][col] = temp
        elif(ticket_matrix[0][col] == 0 and ticket_matrix[1][col] != 0 and ticket_matrix[2][col] != 0):
            if ticket_matrix[1][col] > ticket_matrix[2][col]:
                temp = ticket_matrix[1][col]
                ticket_matrix[1][col] = ticket_matrix[2][col]
                ticket_matrix[2][col] = temp
    return ticket_matrix

def main():
    numberOfTickets = 5
    for i in range(numberOfTickets):
        ticket = getTicket()
        #Removing all the zeros from the matrix
        ticket = ticket.astype('str') 
        ticket[ticket=="0"]=" "
        print(tabulate(ticket,tablefmt="grid", numalign="center"))
        print()
        print()

if __name__=="__main__":
    main()