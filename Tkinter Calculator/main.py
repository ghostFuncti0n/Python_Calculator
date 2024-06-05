# importing tkinter 
from tkinter import *
from tkinter import ttk

# colors used
color1 = "#242322" #black
color2 = "#faf3de" #white
color3 = "#fa1302" #red
color4 = "#07a807" #green
color5 = "#d3d9e3" #gray

# creating the window
window = Tk()
window.title("Calculator")
window.geometry("235x310")
window.config(bg= color1)

# creating frames
frame_screen = Frame(window, width= 235, height= 50, bg= color4)
frame_screen.grid(row= 0, column= 0)

frame_body = Frame(window, width= 235, height= 268)
frame_body.grid(row= 1, column= 0)

#all values variables

all_values = ''

#creating the functions

def enter_values(event):

    global all_values;
    all_values = all_values +  str(event); 
    
   
# showing numbers in the screen

    text_value.set(all_values)

#function to calculate 

def calculate():
      global all_values
      result = eval(all_values)
      
      text_value.set(str(result))

#clear_screen function

def clear_screen():
     global all_values
     all_values = ""
     text_value.set("")


# creating labels
text_value = StringVar()

app_label = Label(frame_screen, textvariable=text_value, width= 16, height= 2, padx=7 , relief=FLAT, anchor="e", justify="right", font=('Ivy 18 '), bg=color4, fg=color2)
app_label.place(x=0, y=0)

  

# creating buttons
b_clear = Button(frame_body, command=clear_screen, text="C", width=11, height=2, bg= color5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_clear.place(x=0, y=0)
b_1 = Button(frame_body, command=lambda:enter_values('%'), text="%", width=5, height=2, bg=color5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_1.place(x=118, y=0)
b_2 = Button(frame_body, command=lambda:enter_values('/'), text="/", width=5, height=2, bg= color3, fg= color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=177, y=0)

b_3 = Button(frame_body, command=lambda:enter_values('7'),text="7", width=5, height=2, bg=color5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_3.place(x=0, y=52)
b_4 = Button(frame_body, command=lambda:enter_values('8'),text="8", width=5, height=2, bg=color5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_4.place(x=59, y=52)
b_5 = Button(frame_body, command=lambda:enter_values('9'),text="9", width=5, height=2, bg=color5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_5.place(x=118, y=52)
b_6 = Button(frame_body, command=lambda:enter_values('*'),text="*", width=5, height=2, bg= color3, fg= color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_6.place(x=177, y=52)

b_7 = Button(frame_body, command=lambda:enter_values('4'),text="4", width=5, height=2, bg=color5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=104)
b_8 = Button(frame_body, command=lambda:enter_values('5'),text="5", width=5, height=2, bg=color5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_8.place(x=59, y=104)
b_9 = Button(frame_body, command=lambda:enter_values('6'),text="6", width=5, height=2, bg=color5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_9.place(x=118, y=104)
b_10 = Button(frame_body,command=lambda:enter_values('-'),text="-", width=5, height=2, bg= color3, fg= color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_10.place(x=177, y=104)

b_11 = Button(frame_body,command=lambda:enter_values('1'),text="1", width=5, height=2, bg=color5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_11.place(x=0, y=156)
b_12 = Button(frame_body,command=lambda:enter_values('2'),text="2", width=5, height=2, bg=color5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_12.place(x=59, y=156)
b_13 = Button(frame_body,command=lambda:enter_values('3'),text="3", width=5, height=2, bg=color5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_13.place(x=118, y=156)
b_14 = Button(frame_body,command=lambda:enter_values('+'),text="+", width=5, height=2, bg= color3, fg= color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_14.place(x=177, y=156)

b_15 = Button(frame_body,command=lambda:enter_values('0'),text="0", width=5, height=2, bg= color5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_15.place(x=0, y=208)
b_comma = Button(frame_body, command=lambda:enter_values(','), text=",", width=5, height=2, bg=color5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_comma.place(x=59, y=208)
b_equal = Button(frame_body, command= calculate, text="=", width=11, height=2, bg= color3, fg= color2, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_equal.place(x=118, y=208)

 

window.mainloop()