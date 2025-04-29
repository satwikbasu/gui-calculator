from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("360x550")
root.configure(bg="lightblue")
root.resizable(False, False)

index = 0

def get_number(number):
    global index
    input.insert(index, number)
    index += 1

def get_operations(operator):
    global index
    if operator == "AC":
        input.delete(0, END)
        index = 0
        return
    length=len(operator)
    input.insert(index, operator)
    index += length

inputframe = Frame(root, bg="lightblue")
inputframe.grid(row=0, column=0, padx=5, pady=5)
input = Entry(inputframe,width=30, borderwidth=5,font=("Arial", 11))
input.grid(row=0, column=0, rowspan=5, columnspan=6, ipadx=40, padx=10, pady=10)

numberframe = Frame(root,bg="lightblue")
numberframe.grid(row=1, column=0)
numbers=[1,2,3,4,5,6,7,8,9]
count=0
for i in range(0,3):
    for j in range(0,3):
        buttontext = numbers[count]
        button = Button(numberframe, text=buttontext, padx=5, pady=5, font=("Arial", 11),width=4,command=lambda x=buttontext:get_number(x))
        button.configure(bg="#63bcee")
        button.grid(row=i, column=j, padx=10, pady=10)
        count += 1
button0 = Button(numberframe, text="0", padx=5, pady=5, font=("Arial", 11),width=4,command=lambda :get_number(0),bg="#63bcee")
button0.grid(row=3, column=1, padx=10, pady=10)

operations=["AC", "+", "-", "*", "/", "=","**","%","*3.14","**2","(",")"]
operationsframe = Frame(root,bg="lightblue")
operationsframe.grid(row=2, column=0)
for i in range(4):
    for j in range(3):
        button = Button(operationsframe, text=operations[i*3+j], padx=5, pady=5, font=("Arial", 10),width=4,command=lambda x=operations[i*3+j]:get_operations(x))
        button.configure(bg="#63bcee",fg="darkblue")
        button.grid(row=i, column=j, padx=10, pady=10)

root.mainloop()