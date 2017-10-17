import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox

win = tk.Tk()
win.title("Python GUI")
tabControl = ttk.Notebook(win)     #Create Tab Control
tab1=ttk.Frame(tabControl)         #Create a tab
tabControl.add(tab1,text="Tab 1")  #Pack to make visible
tabControl.pack(expand=1,fill="both")
tab2=ttk.Frame(tabControl)         #Add a second tab
tabControl.add(tab2,text='Tab 2')  #Make second tab visible

monty = ttk.LabelFrame(tab1,text='Monty Python')
monty.grid(column=0,row=0)
monty2=ttk.LabelFrame(tab2,text='The Snake')
monty2.grid(column=0,row=0,padx=8,pady=4)



#We are creating a container frame to hold all other widgets #1
#monty=ttk.LabelFrame(win,text='Monty Python')

#Adding a  Label
#ttk.Label(win,text="A Label").grid(column=0,row=0)
aLabel= ttk.Label(monty,text="A Label")
aLabel.grid(column=0,row=0)

def clickMe():
    #action.configure(text="** I have been Clicked! **")
    #aLabel.configure(foreground='red')
    action.configure(text='Hello '+name.get())
    #action.configure(state='disabled')
    #action.grid(column=1,row=3)

    #changing our label
ttk.Label(monty,text="Enter a name:").grid(column=0,row=0,sticky='W')

    #Adding a Textbox Entry widget
name=tk.StringVar()
nameEntered=ttk.Entry(monty,width=12,textvariable=name)
nameEntered.focus()
nameEntered.grid(column=0,row=1,sticky=tk.W)

action=ttk.Button(monty,text="Click Me",command=clickMe)
action.grid(column=2,row=1)

ttk.Label(monty,text="Choose a number:").grid(column=1,row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(monty,width=12,textvariable=number)
numberChosen['values']=(1,2,4,42,100)
numberChosen.grid(column=1,row=1)
numberChosen.current(0)

#Creating three checkbuttons
chVarDis = tk.IntVar()
check1=tk.Checkbutton(monty2,text='Disabled',variable=chVarDis,state='disabled')
check1.select()
check1.grid(column=0,row=0,sticky=tk.W)

chVarUn = tk.IntVar()
check2=tk.Checkbutton(monty2,text='UnChecked',variable=chVarUn)

check2.deselect()  #setting default not selected
check2.grid(column=1,row=0,sticky=tk.W)

chVarEn = tk.IntVar()
check3=tk.Checkbutton(monty2,text='Enabled',variable=chVarEn)
check3.select()
check3.grid(column=2,row=0,sticky=tk.W)
'''
#Using a scrolled Text control  #3
scrolW = 40              #4
scrolH = 3               #5
scr =scrolledtext.ScrolledText(monty2,width=scrolW,height=scrolH,wrap=tk.WORD)   #6
#scr.grid(column=0,sticky='WE',columnspan=3)
scr.grid(column=0,columnspan=3)                                               #7
'''
#Radiobutton Globals
'''COLOR1 = 'Blue'          #2
COLOR2 = 'Gold'          #3
COLOR3 = "Red"           #4

#Radiobutton Callback    #5
def radCall():           #6
    radSel=radVar.get()
    if radSel == 1 :
        win.configure(background=COLOR1)
        print(radSel)
    elif radSel == 2:
        win.configure(background=COLOR2)
        print(radSel)
    elif radSel == 3 :
        win.configure(background=COLOR3)
        print(radSel)
#create three Radiobuttons
radVar = tk.IntVar()
rad1 = tk.Radiobutton(win,text=COLOR1,variable=radVar,value=1,command=radCall)
rad1.grid(column=0,row=5,sticky=tk.W)

rad2 = tk.Radiobutton(win,text=COLOR2,variable=radVar,value=2,command=radCall)
rad2.grid(column=1,row=5,sticky=tk.W)

rad3 = tk.Radiobutton(win,text=COLOR3,variable=radVar,value=3,command=radCall)
rad3.grid(column=2,row=5,sticky=tk.W)
'''
#First, we change our Radiobutton global variables into a list.
colors = ["Blue","Gold","Red"]

#create three Radiobuttons using one variable
radVar = tk.IntVar()

def radCall():
    radSel=radVar.get()
    if radSel ==0:
        #win.configure(background=colors[0])
        monty2.configure(text='Blue')
    elif radSel == 1:
        #win.configure(background=colors[1])
        monty2.configure(text='Gold')
    elif radSel == 2:

        #win.configure(background=colors[2])
        monty2.configure(text='Red')
#Next we are selecting a non-existing index value for radVar
for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(monty2,text=colors[col],variable=radVar,value=col,command=radCall)
    curRad.grid(column=col,row=1,sticky=tk.W)

#We have also changed the callback function to be zero-based,using the
#list instead of module-level global variables.

#Radiobutton callback function


#Add this import to the top of the Python Module #1



#Create a container to hold labels
labelFrame=ttk.LabelFrame(monty2,text="Label in a Frame") #1
labelFrame.grid(column=0,row=2,padx=20,pady=40)  #the scrolledtext take 3 rowspan

#Place labels into the container element #2
ttk.Label(labelFrame,text="Label1").grid(column=0,row=0)  #;label in label Frame
ttk.Label(labelFrame,text="Label2").grid(column=0,row=1)
#ttk.Label(labelFrame,text="Label3").grid(column=0,row=2)

#for child in labelFrame.winfo_children():
 #   child.grid_configure(padx=8,pady=4)

#Place cursor into name Entry

def _quit():
    win.quit()
    win.destroy()
    exit()

menuBar = Menu(win)             #1
win.config(menu=menuBar)
#Now we add a menu to the bar and also assign a menu item to the menu
fileMenu = Menu(menuBar)        #2
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=_quit)
menuBar.add_cascade(label="File",menu=fileMenu)

#Dispaly a Message Box
#Callback function

def _msgBox():
#    mBox.showinfo('Python Message Info Box','A Python GUI created using tkinter:\nThe year is 2015.')
#    mBox.showwarning('Python Message Warning Box','A Python GUI created using tkinter:\nWarning:There might bea bug in this code')
#    answer=mBox.showerror("Encount error","A Python GUI created using tkinter :\nError:Houston ~ we Do have a serious Problem")
    answer = mBox.askyesno("Python Message Dual Choice Box","Are you sure you sure you really wish to do this?")

    print(answer)

    if answer == True:
        print("The input answer is True")
#Add menu items
fileMenu = Menu(menuBar,tearoff=0)    #tearoff disable can not pull out
helpMenu = Menu(menuBar,tearoff=0)
helpMenu.add_command(label="About",command=_msgBox)
menuBar.add_cascade(label="Help",menu=helpMenu)


nameEntered.focus()




monty.grid(column=0,row=0,padx=8,pady=4)
ttk.Label(monty,text="Enter a name:").grid(column=0,row=0,sticky='W')


chVarDis=tk.IntVar()
check1=tk.Checkbutton(monty2,text='Disabled',variable=chVarDis,state='disabled')

win.mainloop()