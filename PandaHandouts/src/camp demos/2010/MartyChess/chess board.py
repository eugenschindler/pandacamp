# To change this template, choose Tools | Templates
# and open the template in the editor.

from Panda import *
height = slider(min = 5, max = 25, init = 25)
angle= slider(min=0, max=2*pi,init=0)

camera.position = P3C(15,angle,height)
camera.hpr = P3toHPR(camera.position)

pl = pointLight(position=P3(3,-3,3))
al = ambientLight()

def launch(m, v):
    m.position = m.position.now() + P3(localTime/30.0*m.x1, localTime/40.0*m.y1, localTime*localTime/5.0)
    m.hpr = HPR(0, localTime * m.x1 / 10.0, 0)
    
def placepiece(m,x,y):
    m.position=P3(-4.5+x,4.5-y,0)
    m.x1 = static(x)
    m.y1 = static(y)
    m.react1(timeIs((x+y)/3.0 + 12), launch)

#WHITE PIECES
wK=modelHandle("King.egg",size = .3, color = Color(.6,.6,.6))
wH1=modelHandle("horse.egg",size = .19, color = Color(.6,.6,.6),hpr=HPR(pi/2,0,0))
wH2=modelHandle("horse.egg",size = .19, color = Color(.6,.6,.6),hpr=HPR(pi/2,0,0))
wQ=modelHandle("queen_1.egg",size = .6, color = Color(.6,.6,.6))
wP1=modelHandle("pawn.egg",size = .15, color = Color(.6,.6,.6))
wP2=modelHandle("pawn.egg",size = .15, color = Color(.6,.6,.6))
wP3=modelHandle("pawn.egg",size = .15, color = Color(.6,.6,.6))
wP4=modelHandle("pawn.egg",size = .15, color = Color(.6,.6,.6))
wP5=modelHandle("pawn.egg",size = .15, color = Color(.6,.6,.6))
wP6=modelHandle("pawn.egg",size = .15, color = Color(.6,.6,.6))
wP7=modelHandle("pawn.egg",size = .15, color = Color(.6,.6,.6))
wP8=modelHandle("pawn.egg",size = .15, color = Color(.6,.6,.6))
wb1=modelHandle("bishop_1.egg",size = .6, color = Color(.6,.6,.6))
wb2=modelHandle("bishop_1.egg",size = .6, color = Color(.6,.6,.6))
wr1=modelHandle("rook.egg",size = .15, color = Color(.6,.6,.6))
wr2=modelHandle("rook.egg",size = .15, color = Color(.6,.6,.6))

placepiece(wK,1,5)
placepiece(wH1,0,7)
placepiece(wH2,0,2)
placepiece(wQ,1,4)
placepiece(wP1,2,8.2)
placepiece(wP2,2,7.2)
placepiece(wP3,2,6.2)
placepiece(wP4,2,5.2)
placepiece(wP5,2,4.2)
placepiece(wP6,2,3.2)
placepiece(wP7,2,2.2)
placepiece(wP8,2,1.2)
placepiece(wb1,1,3)
placepiece(wb2,1,6)
placepiece(wr1,.5,8)
placepiece(wr2,.5,1)


#BLACK PIECES
bK=modelHandle("King.egg",size = .3, color = Color(.2,.2,.2))
bH1=modelHandle("horse.egg",size = .19, color = Color(.2,.2,.2),hpr=HPR(-pi/2,0,0))
bH2=modelHandle("horse.egg",size = .19, color = Color(.2,.2,.2),hpr=HPR(-pi/2,0,0))
bQ=modelHandle("queen_1.egg",size = .6, color = Color(.2,.2,.2))
bP1=modelHandle("pawn.egg",size = .15, color = Color(.2,.2,.2))
bP2=modelHandle("pawn.egg",size = .15, color = Color(.2,.2,.2))
bP3=modelHandle("pawn.egg",size = .15, color = Color(.2,.2,.2))
bP4=modelHandle("pawn.egg",size = .15, color = Color(.2,.2,.2))
bP5=modelHandle("pawn.egg",size = .15, color = Color(.2,.2,.2))
bP6=modelHandle("pawn.egg",size = .15, color = Color(.2,.2,.2))
bP7=modelHandle("pawn.egg",size = .15, color = Color(.2,.2,.2))
bP8=modelHandle("pawn.egg",size = .15, color = Color(.2,.2,.2))
bb1=modelHandle("bishop_1.egg",size = .6, color = Color(.2,.2,.2))
bb2=modelHandle("bishop_1.egg",size = .6, color = Color(.2,.2,.2))
br1=modelHandle("rook.egg",size = .15, color = Color(.2,.2,.2))
br2=modelHandle("rook.egg",size = .15, color = Color(.2,.2,.2))

placepiece(bK,8,5)
placepiece(bH1,9,7)
placepiece(bH2,9,2)
placepiece(bQ,8,4)
placepiece(bP1,7,8.2)
placepiece(bP2,7,7.2)
placepiece(bP3,7,6.2)
placepiece(bP4,7,5.2)
placepiece(bP5,7,4.2)
placepiece(bP6,7,3.2)
placepiece(bP7,7,2.2)
placepiece(bP8,7,1.2)
placepiece(bb1,8,3)
placepiece(bb2,8,6)
placepiece(br1,7.5,8)
placepiece(br2,7.5,1)



#camera.hpr = HPR(0,4.68,0)

#rectangle(P3(-4,4,0),P3(-4,3,0),P3(-3,4,0),color = black)
board = emptyModel()
for i in range(8) :
    for j in range(8) :
        r = rectangle(P3(i-4,4-j,0),P3(i-3,4-j,0),P3(i-4,3-j,0),color=choose((i+j)%2,black,white))
        r.reparentTo(board)

def moveBoard(m,v):
    board.position = P3(0,0,localTime)
    board.hpr = HPR(localTime*localTime/3, localTime/3, 0)
react1(timeIs(16), moveBoard)


start()