init:

    image bg Battle field = "Pattern-Camouflage-militari.jpg"
    image princess happy = "princess.png"

    python:
        SCREEN_WIDTH  = 800
        SCREEN_HEIGHT = 600

        MAP = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,0,1,0,1,0,0,0,1,1,1,1,1],
               [1,1,0,1,0,1,0,1,0,1,1,1,1,1],
               [1,1,0,1,0,1,0,0,0,1,1,1,1,1],
               [1,1,0,1,0,1,0,1,1,1,1,1,1,1],
               [1,1,0,0,0,1,0,1,1,0,1,2,3,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
               [1,3,3,3,1,0,0,0,1,2,2,2,1,1],
               [1,1,3,1,1,0,1,0,1,2,1,1,1,1],
               [1,1,3,1,1,0,0,0,1,2,2,2,1,1],
               [1,1,3,1,1,0,1,0,1,1,1,2,1,1],
               [1,3,3,1,1,0,1,0,1,2,2,2,1,1],
               [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
               
        UNITMAP = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,1,0,0,0,0,0,0,0],
                   [0,0,0,0,0,1,1,1,0,0,0,0,0,0],
                   [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                   [0,0,0,0,0,1,1,1,0,0,0,0,0,0],
                   [0,0,0,0,0,0,1,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

        MAP_WIDTH  = 14
        MAP_HEIGHT = 14
        TILE_WIDTH = 64
        TILE_HEIGHT = 32
        
        #Tile Defines
        TILE_GRASS = 1
        TILE_FOREST = 0
        TILE_DIRT = 2
        TILE_WATER = 3
        
#-------------------------------------------------------------------

        class Star(object):
            #"""This class is the astar algorithm itself.  The goal is to make it
            #flexible enough that it can be used in isolation."""
            def __init__(self,start,end,move_type,barriers):
                """Arguments start and end are coordinates to start solving from and to.
                move_type is a string cooresponding to the keys of the ADJACENTS and
                HEURISTICS constant dictionaries. barriers is a set of cells which the
                agent is not allowed to occupy."""
                self.start,self.end = start,end
                self.moves = ADJACENTS[move_type]
                self.heuristic = HEURISTICS[move_type]
                self.barriers = barriers
                self.setup()

            def setup(self):
                """Initialize sets,dicts and others"""
                self.closed_set = set((self.start,)) #Set of cells already evaluated
                self.open_set   = set() #Set of cells to be evaluated.
                self.came_from = {} #Used to reconstruct path once solved.
                self.gx = {self.start:0} #Cost from start to current position.
                self.hx = {} #Optimal estimate to goal based on heuristic.
                self.fx = {} #Distance-plus-cost heuristic function.
                self.current = self.start
                self.current = self.follow_current_path()
                self.solution = []
                self.solved = False

            def get_neighbors(self):
                """Find adjacent neighbors with respect to how our agent moves."""
                neighbors = set()
                for (i,j) in self.moves:
                    check = (self.current[0]+i,self.current[1]+j)
                    if check not in (self.barriers|self.closed_set):
                        neighbors.add(check)
                return neighbors

            def follow_current_path(self):
                """In the very common case of multiple points having the same heuristic
                value, this function makes sure that points on the current path take
                presidence.  This is most obvious when trying to use astar on an
                obstacle free grid."""
                next_cell = None
                for cell in self.get_neighbors():
                    tentative_gx = self.gx[self.current]+1
                    if cell not in self.open_set:
                        self.open_set.add(cell)
                        tentative_best = True
                    elif cell in self.gx and tentative_gx < self.gx[cell]:
                        tentative_best = True
                    else:
                        tentative_best = False

                    if tentative_best:
                        x,y = abs(self.end[0]-cell[0]),abs(self.end[1]-cell[1])
                        self.came_from[cell] = self.current
                        self.gx[cell] = tentative_gx
                        self.hx[cell] = self.heuristic(x,y)
                        self.fx[cell] = self.gx[cell]+self.hx[cell]
                        if not next_cell or self.fx[cell]<self.fx[next_cell]:
                            next_cell = cell
                return next_cell

            def get_path(self,cell):
                """Recursively reconstruct the path. No real need to do it recursively."""
                if cell in self.came_from:
                    self.solution.append(cell)
                    self.get_path(self.came_from[cell])

            def evaluate(self):
                """Core logic for executing the astar algorithm."""
                if self.open_set and not self.solved:
                    for cell in self.open_set:
                        if (self.current not in self.open_set) or (self.fx[cell]<self.fx[self.current]):
                            self.current = cell
                    if self.current == self.end:
                        self.get_path(self.current)
                        self.solved = True
                    self.open_set.discard(self.current)
                    self.closed_set.add(self.current)
                    self.current = self.follow_current_path()
                elif not self.solution:
                    self.solution = "NO SOLUTION"
            
#-------------------------------------------------------------------
#        class PathFinder():
#            def __init__(self):
#                self.startPos = (0,0)
#                self.goalPos = (0,0)
#                self.OpenNodes = []
#                self.ClosedNodes = []
#                self.gScoreList = []
#                self.fScoreList = []
#                self.HeuristicValue = 0
#                
#                self.FOUND = 1
#                self.NONEXISTANT = 2
#            
#            def setStartPos(self, x, y):
#                self.startPos = (x, y)
#                
#            def setGoalPos(self, x, y):
#                self.goalPos = (x, y)
#            
#            def FindPath(self):
#                #0. reset lists
#                self.OpenNodes = []
#                self.ClosedNodes = []
#                self.gScoreList = []
#                self.fScoreList = []
#                
#                #1. Get Locations
#                startX = self.startPos[0]
#                startY = self.startPos[1]
#                targetX = self.goalPos[0]
#                targetY = self.goalPos[1]
#                
#                #2. Check Path is needed
#                if (startX == targetX and startY == targetY)
#                    return self.FOUND = 1
#                    
#                #3. Reset some variables
#                self.gScoreList[startX][startY] = 0
#                
#                #4. add starting Pos to Open list 
#                self.OpenNodes.append((startX,startY))
#-------------------------------------------------------------------
        class Unit():
            def __init__(self):
                self.Name = "Unit1"
                self.Image = Image("Unit1.png")
                self.X = 0
                self.Y = 0
                self.Atk = 0
                self.Def = 0
                self.Mov = 0
                self.Spd = 5
                self.moved = True
            
            def SetPos(self, x, y):  
                self.X = x
                self.Y = y              
        
            def SetMov(self, mov):  
                self.Mov = mov
                
#-------------------------------------------------------------------
        class BattleDisplayable(renpy.Displayable):
            def __init__(self):

                renpy.Displayable.__init__(self)

                # Some displayables we use.
                self.paddle = Image("Battle.png")
                self.ball = Image("Battle_ball.png")
                self.player = Text(_("Player"), size=36)
                self.princess = Text(_("Princess"), size=36)
                self.ctb = Text(_("Click to Begin"), size=36)
                self.tile1 = Image("grass1.png")
                self.tile2 = Image("ground1.png")
                self.tile3 = Image("water.png")
                self.tile4 = Image("forest.png")
                self.MoveTile = Image("pointerYELL.png")
                self.Pointer = Image("pointerBLUE.png")
                
                self.unit1 = Image("Unit1.png")

                self.tile = Image("BoardPiece.png")
                
                # The time of the past render-frame.
                self.oldst = None

                # The winner.
                self.winner = None
                self.ballListx=[]
                self.ballListy=[]
                self.ballcount=0
                
                self.UNITLIST=[]
                self.CurrUnitMove=[]
                
                #tiles
                self.tile_x=0
                self.tile_y=0
                self.tile_x2=0
                self.tile_y2=0
                self.map_x = SCREEN_WIDTH/2
                self.map_y = TILE_HEIGHT
                self.stategame = 1
                self.HighlightedUnitIndex = -1
                self.oldUnitIndex = -1
                self.HighlightedTile = (0,0)
                self.bDoMoveMap = False

                # miejsce na obrazki kafli
                self.tiles = []   

                # pozycja myszki w rzucie izometrycznym
                self.mousex=0
                self.mousey=0   
                
            def iso2screen(self,x,y):
               xx = (x-y)*(TILE_WIDTH/2)
               yy = (x+y)*(TILE_HEIGHT/2)
               return xx,yy
               
               
            def screen2iso(self,x,y):
              x = x/2
              xx = (y+x)/(TILE_WIDTH/2)
              yy = (y-x)/(TILE_WIDTH/2)
              return xx,yy
            
            def draw_map(self, st, at,r):            
              for x in range(MAP_WIDTH):
                for y in range(MAP_HEIGHT):
                  atile = MAP[y][x]
                  aunit = UNITMAP[y][x]
                  tile_x, tile_y = self.iso2screen(x,y)
                  tile1 = renpy.render(self.tile1, SCREEN_WIDTH, SCREEN_HEIGHT, st, at)
                  tile2 = renpy.render(self.tile2, SCREEN_WIDTH, SCREEN_HEIGHT, st, at)
                  tile3 = renpy.render(self.tile3, SCREEN_WIDTH, SCREEN_HEIGHT, st, at)
                  tile4 = renpy.render(self.tile4, SCREEN_WIDTH, SCREEN_HEIGHT, st, at)
                  unit1 = renpy.render(self.unit1, SCREEN_WIDTH, SCREEN_HEIGHT, st, at)
                  if (atile == TILE_GRASS):
                    r.blit(tile1, (tile_x+self.map_x, tile_y+self.map_y))
                  elif(atile == TILE_DIRT):
                    r.blit(tile2, (tile_x+self.map_x, tile_y+self.map_y))
                  elif(atile == TILE_WATER):
                    r.blit(tile3, (tile_x+self.map_x, tile_y+self.map_y))
                  else:
                    r.blit(tile4, (tile_x+self.map_x, tile_y+self.map_y-8))
              
              for i in range(self.ballcount):  
                tile_x, tile_y = self.iso2screen(self.UNITLIST[i].X, self.UNITLIST[i].Y)           
                unit = renpy.render(self.UNITLIST[i].Image, SCREEN_WIDTH, SCREEN_HEIGHT, st, at)
                r.blit(unit, (tile_x+self.map_x, tile_y+self.map_y))
                
                if (i == self.ballcount-1):
                    self.player = Text(str(self.UNITLIST[i].X), size=36)
                    self.princess = Text(str(self.UNITLIST[i].Y), size=36)
                    # Show the player names.
                    player = renpy.render(self.player, SCREEN_WIDTH, SCREEN_HEIGHT, st, at)
                    r.blit(player, (20, 70))

                    # Show Princess's name.
                    princess = renpy.render(self.princess, SCREEN_WIDTH, SCREEN_HEIGHT, st, at)
                    ew, eh = princess.get_size()
                    r.blit(princess, (790 - ew, 70))
                
                  
            def getUnitAtMouse(self, x,y):
              for i in range(self.ballcount):  
                if ((self.UNITLIST[i].X == x) and (self.UNITLIST[i].Y == y)):
                    return i
                
              return -1
            
            def DrawTileAt(self, r, tile, x, y):
                tile_x, tile_y = self.iso2screen(x, y) 
                r.blit(tile, (tile_x+self.map_x, tile_y+self.map_y))
                
            def IsInMapBounds(self, x, y):
                if ((x >= 0 and x < MAP_WIDTH) and
                    (y >= 0 and y < MAP_HEIGHT) ):
                    return True
                else:
                    return False
            
            def IsTileCrossable(self, x, y):
                if ((MAP[y][x] == TILE_WATER) or 
                     (self.getUnitAtMouse(x, y) != -1 and
                     self.getUnitAtMouse(x, y) != self.HighlightedUnitIndex)):
                    return False
                else:
                    return True            
            
            def CanMoveToSurroundingTiles(self, x,y, mov):
                if ((self.IsInMapBounds(x, y) == True)):
                    if ((MAP[y][x] == TILE_FOREST)):
                        mov = mov-1
                    if ((mov > 0) and self.IsTileCrossable(x,y) == True):
                        if ((self.IsPosTaken(self.CurrUnitMove, x, y) == False)):
                            self.CurrUnitMove.append((x,y))
                        self.CanMoveToSurroundingTiles(x+1,y, mov-1)
                        self.CanMoveToSurroundingTiles(x-1,y, mov-1)
                        self.CanMoveToSurroundingTiles(x,y+1, mov-1)
                        self.CanMoveToSurroundingTiles(x,y-1, mov-1)
            
            def IsPosTaken(self, list, x, y):
                for i in range(len(self.CurrUnitMove)): 
                    if (list[i][0] == x and list[i][1] == y):
                        return True
                return False
                
            #def CalcUnitRange(self, x, y, mov):

            
            def DrawUnitRange(self, hUnitIndex, st, at, r):
                iUnitIndex = int(hUnitIndex)
                tile_x, tile_y = self.iso2screen(self.UNITLIST[iUnitIndex].X,self.UNITLIST[iUnitIndex].Y)
                tile1 = renpy.render(self.MoveTile, SCREEN_WIDTH, SCREEN_HEIGHT, st, at)
                MoveRange = self.UNITLIST[iUnitIndex].Mov+1
                PosX = self.UNITLIST[iUnitIndex].X
                PosY = self.UNITLIST[iUnitIndex].Y  
                if (iUnitIndex != self.oldUnitIndex or self.UNITLIST[iUnitIndex].moved):
                    del self.CurrUnitMove[:]
                    self.CanMoveToSurroundingTiles(PosX, PosY, MoveRange)
                    self.oldUnitIndex = iUnitIndex                    
                    self.UNITLIST[iUnitIndex].moved = False
                
                for i in range(len(self.CurrUnitMove)):
                    self.DrawTileAt(r, tile1, self.CurrUnitMove[i][0], self.CurrUnitMove[i][1])
                                        
                        
            def canMoveTo(self, x, y):
                for i in range(len(self.CurrUnitMove)):
                    if (self.CurrUnitMove[i][0] == x and  self.CurrUnitMove[i][1] == y):
                        return True
                return False
                
            def MoveUnit(self, index, x, y):
                self.UNITLIST[index].X = x
                self.UNITLIST[index].Y = y
                self.UNITLIST[index].moved = True
            
            def visit(self):
                return [ self.paddle, self.ball, self.player, self.princess, self.ctb ]

            # Recomputes the position of the ball, handles bounces, and
            # draws the screen.
            def render(self, width, height, st, at):

                # The Render object we'll be drawing into.
                r = renpy.Render(width, height)

                # Figure out the time elapsed since the previous frame.
                if self.oldst is None:
                    self.oldst = st

                dtime = st - self.oldst
                self.oldst = st

                ball = renpy.render(self.ball, SCREEN_WIDTH, SCREEN_HEIGHT, st, at)
                # Draw the ball.
                #for i in range(0,self.ballcount):
                #    r.blit(ball, (self.ballListx[i],self.ballListy[i]))
                #r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2),
                #              int(self.by - self.BALL_HEIGHT / 2)))

                self.player = Text(str(self.map_x), size=36)
                self.princess = Text(str(self.map_y), size=36)
                # Show the player names.
                player = renpy.render(self.player, SCREEN_WIDTH, SCREEN_HEIGHT, st, at)
                r.blit(player, (20, 25))
                
                # Show princess's name.
                princess = renpy.render(self.princess, SCREEN_WIDTH, SCREEN_HEIGHT, st, at)
                ew, eh = princess.get_size()
                r.blit(princess, (790 - ew, 25))
                #
                #self.player = Text(str(self.tile_x2), size=36)
                #self.princess = Text(str(self.tile_y2), size=36)
                ## Show the player names.
                #player = renpy.render(self.player, SCREEN_WIDTH, SCREEN_HEIGHT, st, at)
                #r.blit(player, (20, 50))
                #
                ## Show princess's name.
                #princess = renpy.render(self.princess, SCREEN_WIDTH, SCREEN_HEIGHT, st, at)
                #ew, eh = princess.get_size()
                #r.blit(princess, (790 - ew, 50))
                #
                #self.player = Text(str(self.HighlightedUnitIndex), size=36)
                #player = renpy.render(self.player, SCREEN_WIDTH, SCREEN_HEIGHT, st, at)
                #r.blit(player, (20, 90))

                
                # Show the tile.
                #tile = renpy.render(self.tile, SCREEN_WIDTH, SCREEN_HEIGHT, st, at)
                #r.blit(tile, (self.tile_x, self.tile_y))
                
                self.draw_map(st, at,r)
                
                if (self.ballcount > 0):
                    if (self.HighlightedUnitIndex != -1):
                        self.DrawUnitRange(self.HighlightedUnitIndex, st, at, r)
                        #self.DrawUnitRange(0, st, at, r)
                
                if (self.IsInMapBounds(self.HighlightedTile[0],self.HighlightedTile[1])):
                    tile_x, tile_y = self.iso2screen(self.HighlightedTile[0],self.HighlightedTile[1])
                    #tile_x, tile_y = self.HighlightedTile[0],self.HighlightedTile[1]
                    tile1 = renpy.render(self.Pointer, SCREEN_WIDTH, SCREEN_HEIGHT, st, at)
                    r.blit(tile1, (tile_x+self.map_x, tile_y+self.map_y))
                    ##
                    self.player = Text(str(tile_x), size=36)
                    self.princess = Text(str(tile_y), size=36)
                    # Show the player names.
                    player = renpy.render(self.player, SCREEN_WIDTH, SCREEN_HEIGHT, st, at)
                    r.blit(player, (20, 50))
    
                    # Show princess's name.
                    princess = renpy.render(self.princess, SCREEN_WIDTH, SCREEN_HEIGHT, st, at)
                    ew, eh = princess.get_size()
                    r.blit(princess, (790 - ew, 50))
                
                # Ask that we be re-rendered ASAP, so we can show the next
                # frame.
                renpy.redraw(self, 0)

                # Return the Render object.
                return r
            # Handles events.
            def event(self, ev, x, y, st):

                import pygame
                x3=x
                y3=y
                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                    self.winner = "player"

                self.tile_x2 =x
                self.tile_y2 =y
                #x-=((TILE_WIDTH/2))
                #y-=(TILE_HEIGHT/2)
                #self.tile_x, self.tile_y = self.iso2screen(x,y)
                self.tile_x, self.tile_y = self.screen2iso(x+self.map_x,y+self.map_y)
                
                # Mousebutton down == start the game by setting stuck to
                # false.
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 2:
                    x2 = x
                    y2 = y
                    x2-=(self.map_x+(TILE_WIDTH/2))
                    y2-=(self.map_y)
                    self.stuck = False
                    
                    IsoX, IsoY = self.screen2iso(x2,y2)
                    if (self.getUnitAtMouse(IsoX, IsoY) == -1):
                        self.ballListx.append(x2)
                        self.ballListy.append(y2)
                        self.ballcount = self.ballcount+1
                        newUnit = Unit()
                        newUnit.SetPos(IsoX, IsoY)
                        newUnit.SetMov(5)
                        self.UNITLIST.append(newUnit)    
                
                x-=(self.map_x+(TILE_WIDTH/2))
                y-=(self.map_y)
                IsoX, IsoY = self.screen2iso(x,y)
                self.HighlightedTile = (IsoX, IsoY)              
                                
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                    if ((self.HighlightedUnitIndex != -1) and self.canMoveTo(IsoX, IsoY)):
                        self.MoveUnit(self.HighlightedUnitIndex, IsoX, IsoY)
                    else:
                        self.HighlightedUnitIndex = self.getUnitAtMouse(IsoX, IsoY)
                
                    
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 3:
                    self.bDoMoveMap = True;
                    
                if ev.type == pygame.MOUSEBUTTONUP and ev.button == 3:
                    self.bDoMoveMap = False

                
                if (self.bDoMoveMap == True):
                    if (self.IsInMapBounds(IsoX, IsoY)):
                        relativeX = (IsoX - MAP_WIDTH/2)
                        relativeY = (IsoY - MAP_HEIGHT/2)
                        newX, newY = self.iso2screen(relativeX,relativeY)
                        self.map_x = (self.map_x - newX) if (self.map_x/2 > SCREEN_WIDTH/2) else (self.map_x + newX)
                        self.map_y = (self.map_y - newY) if (self.map_y/2 > SCREEN_HEIGHT/2) else (self.map_y + newY)
                
                    
                # If we have a winner, return him or her. Otherwise, ignore
                # the current event.
                if self.winner:
                    return self.winner
                else:
                    raise renpy.IgnoreEvent()

                
#-------------------------------------------------------------------
                
label demo_minigame:

    e "You may want to mix Ren'Py with other forms of gameplay. There are many ways to do this."

    e "The first is with the UI functions, which can be used to create powerful button and menu based interfaces."

    e "These are often enough for many simulation-style games."

    e "We also have two more ways in which Ren'Py can be extended. Both require experience with Python programming, and so aren't for the faint of heart."

    e "Renpygame is a library that allows pygame games to be run inside Ren'Py."

    e "When using renpygame, Ren'Py steps out of the way and gives you total control over the user's experience."

    e "You can get renpygame from the Frameworks page of the Ren'Py website."

    e "If you want to integrate your code with Ren'Py, you can write a user-defined displayable."

    e "User-defined displayables are somewhat more limited, but integrate better with the rest of Ren'Py."

    e "For example, one could support loading and saving while a user-defined displayable is shown."

    e "Now, why don't we play some Battle?"

label demo_minigame_Battle:

    window hide None

    # Put up the Battle background, in the usual fashion.
    scene bg Battle field

    # Run the Battle minigame, and determine the winner.
    python:
        ui.add(BattleDisplayable())
        winner = ui.interact(suppress_overlay=True, suppress_underlay=True)

    scene bg washington
    show princess happy at right

    window show None


    if winner == "princess":

        e "I win!"

    else:

        e "You won! Congratulations."


    show princess happy at right

    menu:
        e "Would you like to play again?"

        "Sure.":
            jump demo_minigame_Battle
        "No thanks.":
            pass


    e "Remember to be careful about putting minigames in a visual novel, since not every visual novel player wants to be good at arcade games."

    return

    
    # You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image princess happy = "princess_happy.png"

# Declare characters used by this game.
define e = Character('princess', color="#c8ffc8")


# The game starts here.
label start:

    jump demo_minigame_Battle
    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"
    jump demo_minigame_Battle
    return
