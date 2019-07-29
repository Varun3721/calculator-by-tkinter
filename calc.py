from tkinter import *

whole_equation = ""


def pressed(inputs):
    global whole_equation

    whole_equation = whole_equation + str(inputs)

    var1.set(whole_equation)


def equalto():
    try:
        global whole_equation
        results = str(eval(whole_equation))
        var1.set(results)

        whole_equation = ""

    except:

        var1.set("its an error")
        whole_equation = ""


def clearscreen():
    global whole_equation
    whole_equation = ""
    var1.set(whole_equation)


if __name__ == "__main__":
    root = Tk()
    root.title("Calculator")
    var1 = StringVar()
    Output = Entry(root, textvariable=var1)
    Output.grid(columnspan=4, ipadx=80)
    var1.set("   ")

    button1 = Button(root, text="1", bg="black", fg="white", width=7, height=1, command=lambda: pressed(1))
    button2 = Button(root, text="2", bg="black", fg="white", width=7, height=1, command=lambda: pressed(2))

    button3 = Button(root, text="3", bg="black", fg="white", width=7, height=1, command=lambda: pressed(3))

    button4 = Button(root, text="4", bg="black", fg="white", width=7, height=1, command=lambda: pressed(4))
    button5 = Button(root, text="5", bg="black", fg="white", width=7, height=1, command=lambda: pressed(5))
    button6 = Button(root, text="6", bg="black", fg="white", width=7, height=1, command=lambda: pressed(6))
    button7 = Button(root, text="7", bg="black", fg="white", width=7, height=1, command=lambda: pressed(7))
    button8 = Button(root, text="8", bg="black", fg="white", width=7, height=1, command=lambda: pressed(8))
    button9 = Button(root, text="9", bg="black", fg="white", width=7, height=1, command=lambda: pressed(9))
    button0 = Button(root, text="0", bg="black", fg="white", width=7, height=1, command=lambda: pressed(0))
    ADD = Button(root, text="+", bg="black", fg="white", width=7, height=1, command=lambda: pressed("+"))
    SUB = Button(root, text="-", bg="black", fg="white", width=7, height=1, command=lambda: pressed("-"))
    MUL = Button(root, text="*", bg="black", fg="white", width=7, height=1, command=lambda: pressed("*"))
    DIV = Button(root, text="/", bg="black", fg="white", width=7, height=1, command=lambda: pressed("/"))
    EQUAL = Button(root, text="=", bg="black", fg="white", width=7, height=1, command=equalto)
    clr = Button(root, text="clear", bg="black", fg="white", width=7, height=1, command=clearscreen)

    button1.grid(row=4, column=0)
    button2.grid(row=4, column=1)
    button3.grid(row=4, column=2)
    button4.grid(row=6, column=0)
    button5.grid(row=6, column=1)
    button6.grid(row=6, column=2)
    button7.grid(row=8, column=0)
    button8.grid(row=8, column=1)
    button9.grid(row=8, column=2)
    button0.grid(row=10, column=0)
    ADD.grid(row=4, column=3)
    SUB.grid(row=6, column=3)
    MUL.grid(row=8, column=3)
    DIV.grid(row=10, column=3)
    EQUAL.grid(row=10, column=1)
    clr.grid(row=10, column=2)
    root.mainloop()





