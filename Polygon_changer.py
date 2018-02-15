#####
#PROJECT BY OPHIR S. NANDHAN N. & LUCAS L.
#####

#####
#the goal is to change a slider
#and depending on its value 
#create a polygon with that many points
#####

#import Tkinter and Math for calculations
import Tkinter
import math
#####
#create a window
#####
root = Tkinter.Tk()
root.wm_title('Polygon Creator')
red = Tkinter.IntVar()
red.set(0)
blue = Tkinter.IntVar()
blue.set(0)
green = Tkinter.IntVar()
green.set(0)
circlevar=Tkinter.IntVar()
circlevar.set(0)
#####
#create canvas
#####
canvas = Tkinter.Canvas(root, width=500, height=500, background='#FFFFFF')
canvas.grid(row=0, rowspan=2, column=1)
new_shape=canvas.create_polygon((250, 0), (33.49364905389049, 375), (466.5063509461098, 375))
hexavariable = '#' + '00' + '00' + '00'
recent_coord=[250, 0]
temp_list=[]
plot_list=[(250,0)]
x1=recent_coord[-2]
y1=recent_coord[-1]
r=x1
circleoutline=canvas.create_oval(0,0,0,0)

def circleOutline():
    global circleoutline
    if len(temp_list)%2==0: 
        circleoutline=canvas.create_oval(1.5, 1.5, (2*r)-1, (2*r)-1)
    else:
        canvas.delete(circleoutline)
    temp_list.append(1)

def polygon():
    del plot_list[1:]
    del recent_coord[2:]
    canvas.delete(new_shape)
    n=int(nop.get())
    A=math.radians(((180*(n-2))/n))
    hA=(math.pi+(math.pi-A)/2)
    for i in range(n-1):
        sl=(500*math.cos(A/2))
        x=recent_coord[-2]+(sl*math.cos(hA+(i*(math.pi-A))))
        y=recent_coord[-1]-(sl*math.sin(hA+(i*(math.pi-A))))
        plot_list.append((x,y))
        recent_coord.append(x)
        recent_coord.append(y)
    global new_shape
    new_shape=canvas.create_polygon(plot_list, fill = hexavariable)
    
def colorchange():
    r = '00'
    g = '00'
    b = '00'
    if red.get() == 255:
        r = 'FF'
    if green.get() == 255:
        g = 'FF'
    if blue.get() == 255:
        b = 'FF'
    canvas.itemconfig(new_shape, fill = '#' + r + g + b)
    global hexavariable
    hexavariable = '#' + r + g + b
#####
#create controller
#####
redButton = Tkinter.Checkbutton(root, text = "red", variable = red, onvalue = 255, offvalue = 0, command = colorchange)
redButton.grid(row = 2, column = 0, sticky = Tkinter.W)
blueButton = Tkinter.Checkbutton(root, text = "blue", variable = blue, onvalue = 255, offvalue = 0, command = colorchange)
blueButton.grid(row = 3, column = 0, sticky = Tkinter.W)
greenButton = Tkinter.Checkbutton(root, text = "green", variable = green, onvalue = 255, offvalue = 0, command = colorchange)
greenButton.grid(row = 4, column = 0, sticky = Tkinter.W)
nop = Tkinter.Spinbox(root, from_=3, to=70, command=polygon)
nop.grid(row=1, column=0, sticky=Tkinter.W)
circleButton=Tkinter.Button(root, text="Outline of Circle", command=circleOutline) 
circleButton.grid(row=0, column=0, sticky=Tkinter.W)
print(circlevar.get())
root.mainloop()