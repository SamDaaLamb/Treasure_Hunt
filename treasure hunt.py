
import random


pos = []
class Piece():
    global pos
    global pieces



    def __init__(self):
        self.x = random.randint(0,9)
        self.y = random.randint(0,9)
        self.visible = True
        if Piece.isVacant(self) is False and type(self) is Treasure:
            self.__init__(gold = random.choice(amounts))

        elif Piece.isVacant(self) is False:
            self.__init__()

        # print('yay',pos)
        pos.append(((self.x, self.y),type(self)))


    # def __eq__(self, other):
    #     if not isinstance(other, Piece):
    #         # don't attempt to compare against unrelated types
    #         return NotImplemented
    #
    #     return self is other
    def isVacant(self):
        for i in pos:
            # print(self.x)
            # print(self.y)
            # print(i, 'list')
            if (self.x,self.y) in i:
                # print('ran')
                if type(self) is Scallywag:
                    # print('ended')
                    self.__init__(loot=0)

                    break

                return False


        return True

    def setX(self, new_x):
        pr_x = self.getX()
        self.x = new_x

        if self.x > 9:
            self.x-=1
            return
        elif self.x <0:
            self.x+=1
            return

        if not self.isVacant():
            self.x= pr_x



    def setY(self, new_y):
        pr_y = self.getY()
        self.y = new_y
        if self.y > 9:
            self.y-=1
            return
        elif self.y <0:
            self.y+=1
            return
        if not self.isVacant():
            self.y= pr_y

    def getX(self):
        return(self.x)

    def getY(self):
        return(self.y)

    def getVisible(self):
        return self.visible

    def getSymbol(self):
        # print(self.getVisible())
        if self.getVisible() is True:

            return self.sym
        else:
            return '_'

class Treasure(Piece):


    def __init__(self, gold):
        super().__init__()
        self.gold = gold
        self.sym = 'T'
    def getGold(self):
        return self.gold
    def SetGold(self,gold):
        self.gold = gold
    def isVacant(self):

        for i in pos:
            if (self.x,self.y) in i:
                # print('ran in tres')

                self.__init__(gold=random.choice(amounts))




    def setSymbol(self):
        self.sym = 't'
#
class Pirates(Piece):
    def __init__(self): # what if you dont even add an initalize function
        super().__init__()
        self.sym = "P"

    def setDiagonal(self, new_x, new_y,dir):
        pr_x = self.getX()
        pr_y = self.getY()
        if dir == 'up_r'and (self.getX() == 9 or self.getY() == 0):
            return
        elif dir == 'up_l'and (self.getX() == 0 or self.getY() == 0):
            return
        elif dir == 'down_r'and (self.getX() == 9 or self.getY() == 9):
            return
        elif dir == 'down_l'and (self.getX() == 0 or self.getY() == 9):
            return
        # print('test1')
        self.x = new_x
        self.y = new_y

        if not self.isVacant():
            # print('test2')
            # print(pr_x)
            # print(pr_y)
            self.x = pr_x
            self.y = pr_y
            # print(self.x)
            # print(self.y)
    def move(self):
        picks = ['up','up_r','right','down_r','down','down_l','left','up_left']
        direction = random.choice(picks)
        if direction == picks[0]: #up
            self.setY(self.getY() -1)
        elif direction == picks[1]: #up right
            self.setDiagonal(self.getX()+1,self.getY() - 1, direction)
        elif direction == picks[2]:# right
            self.setX(self.getX() +1)
        elif direction == picks[3]: # down right
            self.setDiagonal(self.getX()+1,self.getY() + 1, direction)
        elif direction == picks[4]: # down
            self.setY(self.getY() + 1)
        elif direction == picks[5]: # down left
            self.setDiagonal(self.getX()-1,self.getY() + 1, direction)
        elif direction == picks[6]:  # left
            self.setX(self.getX() - 1)
        elif direction == picks[7]: # up left
            self.setDiagonal(self.getX()-1,self.getY() - 1, direction)
    # def getSymbol(self):
    #     return ('P')

class Ambush(Piece):
    def __init__(self):
        super().__init__()
        self.visible = False
        self.sym = "A"
    # def getSymbol(self):
    #     return ('A')


class Escape(Piece):
    def __init__(self):
        super().__init__()
        self.visible = False
        self.sym = "X"
    def setVisible(self):
        self.visible = True






class Scallywag(Piece):

    def __init__(self, loot):
        super().__init__()
        self.loot = loot
    def setX(self, new_x):
        global GameisOn
        self.x = new_x
        if self.x > 9:
            self.x-=1
            return
        elif self.x <0:
            self.x+=1
            return
        # print('about')
        if self.isVacant():
           pass

        else:
            under = None
            position = (self.getX(), self.getY())
            for i in pos:
                if position in i:
                    under = i[1]

                    for j in pieces:
                        # print(j)
                        if (j.getX(),j.getY()) == position:
                            if under is Treasure:
                                self.setLoot(self.getLoot() + j.getGold())
                                j.SetGold(0)
                                j.setSymbol()
                            elif under is Pirates: #add more feedback when u hit pirate
                                self.setLoot(self.getLoot()/2)
                            elif under is Ambush:
                                self.setLoot(0)
                                GameisOn = False
                                print("Game Over: You ran into an ambush. Your total loot is", S.getLoot(),':(')
                            elif under is Escape:

                                user = input("        CONGRATS, You found an ESCAPE        \n"
                                             "        Would you like to: 1.) escape the game"
                                             "\n                      or                   \n"
                                             "          2.) continue to play to try an acquire some more loot.\n"
                                                                    "Choice 1 or Choice 2(1/2):")
                                if user == '1':
                                    GameisOn = False
                                    print("ESCAPED: You escaped the game board. Your total loot is", S.getLoot(),'\nGreat Job')
                                elif user == '2':
                                    j.setVisible()
                                    print('Ok, game will continue')
                                else:
                                    print("Wrong input enter either 1 or 2")


    def setY(self, new_y):
        global GameisOn
        self.y = new_y
        if self.y > 9:
            self.y-=1
            return
        elif self.y <0:
            self.y+=1
            return
        # print('about')
        if self.isVacant():
            pass

        else:
            under = None
            position = (self.getX(), self.getY())
            for i in pos:
                if position in i:
                    under = i[1]

                    for j in pieces:
                        # print(j)
                        if (j.getX(),j.getY()) == position:
                            if under is Treasure:
                                # print('treas')
                                self.setLoot(self.getLoot() + j.getGold())
                                j.SetGold(0)
                                j.setSymbol()
                            if under is Pirates:
                                # print('pirate')
                                self.setLoot(self.getLoot()/2)
                            elif under is Ambush:
                                self.setLoot(0)
                                GameisOn = False
                                print("Game Over: You ran into an ambush. Your total loot is", S.getLoot(),':(')
                            elif under is Escape:

                                user = input("        CONGRATS, You found an ESCAPE        \n"
                                             "        Would you like to: 1.) escape the game"
                                             "\n                      or                   \n"
                                             "          2.) continue to play to try an acquire some more loot.\n"
                                                                    "Choice 1 or Choice 2(1/2):")
                                if user == '1':
                                    GameisOn = False
                                    print("ESCAPED: You escaped the game board. Your total loot is", S.getLoot(),'\nGreat Job')
                                elif user == '2':
                                    j.setVisible()
                                    print('Ok, game will continue')
                                else:
                                    print("Wrong input enter either 1 or 2")

    def isVacant(self):
        for i in pos:

            if (self.x,self.y) in i:
                # print('ran in scallywag')
                # print(i[1])
                if i[1] is Treasure:
                    return (False)
                elif i[1] is Pirates:
                    return (False)
                elif i[1] is Ambush:
                    return (False)
                elif i[1] is Escape:
                    return(False)
                self.__init__(self.loot) # why cant it ibe init


        return (True)


    def setLoot(self, loot):
        self.loot = loot
    def getLoot(self):
        return(self.loot)
    def getSymbol(self):
        return('S')


S = Scallywag(0)


def WriteonBoard(x,y,symbol, game):
    # print(symbol)
    game[y][x] = symbol
    return game


menu = input("1.	Play game\n"
             "2.	How to play\n"
             "3.	Legend\n"
             "4.	Exit\n")
if menu == '1':
    pass
elif menu == '2':
    print('For this game, the user (a scallywag) will be going on a treasure hunt. They will explore a 10 x 10 board that\n'
          'will contain treasure, pirates and an ambush! The goal is to escape the island with the most treasure possible.\n'
          'If you would like to click read this again type: 2, at any point in the game')
elif menu == '3':
    print('T - full treasure\n'
          't - empty treasure\n'
          'P - pirate, YIKES!\n'
          'X - escape the island\n'
          'S - the scallywag … YOU!\n'
          'If you would like to click read this again type: 3, at any point in the game')
elif menu == '4':
    exit()


#Setting up Board
amounts = [100, 250, 500, 1000]
pieces = []
for i in range(10):
    pieces.append(Treasure(random.choice(amounts)))
for i in range(4):
    pieces.append(Pirates())
pieces.append(Ambush())
pieces.append(Escape())


GameisOn = True

while GameisOn:
    count = 0
    game_board = [['_','_','_','_','_','_','_','_','_','_'],
              ['_','_','_','_','_','_','_','_','_','_'],
              ['_','_','_','_','_','_','_','_','_','_'],
              ['_','_','_','_','_','_','_','_','_','_'],
              ['_','_','_','_','_','_','_','_','_','_'],
              ['_','_','_','_','_','_','_','_','_','_'],
              ['_','_','_','_','_','_','_','_','_','_'],
              ['_','_','_','_','_','_','_','_','_','_'],
              ['_','_','_','_','_','_','_','_','_','_'],
              ['_','_','_','_','_','_','_','_','_','_'],
              ]

    for i in pieces:

        game_board = WriteonBoard(i.getX(), i.getY(), i.getSymbol(), game_board)

    game_board = WriteonBoard(S.getX(), S.getY(), S.getSymbol(), game_board)
    for i in game_board:
        print(*i)

        # for j in i:
        #     if j != '_':
        #         count +=1
    # print(count)


    print('Gold:', S.getLoot())
    # print(pos)
    ans = True
    while ans:
        ans = False
        dir = input("What direction would you like to move (w,a,s,d):")
        if dir == 'w':
            S.setY(S.getY() + -1)
        elif dir == 'a':
            S.setX(S.getX() + -1)
        elif dir == 's':
            S.setY(S.getY() + 1)
        elif dir == 'd':
            S.setX(S.getX() + 1)
        elif dir == '2':
            print(
                'For this game, the user (a scallywag) will be going on a treasure hunt. They will explore a 10 x 10 board that\n'
                'will contain treasure, pirates and an ambush! The goal is to escape the island with the most treasure possible.\n')
            ans = True
        elif dir == '3':
            print('T - full treasure\n'
              't - empty treasure\n'
              'P - pirate, YIKES!\n'
              'X - escape the island\n'
              'S - the scallywag … YOU!\n')
            ans = True
        else:
            print("wrong input go again")
            ans = True

    for i in pieces:
        if type(i) == Pirates:
            i.move()

    pos = []
    pos.append(((S.getX(), S.getY()), type(S)))  # what the point of get
    for i in pieces:

        # what the point of get
        pos.append(((i.x, i.y),type(i)))
