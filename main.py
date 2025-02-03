from ttt import Tic_Tac_Toe

gameover = False
big_board = []

# create 9 tic-tac-toe games
for ii in range(3):
    temp = []
    for jj in range(3):
        temp.append(Tic_Tac_Toe())
    big_board.append(temp)
games = {
    "game_one" : big_board[0][0],
    "game_two" : big_board[0][1],
    "game_three" : big_board[0][2],
    "game_four" : big_board[1][0],
    "game_five" : big_board[1][1],
    "game_six" : big_board[1][2],
    "game_seven" : big_board[2][0],
    "game_eight" : big_board[2][1],
    "game_nine" : big_board[2][2],
}

def print_helper(row):
    micro_one = ""
    for ii in range(3):
        micro_one += row[ii][0:5]

    micro_two = ""
    for ii in range(3):
        micro_two += row[ii][6:11]

    micro_three = ""
    for ii in range(3):
        micro_three += row[ii][12:17]
    
    print(micro_one)
    print(micro_two)
    print(micro_three)

def print_ultimate():

    row_one = games["game_one"].print_board() + "$" + games["game_two"].print_board() + "$" + games["game_three"].print_board()
    row_two = games["game_four"].print_board() + "$" + games["game_five"].print_board() + "$" + games["game_six"].print_board()
    row_three = games["game_seven"].print_board() + "$" + games["game_eight"].print_board() + "$" + games["game_nine"].print_board()
    lb = "--- +--- +--- +"
    r1_list = row_one.split("$")
    r2_list = row_two.split("$")
    r3_list = row_three.split("$")


    print_helper(r1_list)
    print(lb)
    print_helper(r2_list)
    print(lb)
    print_helper(r3_list)

def update_ultimate(game_number,position,player):
    match game_number:
        case 1:
            games["game_one"].place_turn(position,player)
            return True
        case 2:
            games["game_two"].place_turn(position,player)
            return True
        case 3:
            games["game_three"].place_turn(position,player)
            return True
        case 4:
            games["game_four"].place_turn(position,player)
            return True
        case 5:
            games["game_five"].place_turn(position,player)
            return True
        case 6:
            games["game_six"].place_turn(position,player)
            return True
        case 7:
            games["game_seven"].place_turn(position,player)
            return True
        case 8:
            games["game_eight"].place_turn(position,player)
            return True
        case 9:
            games["game_nine"].place_turn(position,player)
            return True

def check_inner_game(game_number):
    match game_number:
        case 1:
            if games["game_one"].check4win():
                return True
        case 2:
            if games["game_two"].check4win():
                return True
        case 3:
            if games["game_three"].check4win():
                return True
        case 4:
            if games["game_four"].check4win():
                return True
        case 5:
            if games["game_five"].check4win():
                return True
        case 6:
            if games["game_six"].check4win():
                return True
        case 7:
            if games["game_seven"].check4win():
                return True
        case 8:
            if games["game_eight"].check4win():
                return True
        case 9:
            if games["game_nine"].check4win():
                return True
        case _:
            return False

def print_square():
    print("""
1 | 2 | 3
- + - + -
4 | 5 | 6
- + - + -
7 | 8 | 9
      """)

def check_win_ultimate():
        #horizontal
        foundWin = False
        for ii in range(3):
            if big_board[ii][0].get_winner() != " " and big_board[ii][0].get_winner() == big_board[ii][1].get_winner() and big_board[ii][1].get_winner() == big_board[ii][2].get_winner():
                foundWin = True
                break
        #vertical
        for ii in range(3):
            if big_board[0][ii].get_winner() != " " and big_board[0][ii].get_winner() == big_board[1][ii].get_winner() and big_board[1][ii].get_winner() == big_board[2][ii].get_winner():
                foundWin = True
                break

        #diagonal
        if big_board[1][1].get_winner() != " " and big_board[0][0].get_winner() == big_board[1][1].get_winner() and big_board[1][1].get_winner() == big_board[2][2].get_winner():
            foundWin = True
        
        #anti-diagonal
        if big_board[1][1].get_winner() != " " and big_board[0][2].get_winner() == big_board[1][1].get_winner() and big_board[1][1].get_winner() == big_board[2][0].get_winner():
            foundWin = True

        return foundWin


# ----

print_square()
p1_choice = int(input("Enter Choice :: "))
p1_position = int(input("Which position to select:: "))
#TODO: validate input
update_ultimate(p1_choice,p1_position,'X')
print_ultimate()

while not gameover:

    #check if game of p1 last turn is won: if so, allow the p2 to pick a game to enter
    if check_inner_game(p1_position):
        print_square()
        p2_choice = int(input("Enter Choice :: "))
        p2_position = int(input("Which position to select:: "))
        update_ultimate(p2_choice,p2_position,'O')
    else:
        print(f"~~Player 2 has to play game {p1_position}~~")
        p2_position = int(input(f"[Game{p1_position}] Which position:: "))
        update_ultimate(p1_position,p2_position,'O')
    
    print_ultimate()

    #check for win after p2 turn
    if check_win_ultimate():
        gameover = True
        print("P2 Won the Game!")
        break

     #check if game of p2 last turn is won: if so, allow the p1 to pick a game to enter
    if check_inner_game(p2_position):
        print_square()
        p1_choice = int(input("Enter Choice :: "))
        p1_position = int(input("Which position to select:: "))
        update_ultimate(p1_choice,p1_position,'X')
    else:
        print(f"~~ Player 1 has to play game {p2_position} ~~")
        p1_position = int(input(f"[Game{p2_position}] Which position:: "))
        update_ultimate(p2_position,p1_position,'X')

    print_ultimate()

    #check for win after p1 turn
    if check_win_ultimate():
        gameover = True
        print("P1 Won the Game!")
        break

#TODO: Validate Input
#TODO: Announce local wins and change sector


# 1 | 2 | 3
# - + - + -
# 4 | 5 | 6
# - + - + -
# 7 | 8 | 9

# 1 | 2 | 3
# - + - + -
# 4 | 5 | 6
# - + - + -
# 7 | 8 | 9

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