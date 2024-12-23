import pgzrun

#setting outputs width and height of screen

WIDTH = 500
HEIGHT = 700

#title of the output width
TITLE= "square shapes project"
# putting shapes on the screen.
def draw():
    corner1 = (0,0)
    corner2 =(150,150)
    square=Rect(corner1,corner2)
    #adding the created square on screen
    screen.draw.rect(square,(0,255,0))#0,255,0 is the rgb colour for green

    #DRAWING A LINE 
    screen.draw.line((300,350),(400,400),(0,255,0))



    
    
    
    
pgzrun.go()