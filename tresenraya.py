from turtle import *
from time import *
speed(0)
def cuadrado():
	i=0
	while i<4:
		forward(50)
		right(90)
		i=i+1
def x(ejex,ejey):
	penup()
	goto(ejex,ejey)
	setheading(0)
	pendown()
	right(45)
	forward(70.7106781187)
	right(45+90)
	forward(50)
	right(90+45)
	forward(70.7106781187)
	
def circulo(ejex,ejey):
	penup()
	goto(ejex,ejey)
	setheading(0)
	right(90)
	forward(50)
	left(90)
	forward(25)
	pendown()
	circle(25)
	
def posicionx(c):
	if c==1:
		ejex=0
	elif c==2:
		ejex=50
	elif c==3:
		ejex=100
	elif c==4:
		ejex=0
	elif c==5:
		ejex=50
	elif c==6:
		ejex=100
	elif c==7:
		ejex=0
	elif c==8:
		ejex=50
	elif c==9:
		ejex=100
	return(ejex)

def posiciony(c):
	if c==1:
		ejey=0
	elif c==2:
		ejey=0
	elif c==3:
		ejey=0
	elif c==4:
		ejey=-50
	elif c==5:
		ejey=-50
	elif c==6:
		ejey=-50
	elif c==7:
		ejey=-100
	elif c==8:
		ejey=-100
	elif c==9:
		ejey=-100
	return(ejey)
		
		
	
#cuadricula
penup()
goto(0,0)
pendown()
cuadrado()
goto(50,0)
cuadrado()
goto(100,0)
cuadrado()
penup()
goto(0,-50)
pendown()
cuadrado()
goto(50,-50)
cuadrado()
goto(100,-50)
cuadrado()
penup()
goto(0,-100)
pendown()
cuadrado()
goto(50,-100)
cuadrado()
goto(100,-100)
cuadrado()
sleep(1)

turno=1
while turno<=9:
	if turno%2!=0:
		c=int(input('turno de la Equis. Dime en qué casilla del 1 al 9'))
		ejex=posicionx(c)
		ejey=posiciony(c)
		x(ejex,ejey)	
		turno=turno+1
	else:
		c=int(input('turno del círculo. Dime en qué casilla del 1 al 9'))
		ejex=posicionx(c)
		ejey=posiciony(c)
		circulo(ejex,ejey)	
		turno=turno+1

	
