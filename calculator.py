import tkinter
from tkinter import *

root = Tk()
root.title("Nsereko kayongo julius Calculator")
root.geometry("340x570")
root.resizable(False, False)
root.config(bg="black")

equation = ""


def show(value):
    global equation
    equation += str(value)
    LABEL_RESULT.config(text=equation)


def clear():
    global equation
    equation = ""
    LABEL_RESULT.config(text=equation)


def calculate():
    global equation
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "Error"
            equation = ""

    LABEL_RESULT.config(text=result)


LABEL_RESULT = Label(root, width=14, height=2, text="", font=("arial", 30))
LABEL_RESULT.pack()

Button(root, text="C", width=2, height=1, font=(
    "arial", 30, "bold"), bd=1, fg="white", bg="#3697f5", command=lambda: clear()).place(x=10, y=100)
Button(root, text="/", width=2, height=1, font=(
    "arial", 30, "bold"), bd=1, fg="white", bg="#2a2d36", command=lambda: show("/")).place(x=90, y=100)
Button(root, text="%", width=2, height=1, font=(
    "arial", 30, "bold"), bd=1, fg="white", bg="#2a2d36", command=lambda: show("%")).place(x=170, y=100)
Button(root, text="*", width=2, height=1, font=(
    "arial", 30, "bold"), bd=1, fg="white", bg="#2a2d36", command=lambda: show("*")).place(x=250, y=100)

Button(root, text="7", width=2, height=1, font=(
    "arial", 30, "bold"), bd=1, fg="white", bg="#2a2d36", command=lambda: show("7")).place(x=10, y=170)
Button(root, text="8", width=2, height=1, font=(
    "arial", 30, "bold"), bd=1, fg="white", bg="#2a2d36", command=lambda: show("8")).place(x=90, y=170)
Button(root, text="9", width=2, height=1, font=(
    "arial", 30, "bold"), bd=1, fg="white", bg="#2a2d36", command=lambda: show("9")).place(x=170, y=170)
Button(root, text="-", width=2, height=1, font=(
    "arial", 30, "bold"), bd=1, fg="white", bg="#2a2d36", command=lambda: show("-")).place(x=250, y=170)

Button(root, text="4", width=2, height=1, font=(
    "arial", 30, "bold"), bd=1, fg="white", bg="#2a2d36", command=lambda: show("4")).place(x=10, y=240)
Button(root, text="5", width=2, height=1, font=(
    "arial", 30, "bold"), bd=1, fg="white", bg="#2a2d36", command=lambda: show("5")).place(x=90, y=240)
Button(root, text="6", width=2, height=1, font=(
    "arial", 30, "bold"), bd=1, fg="white", bg="#2a2d36", command=lambda: show("6")).place(x=170, y=240)
Button(root, text="+", width=2, height=1, font=(
    "arial", 30, "bold"), bd=1, fg="white", bg="#2a2d36", command=lambda: show("+")).place(x=250, y=240)

Button(root, text="1", width=2, height=1, font=(
    "arial", 30, "bold"), bd=1, fg="white", bg="#2a2d36", command=lambda: show("1")).place(x=10, y=310)
Button(root, text="2", width=2, height=1, font=(
    "arial", 30, "bold"), bd=1, fg="white", bg="#2a2d36", command=lambda: show("2")).place(x=90, y=310)
Button(root, text="3", width=2, height=1, font=(
    "arial", 30, "bold"), bd=1, fg="white", bg="#2a2d36", command=lambda: show("3")).place(x=170, y=310)
Button(root, text="0", width=5, height=1, font=(
    "arial", 30, "bold"), bd=1, fg="white", bg="#2a2d36", command=lambda: show("0")).place(x=10, y=380)

Button(root, text=".", width=2, height=1, font=(
    "arial", 30, "bold"), bd=1, fg="white", bg="#2a2d36", command=lambda: show(".")).place(x=170, y=380)
Button(root, text="=", width=2, height=3, font=(
    "arial", 30, "bold"), bd=1, fg="white", bg="green", command=lambda: calculate()).place(x=250, y=310)

root.mainloop()
