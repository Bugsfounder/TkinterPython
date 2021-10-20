from tkinter import *

root = Tk()
root.title("Learning Canvas Using Python tkinter")

# CANCAS HERE 
canvasWidth = 800
canvasHeight = 400
root.geometry(f"{canvasWidth}x{canvasHeight}")

canvasWidget = Canvas(root, width=canvasWidth, height=canvasHeight)
canvasWidget.pack()

# THE LINE GOES FROM THE POINT X1, Y1 TO X2, Y2 
canvasWidget.create_line(0, 0, 800, 400, fill='red')
canvasWidget.create_line(0, 400, 800, 0, fill='red')

# TO CREATE A RECTANGEL SPECIFY PARAMETERS IN THIS ORDER - COORS OF TOP LEFT AND COORS FO BOTTOM RIGHT 
# canvasWidget.create_rectangle(3,5,800,400)
canvasWidget.create_rectangle(2,3,800,400, fill='BLUE')


# canvasWidget.create_oval(200,200,800,400, fill='red')
# canvasWidget.create_oval(0,0,400,400, fill='red')

canvasWidget.create_window(200, 400)
canvasWidget.create_image(200,400)

canvasWidget.create_text(200,200, text="This is The Text", font=("", 20, "bold"))
root.mainloop()