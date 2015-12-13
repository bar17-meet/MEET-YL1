import meet
import turtle

user_cell={'radius':15,'x':0,'y':0,'dx':0.1,'dy':0.2,'color':'red','shape':'circle'}
cell1={'radius':28,'x':-150,'y':-100,'dx':0.2,'dy':-0.10,'color':'orange','shape':'circle'}
cell2={'radius':25,'x':150,'y':-100,'dx':-0.2,'dy':-0.4,'color':'pink','shape':'circle'}
cell3={'radius':12,'x':100,'y':150,'dx':0.3,'dy':0.5,'color':'blue','shape':'circle'}
cell4={'radius':20,'x':120,'y':-130,'dx':0.8,'dy':0.9,'color':'green','shape':'circle'}
cell5={'radius':15,'x':170,'y':150,'dx':0.60,'dy':-0.5,'color':'yellow','shape':'circle'}

cells=[]
user_cell=meet.create_cell(user_cell)
cells.append(user_cell)
cell1=meet.create_cell(cell1)
cells.append(cell1)
cell2=meet.create_cell(cell2)
cells.append(cell2)
cell3=meet.create_cell(cell3)
cells.append(cell3)
cell4=meet.create_cell(cell4)
cells.append(cell4)
cell5=meet.create_cell(cell5)
cells.append(cell5)

def Edge(cells):
	for cell in cells:
		if cell.xcor() + cell.get_radius()>meet.get_screen_width():
			cell.set_dx(-cell.get_dx())
		if cell.xcor() + cell.get_radius()<-meet.get_screen_width():
			cell.set_dx(-cell.get_dx())
		if cell.ycor() + cell.get_radius()>meet.get_screen_height():
			cell.set_dy(-cell.get_dy())
		if cell.ycor() + cell.get_radius()<-meet.get_screen_height():
			cell.set_dy(-cell.get_dy())

global flag
flag = True
def Eating(cells):
	for cell in cells:	
		for cell2 in cells:
			if cell!=cell2:
				min_d = cell.get_radius()+cell2.get_radius()
				d = ((cell.xcor()-cell2.xcor())**2+(cell.ycor()-cell2.ycor())**2)**0.5
				if d<min_d:
					if cell.get_radius()>cell2.get_radius():
						if cell2==user_cell:
							turtle.pensize(50)
							turtle.write("Game Over!")
							meet.mainloop()
						x=meet.get_random_x()
						y=meet.get_random_y()
						cell2.goto(x,y)
						r = cell.get_radius() + 0.2 * cell2.get_radius() 
						cell.set_radius(r)
					if cell2.get_radius()>cell.get_radius():
						if cell==user_cell:
							turtle.pensize(50)
							turtle.write("Game Over!")
							meet.mainloop()
						x=meet.get_random_x()
						y=meet.get_random_y()
						cell.goto(x,y)
						r = cell2.get_radius() + 0.2 * cell.get_radius()
						cell2.set_radius(r)

while True:
	x, y = meet.get_user_direction(user_cell)
	user_cell.set_dx(x)
	user_cell.set_dy(y)
	meet.move_cells(cells)
	Edge(cells)
	Eating(cells)


meet.mainloop()