from tkinter import *

window = Tk() #creates an empty window

#function
def km_to_miles():
    print(e1_value.get()) #printing the value in the terminal 
    miles = float(e1_value.get())*1.6 #converting
    t1.insert(END, miles) #PUT AT THE END OF THE TEXT (puts it into the text widget)

#create button widgets
b1 = Button(text = "Execute", command = km_to_miles)
b1.grid(row = 0, column = 0)

e1_value = StringVar() #place holder for what gets input
e1= Entry(window, textvariable = e1_value) #where you can enter something
e1.grid(row = 0, column =1)

t1 = Text(window, height = 1, width = 20)
t1.grid(row = 0, column = 2)

window.mainloop() #closes it