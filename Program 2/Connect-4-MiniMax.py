import json
import random
import sys
import numpy as np

NEGINF = -99999999
POSINF = 99999999

class Minimax:

    def __init__(self, precept):
        self.prepcept = [x[:] for x in precept]
    
    def bestMove(self, depth, state, curr_player):
        """
        This Function is used to return the best move and the alpha calls
        """

        #used to enumerate all the legal moves
        legal_Moves = {} #alpha values to map
        for col in range(7):
            #if this column would be a legal move
            if self.isLegal(col, state):
                #make the move in column
                temp = self.Make_Move(state, col, curr_player)
                legal_Moves[col] = -self.search(depth - 1, temp)

        best_move = None
        moves = legal_Moves.items()
        for move, alpha in moves:
            if alpha >= NEGINF:
                NEGINF = alpha
                best_move = move
        return best_move, alpha

    def Search(self, depth, state, curr_player):
        """
        Section is the best used to search the tree depth
        Would also return the alpha values
        """
        legal_moves = [] #used to enumerate all legal moves in this state
        for i in range(7):
            if self.isLegal(i, state):
                #if column i would be a legal move created
                temp = self.Make_Move(state, i, curr_player)
                legal_moves.append(temp)
        
        #if the nide is a terminal node
        if depth == 0 or len(legal_moves) == 0:
            #would return the heuristic value
            return self.value(state, curr_player)
        
        NEGINF = -9999999
        for child in legal_moves:
            NEGINF = max(NEGINF, -self.search(depth - 1, child))
        return NEGINF
    
    def isLegal(self, col, state):
        """
        Would be able to check if placing the move in the correct column or not
        """
        for i in range(6):
            if state[i][col] == ' ':
                #if its an empty column then it would be able to know where to place the next move
                return True
        #would return False if the column would be full
        return False

    def Make_Move(col, state):
        """
        This section would be returning a copy of the array when a move is created
        """
        for i in range(6):
            if state[i][col] == ' ':
                return True
        return False
    
    def verticalMove(self, row, col, state, block):
        """
        Would check its next moves in vertical rows
        """
        count = 0
        for i in range(row, 6):
            if state[i][col].lower() == state[row][col].lower():
                count += 1
            else:
                break
        
        if count >= block:
            return 1
        else:
            return 0

    def horizontalMove(self, row, col, state, block):
        """
        Would check its next move in horizontal rows
        """
        count = 0
        for j in range(col, 7):
            if state[row][j].lower() == state[row][col].lower():
                count += 1
            else:
                break
        
        if count >= block:
            return 1
        else:
            return 0
    def diagonalCheck(self, row, col, state, block):
        """
        Would check diagonally to see its next possible move
        """
        total = 0
        count = 0
        j = col
        for i in range(row, 6):
            if j > 6:
                break
            elif state[i][j].lower() == state[row][col].lower():
                count += 1
            else:
                break
            j += 1

        if count >= block:
            total += 1
        
        count = 0
        j = col
        for i in range(row, -1, -1):
            if j > 6:
                break
            elif state[i][j].lower() == state[row][col].lower():
                count += 1
            else:
                break
            j += 1
        
        if count >= block:
            total += 1
        
        return total

    def checkRows(self, state, piece, block):
        grid = precept['grid']
        moves = []
        #checks the pieces in the board
        for i in enumerate(grid):
            for j in enumerate(grid):
                if state[i][j].lower() == piece.lower():
                    #would check the opponenents pieces on the board
                    moves += self.verticalMove(i, j, state, block)
                    #would check the vertical moves it possibly has vertically
                    moves += self.horizontalMove(i, j, state, block)
                    #would check the horizontal moves it possibly has horizontally
                    moves += self.diagonalCheck(i, j, state, block)
                    #would check its next moves diagonally
                    moves.append(i)
                    moves.append(j)
        return moves



difficulty = 6
m = Minimax()
print('Connect Four in Python', file=sys.stderr)
for line in sys.stdin:
    print(line, file=sys.stderr)
    precept = json.loads(line)
    moves = m.bestMove(difficulty , precept)
    print(moves, file=sys.stderr)
    move = m.choice(moves)
    action = {'move': move}
    action_json = json.dumps(action)
    print(action_json, file=sys.stderr)
    print(action_json, flush=True)
        
