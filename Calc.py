#TO-DO

# 1:
# Add Negative/Positive Value to the num variables
# Add decimal Button
# Add Remove/Backspace buttton

from tkinter import *
root = Tk()

root.title("Calculator")
root.geometry("450x600")
root.configure(bg='white')


def clicked(number):
    global num_1
    global sign
    global saved_num_1
    
    if number == "=":
        if sign == "*":
            display.set(float(saved_num_1) * float(num_1))
            saved_num_1 = ""
            num_1 = ""
        
        elif sign == "-":
            display.set(float(saved_num_1) - float(num_1))
            saved_num_1 = ""
            num_1 = ""
        
        elif sign == "+":
            display.set(float(saved_num_1) + float(num_1))
            saved_num_1 = ""
            num_1 = ""

        elif sign == "/":
            display.set(float(saved_num_1) / float(num_1))
            saved_num_1 = ""
            num_1 = ""
    
    else:
        
        if number == "x":
            sign = str(number)
            display.set(sign)
            sign = "*"

            
            saved_num_1 = num_1
            num_1 = ""

            
        elif number == "-":
            sign = str(number)
            display.set(sign)
            sign = "-"

            
            saved_num_1 = num_1
            num_1 = ""

            
        elif number == "+":
            sign = str(number)
            display.set(sign)
            sign = "+"
            
            
            saved_num_1 = num_1
            num_1 = ""
            

        elif number == "/":
            sign = str(number)
            display.set(sign)
            sign = "/"

            
            saved_num_1 = num_1
            num_1 = ""

            
        else:
            
            if number == "squared":
                num_1 = str(float(num_1) ** 2)
                display.set(num_1)
                
            
            elif number == "div1":
                num_1 = str(round(1/float(num_1), 7))
                display.set(num_1)
            
            elif number == "back":
                
                num_1 = num_1[:-1]
                display.set(num_1)
            
            elif number == "pn":
                if num_1[0] != "-":
                    num_1 = str("-"+num_1)
                    display.set(num_1)
                else:
                    num_1 = str(num_1.replace(num_1[0],""))
            
            else:
                num_1 += str(number)
                display.set(num_1)


        

# Value's
num_1 = ""
sign = ""
num_2 = 0

saved_num_1 = ""

#Frame
frame = Frame(root,width=400, height=120,background='gray90', highlightbackground='black', highlightthickness= 5)
frame.pack()
frame.pack_propagate(0)
frame.place(x=25,y=10)

#Display
display = StringVar()
display.set(num_1)
display_label = Label(frame, textvariable= display, font = ("Times New Roman",50,'bold'), background='gray90')
#display.place(x = 180,y=10)
display_label.pack()



#||| BUTTONS |||

#NUMBERS
button_7 = Button(root,text = "7",command=lambda: clicked(7), height=2, width= 8, font = "bold")
button_7.place(x=10,y=230)

button_8 = Button(root,text = "8",command=lambda: clicked(8), height=2, width= 8, font = "bold")
button_8.place(x=120,y=230)

button_9 = Button(root,text = "9",command=lambda: clicked(9), height=2, width= 8, font = "bold")
button_9.place(x=230,y=230)

button_4 = Button(root,text = "4",command=lambda: clicked(4), height=2, width= 8, font = "bold")
button_4.place(x=10,y=310)

button_5 = Button(root,text = "5",command=lambda: clicked(5), height=2, width= 8, font = "bold")
button_5.place(x=120,y=310)

button_6 = Button(root,text = "6",command=lambda: clicked(6), height=2, width= 8, font = "bold")
button_6.place(x=230,y=310)

button_1 = Button(root,text = "1",command=lambda: clicked(1), height=2, width= 8, font = "bold")
button_1.place(x=10,y=390)

button_2 = Button(root,text = "2",command=lambda: clicked(2), height=2, width= 8, font = "bold")
button_2.place(x=120,y=390)

button_3 = Button(root,text = "3",command=lambda: clicked(3), height=2, width= 8, font = "bold")
button_3.place(x=230,y=390)

button_0 = Button(root,text = "0",command=lambda: clicked(0), height=2, width= 8, font = "bold")
button_0.place(x=120,y=470)

button_dec = Button(root,text = ".",command=lambda: clicked("."), height=2, width= 8, font = "bold")
button_dec.place(x=230,y=470)

button_sqr = Button(root,text = "x^2",command=lambda: clicked("squared"), height=2, width= 8, font = "bold")
button_sqr.place(x=230,y=150)

button_div1 = Button(root,text = "1/x",command=lambda: clicked("div1"), height=2, width= 8, font = "bold")
button_div1.place(x=120,y=150)

button_7 = Button(root,text = "⌫",command=lambda: clicked("back"), height=2, width= 8, font = "bold")
button_7.place(x=10,y=150)

button_pn = Button(root,text = "+/-",command=lambda: clicked("pn"), height=2, width= 8, font = "bold")
button_pn.place(x=10,y=470)

#OPERATION SIGNS
button_x = Button(root,text = "x",command=lambda: clicked("x"), height=2, width= 8, font = "bold")
button_x.place(x=340,y=230)

button_minus = Button(root,text = "-",command=lambda: clicked("-"), height=2, width= 8, font = "bold")
button_minus.place(x=340,y=310)

button_minus = Button(root,text = "+",command=lambda: clicked("+"), height=2, width= 8, font = "bold")
button_minus.place(x=340,y=390)

button_equal = Button(root,text = "=",command=lambda: clicked("="), height=2, width= 8, font = "bold")
button_equal.place(x=340,y=470)

button_div = Button(root,text = "/",command=lambda: clicked("/"), height=2, width= 8, font = "bold")
button_div.place(x=340,y=150)





root.mainloop()