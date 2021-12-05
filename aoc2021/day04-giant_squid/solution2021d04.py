"""Day 4: Giant Squid""" 
 
import sys, os, inspect

def bingo_load(filepath):
    bingostream = []    # list of numbers drawed for the bingo
    boards = [ [] ]   # list of 2-dimentional playing boards

    with open (filepath, "r") as inputfile:
        iboard = 0 # current board
        for i, line in enumerate(inputfile):
            line = line.rstrip()
            if(i==0):
                bingostream = list(map(int,line.split(',')))
            # we already passed the first separator where boards are defined
            elif (1<i):
                # blank line means board separator, so we start filling the next board
                if len(line)==0 or line.isspace():
                    boards.append([])
                    iboard +=1
                else: # row is added to the current board
                    boards[iboard].append( list( map(int,line.split()) ) )
    
    return bingostream, boards

def bingo_runner(bingostream, boards, find_last_winner=False):
    num_boards = len(boards)
    nrows_board = len(boards[0])
    ncolumns_board = len(boards[0][0])
    res = 0 # final score

    # registry so if find_last_winner=True, register winner boards and skip them to save time
    board_win_registry = [False]*num_boards
    board_winner_n = -1

    # variable for storing already 'called' numbers
    # boards_state[num_boards][nrows_board][ncolumns_board]
    boards_state = [[[False]*ncolumns_board for i in range(nrows_board) ] for j in range(num_boards)]

    # BEWARE OF THE TRAP! THIS WON'T WORK: boards_state = [ [[False]*ncolumns_board]*nrows_board ]*num_boards
    # explanation: Lists are objects. The same list instance of [[False]*ncolumns_board] is referenced for all rows and boards!
    # this is why altering an element alters also all rows in all boards
    # source: https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python#answer-44382900

    # sequencially draw numbers
    for n in bingostream:
        for iboard, board in enumerate(boards):
            if find_last_winner and board_win_registry[iboard]:
                continue
            for irow, row in enumerate(board):
                for icolumn, elem in enumerate(row):
                    if elem==n:
                        boards_state[iboard][irow][icolumn] = True
            
            # after marking the board for all ocurrences of the drawed number n, check if it is a winner board
            if winner_checker(boards_state[iboard]):
                
                # calculate the final score if it was a winning board
                b_score = board_score(board, boards_state[iboard])
                res = n * b_score
                board_winner_n = iboard
                if not find_last_winner:
                    print(f"First winner found for number drawed {n}: board{board_winner_n+1} with score {b_score}")
                    break
                # if find_last_winner is not passed, we keep looking for the rest of the winners
                else:
                    board_win_registry[iboard] = True # winner board is registered

        # if find_last_winner is false we stop searching
        if 0<res and not find_last_winner:
            break
        # if find_last_winner is true we stop when the last board has won
        elif all(board_won for board_won in board_win_registry):
            print(f"Last winner found for number drawed {n}: board{board_winner_n+1} with score {b_score}")
            break

    return res

def board_score(board, board_state):
    score = 0
    for irow, row in enumerate(board_state):
        for icolumn, elem in enumerate(row):
            if elem == False:
                score += board[irow][icolumn]
    return score

def winner_checker(board_state):
    column_checker = [True]*len(board_state[0])
    res = False
    for irow in board_state:
        row_cheker = True
        for ielem, elem in enumerate(irow):
            row_cheker = row_cheker and elem
            column_checker[ielem] = column_checker[ielem] and elem
        if row_cheker==True:
            res = True
            break # A complete row was found
        
    for icolumn, column in enumerate(column_checker):
        if column == True:
            res = True
            break # A complete column was found
    return res

def print_bingo(bingostream, boards):
    print(f"bingostream: {bingostream}")
    print("boards:")
    for board in boards:
        for row in board:
            print(*row, sep='\t')
        print() # board separator
    print() # print_bingo separator

def main():
    # run script with arguments: load the input file

    bingostream = []    # list of numbers drawed for the bingo
    boards = [ [[]] ]   # list of 2-dimentional playing boards

    if(2 <= len(sys.argv)):
        inputfile = sys.argv[1]
        bingostream, boards  = bingo_load(inputfile)
    # run script with no arguments: load example data
    else:
        print("No argument provided. Attempting to load 'example.txt' file\n")
        current_script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        example_inputfile = os.path.join(current_script_dir,"example.txt")

        bingostream, boards  = bingo_load(example_inputfile)
        print(f"Puzzle input (example)\n")
        print_bingo(bingostream, boards)

    print(f"Answer (part 1): {bingo_runner(bingostream, boards)}\n") # Correct example answer: 4512
    print(f"Answer (part 2): {bingo_runner(bingostream, boards, True)}") # Correct example answer: 1924
    pass
 
if __name__ == "__main__": 
	main()