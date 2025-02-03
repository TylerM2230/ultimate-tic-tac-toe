class Tic_Tac_Toe():
    def __init__(self):
        #Initialize board
        self.gameover = False
        self.winner = " "
        self.board=[]
        numeral_val = 1
        for ii in range(3):
            temp = []
            for jj in range(3):
                temp.append(numeral_val)
                numeral_val+=1
            self.board.append(temp)
        
    def print_board(self):
        output = ""
        for ii in range(3):
            for jj in range(3):
                output += str(self.board[ii][jj])
            output += " | "
        return output

    def place_turn(self,position,player):
        positions = {
            1 : [0,0],
            2 : [0,1],
            3 : [0,2],
            4 : [1,0],
            5 : [1,1],
            6 : [1,2],
            7 : [2,0],
            8 : [2,1],
            9 : [2,2],
        }

        match position:
            case 1:
                self.board[positions[1][0]][positions[1][1]] = player
                return True
            case 2:
                self.board[positions[2][0]][positions[2][1]] = player
                return True
            case 3:
                self.board[positions[3][0]][positions[3][1]] = player
                return True
            case 4:
                self.board[positions[4][0]][positions[4][1]] = player
                return True
            case 5:
                self.board[positions[5][0]][positions[5][1]] = player
                return True
            case 6:
                self.board[positions[6][0]][positions[6][1]] = player
                return True
            case 7:
                self.board[positions[7][0]][positions[7][1]] = player
                return True
            case 8:
                self.board[positions[8][0]][positions[8][1]] = player
                return True
            case 9:
                self.board[positions[9][0]][positions[9][1]] = player
                return True

    def check4win(self):

        #horizontal
        foundWin = False
        for ii in range(3):
            if self.board[ii][0] == self.board[ii][1] and self.board[ii][1] == self.board[ii][2]:
                foundWin = True
                break
        #vertical
        for ii in range(3):
            if self.board[0][ii] == self.board[1][ii] and self.board[1][ii] == self.board[2][ii]:
                foundWin = True
                break

        #diagonal
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            foundWin = True
        
        #anti-diagonal
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            foundWin = True

        return foundWin

    def won_game(self,player):
        for ii in range(3):
            for jj in range(3):
                self.board[ii][jj] = player
        self.gameover = True
        self.winner = player
    
    def get_gamestate(self):
        return self.gameover
    
    def get_winner(self):
        return self.winner





# """
# 1 | 2 | 3
# - + - + -
# 4 | 5 | 6
# - + - + -
# 7 | 8 | 9

# """


# """
# initial player determines which game to enter
# 1 | 2 | 3
# - + - + -
# 4 | 5 | 6
# - + - + -
# 7 | 8 | 9
# next player has to play the game of where first player placed
#     if next game is already won, then player gets a choice


# 123 | 123 | 123 |
# 456 | 456 | 456 |
# 789 | 123 | 123 |
# --- + --- + --- +
# 123 | 123 | 123 |
# 456 | 456 | 456 | 
# 789 | 789 | 789 |
# --- + --- + --- +
# 123 | 123 | 123 |
# 456 | 456 | 456 |
# 789 | 789 | 789 |
