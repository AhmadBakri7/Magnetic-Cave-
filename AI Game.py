#Ayman Salama 1200488
#Ahmad Bakri 1201509

# Features of every node of the tree
class Tree_Ball:
    def __init__(self, BRD, clr):
        self.board = BRD # board of the game
        self.color = clr # there are two options white or black
        self.children = [] # array of children contain every possible childs
        self.heuristic = 0
        self.parent = None # This return the parent of the current child

    # This function to add nodes to the tree
    def Ball_Add(self, child):
        self.children.append(child) # Add the childreen to the tree by using the append function
        child.parent = self

    # This function create a tree and generate the nodes
    def Make_Tree(self, Depth):
        if Depth == 0: # return  nothing because there is no tree generated
            return

        # now checks if the value of self.color is equal to 'white' or not
        if self.color == 'white':
            clr_new = 'black'
            Brick_clr = '■'
        else:
            clr_new = 'white'
            Brick_clr = '□'
        # Nested loop to reach for every node of the tree (board)
        for Hor in range(8):
            for Ver in range(8):
                # check if there is an empty place or not
                if self.board[Hor][Ver] == '-':
                    # check the columns 0 and 7 to start wirh these columns
                    if Ver == 0 or Ver == 7: 
                        BRD_new = [i[:] for i in self.board]  # make a copy of the board
                        BRD_new[Hor][Ver] = Brick_clr # add a brick to the board
                        child = Tree_Ball(BRD_new, clr_new)
                        self.Ball_Add(child)
                        child.Make_Tree(Depth - 1)  # reach for avary node of the tree by using recursion
                        # check if the place is not empty
                    elif self.board[Hor][Ver - 1] != '-' or self.board[Hor][Ver + 1] != '-':
                        BRD_new = [j[:] for j in self.board]   # make a copy of the board
                        BRD_new[Hor][Ver] = Brick_clr
                        child = Tree_Ball(BRD_new, clr_new)
                        self.Ball_Add(child)
                        child.Make_Tree(Depth - 1)
                        
    # This display the view of board
    def display_board(self):
        #arrangment of the board
        print("   A B C D E F G H")
        for row in range(8):
            print(f"{row} |{' '.join(self.board[row])}| {row}")
        print("   A B C D E F G H")

    def evaluate(self, clr):
       
        Point = 0 #initialize the point
        # Check for horizontal lines
        for Hor in range(8):
            for Ver in range(5):
                WND = self.board[Hor][Ver:Ver + 4]
                if clr == 'white':
                    Point += self.Determine_point_white(WND)
                elif clr == 'black':
                    Point += self.Determine_point_black(WND)
        # Check for vertical lines
        for Ver in range(8):
            for Hor in range(5):
                WND = [self.board[Hor + i][Ver] for i in range(4)]
                if clr == 'white':
                    Point += self.Determine_point_white(WND)
                elif clr == 'black':
                    Point += self.Determine_point_black(WND)
        # Check the cases of diagonal 
        for Hor in range(5):
            for Ver in range(5):
                WND = [self.board[Hor + i][Ver + i] for i in range(4)]
                if clr == 'white':
                    Point += self.Determine_point_white(WND)
                elif clr == 'black':
                    Point += self.Determine_point_black(WND)
        # Check the cases diagonal also
        for Hor in range(5):
            for Ver in range(3, 8):
                WND = [self.board[Hor + i][Ver - i] for i in range(4)]
                if clr == 'white':
                    Point += self.Determine_point_white(WND)
                elif clr == 'black':
                    Point += self.Determine_point_black(WND)

        self.heuristic = Point # return the score to build the tree in rigth way

        
    #The method calculates the points based on the number of symbols present in the window and assigns different scores for different configurations.
    def Determine_point_white(self, WND):

        Counter_Ai = WND.count('■') #This line counts the occurrences of the symbol '■'
        Counter_opponent = WND.count('□') #This line counts the occurrences of the symbol '□'

        if Counter_Ai == 4:
            return 1000000 
        elif Counter_Ai == 3 and Counter_opponent == 0:
            return 100  
        elif Counter_Ai == 2 and Counter_opponent == 0:
            return 10  
        elif Counter_opponent == 3 and Counter_Ai == 0:
            return -100  
        elif Counter_opponent == 2 and Counter_Ai == 0:
            return -10  
        else:
            return 0  
    #This function same as above function but for black bricks
    def Determine_point_black(self, window):
        Counter_opponent = window.count('■')
        Counter_Ai = window.count('□')

        if Counter_Ai == 4:
            return 1000000 
        elif Counter_Ai == 3 and Counter_opponent == 0:
            return 100 
        elif Counter_Ai == 2 and Counter_opponent == 0:
            return 10  
        elif Counter_opponent == 3 and Counter_Ai == 0:
            return -100  
        elif Counter_opponent == 2 and Counter_Ai == 0:
            return -10  
        else:
            return 0  


    #MinMax algorithem that returns the min value as shown in function
    def minimax(self, Depth, Player_Max):
        
        if Depth == 0 or len(self.children) == 0:
            return self.heuristic

        if Player_Max:
            Level_Max = float('-inf')
            for child in self.children:
                eval = child.minimax(Depth - 1, False)
                Level_Max = max(Level_Max, eval)
            return Level_Max
        else:
            Level_Min = float('inf')
            for child in self.children:
                eval = child.minimax(Depth - 1, True)
                Level_Min = min(Level_Min, eval)
            return Level_Min

def display_board(board):
    print("   A B C D E F G H")
    for row in range(8):
        print(f"{row} |{' '.join(board[row])}| {row}")
    print("   A B C D E F G H")


def Turn_For_Black(BRD):
    #Define array of all Bricks
    Array_Bricks = [] 

    # Determine which place you want for black brick
    Hor = int(input("Enter the row for black: "))
    Ver = int(input("Enter the column for black: "))

    if Ver == 0 or Ver == 7:
        if BRD[Hor][Ver] == '-':
            Array_Bricks.append((Hor, Ver))
            BRD[Hor][Ver] = '□'
            display_board(BRD)
        else:
            print("Try again, you can't put brick here")
            Turn_For_Black(BRD)
    else:
        if BRD[Hor][Ver - 1] != '-' or BRD[Hor][Ver + 1] != '-':
            if BRD[Hor][Ver] == '-':
                Array_Bricks.append((Hor, Ver))
                BRD[Hor][Ver] = '□' 
                display_board(BRD)
            else:
                print("Try again, you can't put brick here")
                Turn_For_Black(BRD)
        else:
            print("Try again, you can't put brick here")
            Turn_For_Black(BRD)

def Turn_For_White(BRD):

    #Define array of all Bricks
    Array_Bricks = [] 

    # Determine which place you want for white brick
    Hor = int(input("Enter the row for white: "))
    Ver = int(input("Enter the column for white: "))

    if Ver == 0 or Ver == 7:
        if BRD[Hor][Ver] == '-':
            Array_Bricks.append((Hor, Ver))
            BRD[Hor][Ver] = '■'  
            display_board(BRD)
        else:
            print("Try again, you can't put brick here")
            Turn_For_White(BRD)
    else:
        if BRD[Hor][Ver - 1] != '-' or BRD[Hor][Ver + 1] != '-':
            if BRD[Hor][Ver] == '-':
                Array_Bricks.append((Hor, Ver))
                BRD[Hor][Ver] = '■' 
                display_board(BRD)
            else:
                print("Try again, you can't put brick here")
                Turn_For_White(BRD)
        else:
            print("Try again, you can't put brick here")
            Turn_For_White(BRD)

def check_winner(board):

    for row in range(8):
        for col in range(8):
            brick = board[row][col]
            if brick != '-':
                # Check horizontal 
                if col <=3:
                    if all(board[row][col+i] == brick for i in range(5)):
                        return True
                else:
                    if all(board[row][col-i] == brick for i in range(5)):
                        return True

                # Check vertical 
                if row <= 3:
                    if all(board[row+i][col] == brick for i in range(5)):
                        return True
                else:
                    if all(board[row-i][col] == brick for i in range(5)):
                        return True

                # Check diagonal win (top-left to bottom-right)
                if row <= 3 and col <= 3:
                    if all(board[row+i][col+i] == brick for i in range(5)):
                        return True
                elif row <= 3 and col >3:
                    # Check diagonal win (top-right to bottom-left)
                    if all(board[row+i][col-i] == brick for i in range(5)):
                        return True
                elif row > 3 and col <= 3:
                # Check diagonal win (bottom-left to top-right)
                    if all(board[row-i][col+i] == brick for i in range(5)):
                        return True
                elif row > 3 and col > 3:
                    # Check diagonal win (bottom-right to top-left)
                    if all(board[row-i][col-i] == brick for i in range(5)):
                        return True
    return False

#The first choise if you want two player option
def Game_Manual(BRD):

    #Display the board
    display_board(BRD)

    while True:
        Turn_For_White(BRD)
        if (check_winner(BRD) == True):
            print("Congrat's, White Win's")
            exit(1)

        Turn_For_Black(BRD)
        if (check_winner(BRD) == True):
            print("Congrat's, black Win's")
            exit(1)

def Ai_White(BRD):
    
    #Generate the root of the tree
    Root = Tree_Ball(BRD, 'white')

    #Generate the tree and put the depth
    Root.Make_Tree(3)

    for child in Root.children:
        for child1 in child.children:
            for child2 in child1.children:
                child2.evaluate('white')

    The_Best_Move = None
    Max_Evaluation = float('-inf')

    for child in Root.children:
        for child1 in child.children:
            for child2 in child1.children:
                Evaluation = child2.minimax(2, False)
                if Evaluation > Max_Evaluation:
                    Max_Evaluation = Evaluation
                    The_Best_Move = child2

    holdHere = The_Best_Move
    while(holdHere.parent != Root and holdHere.parent != None):
        holdHere = holdHere.parent

    holdHere.display_board()
    return holdHere.board

def Ai_Black(BRD):

    #Generate the root of the tree
    Root = Tree_Ball(BRD, 'black')

    #Generate the tree and put the depth
    Root.Make_Tree(3)

    for child in Root.children:
        for child1 in child.children:
            for child2 in child1.children:
                child2.evaluate('black')

    
    The_Best_Move = None
    Max_Evaluation = float('-inf')

    for child in Root.children:
        for child1 in child.children:
            for child2 in child1.children:
                eval = child2.minimax(2, False)
                if eval > Max_Evaluation:
                    Max_Evaluation = eval
                    The_Best_Move = child2

    holdHere = The_Best_Move
    while(holdHere.parent != Root and holdHere.parent != None):
        holdHere = holdHere.parent

    holdHere.display_board()
    return holdHere.board

def White_Manual(BRD):
    #Display board
    display_board(BRD)

    #This while check which one is win
    while True:
        BRD = Ai_White(BRD) # white ai tern
        if (check_winner(BRD) == True):
            print("Congrat's, white Win's")
            exit(1)
        Turn_For_Black(BRD) # tern of black player
        if (check_winner(BRD) == True):
            print("Congrat's, black Win's")
            exit(1)

def Black_Manual(BRD):
    #Display board
    display_board(BRD)

    #This while check which one is win
    while True:
        Turn_For_White(BRD) # tern of white player
        if (check_winner(BRD) == True):
            print("Congrat's, white Win's")
            exit(1)
        BRD = Ai_Black(BRD) # black ai tern
        if (check_winner(BRD) == True):
            print("Congrat's, black Win's")
            exit(1)

def main(board):
    print("welcome to magnetic cave game\n"
          "prepared by:\n"
          "Ayman Salama 1200488\n"
          "Ahmad Bakri 1201509\n")
    choice = input("please choose one of the following options:\n"
                   "1. manual entry for both ■’s moves and □’s moves\n"
                   "2. manual entry for ■’s moves & automatic moves for □\n"
                   "3. manual entry for □’s moves & automatic moves for ■\n")

    if int(choice) == 1:
        Game_Manual(board)
    elif int(choice) == 2:
        White_Manual(board)
    elif int(choice) == 3:
        Black_Manual(board)

board = [['-' for _ in range(8)] for _ in range(8)] # create a board 8*8
main(board) # start the code from here