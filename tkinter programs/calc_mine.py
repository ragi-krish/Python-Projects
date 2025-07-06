from tkinter import *
root=Tk()
root.geometry("320x320")
root.title("CALCULATOR")
#root.resizable(0,0)
equation_txt=""

def num_click(num):
    global equation_txt
    equation_txt=equation_txt+str(num)
    entry_text.set(equation_txt)
    
def equals_fn():
    global equation_txt
    #the eval function evaluates the “String”
    #like a python expression and returns the
    #result as an integer.
    equation_txt=str(eval(equation_txt))
    
    entry_text.set(equation_txt)
    
def clear():
   global equation_txt
   entry_text.set("")
   equation_txt=""
def b_space():
    global equation_txt
    equation_txt=equation_txt[:-1]
    entry_text.set(equation_txt)
    
entry_text=StringVar()

txt_box=Entry(root,bd=2,width=40,textvariable=entry_text).grid(row=0,column=0,columnspan=4,pady=20)
btn_1=Button(text="1",width=10,command=lambda:num_click(1)).grid(row=1,column=0)
btn_2=Button(text="2",width=10,command=lambda:num_click(2)).grid(row=1,column=1)
btn_3=Button(text="3",width=10,command=lambda:num_click(3)).grid(row=1,column=2)
btn_plus=Button(text="+",width=10,command=lambda:num_click("+")).grid(row=1,column=3)


btn_4=Button(text="4",width=10,command=lambda:num_click(4)).grid(row=2,column=0)
btn_5=Button(text="5",width=10,command=lambda:num_click(5)).grid(row=2,column=1)
btn_6=Button(text="6",width=10,command=lambda:num_click(6)).grid(row=2,column=2)
btn_minus=Button(text="-",width=10,command=lambda:num_click("-")).grid(row=2,column=3)

btn_7=Button(text="7",width=10,command=lambda:num_click(7)).grid(row=3,column=0)
btn_8=Button(text="8",width=10,command=lambda:num_click(8)).grid(row=3,column=1)
btn_9=Button(text="9",width=10,command=lambda:num_click(9)).grid(row=3,column=2)
btn_x=Button(text="x",width=10,command=lambda:num_click('*')).grid(row=3,column=3)


btn_0=Button(text="0",width=10,command=lambda:num_click(0)).grid(row=4,column=0)
btn_dot=Button(text=".",width=10,command=lambda:num_click(".")).grid(row=4,column=1)
btn_equal=Button(text="=",width=10,command=equals_fn).grid(row=4,column=2)
btn_div=Button(text="/",width=10,command=lambda:num_click('/')).grid(row=4,column=3)



btn_clear=Button(text="C",width=20,command=clear).grid(row=5,column=0,columnspan=2)
btn_bspace=Button(text="<=",width=20,command=b_space).grid(row=5,column=2,columnspan=2)
root.mainloop()
