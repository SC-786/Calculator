from tkinter import *
from tkmacosx import Button


def get_input(entry, keyword):
    entry.insert(END, keyword)

def clear(entry):
    entry.delete(0, END)


def backspace(entry):
    entry.delete(0, 1)


def calc(entry):
    input_info = entry.get()
    try:
        output = str(eval(input_info))
    except ZeroDivisionError:
        output = ''
        popupmsg()
    clear(entry)
    entry.insert(END, output)


def popupmsg():
    popup = Tk()
    popup.title("Error")
    popup.resizable(0, 0)
    popup.geometry("140x100")
    label = Label(popup, text='Cannot divide by 0,\n UNDEFINED!')
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", bg="#DDDDDD", command=popup.destroy)
    B1.pack()


win = Tk()
win.title("Calculator")


input = Entry(win, justify='right')
input.grid(column=0, row=0, columnspan=4)

button_sq = Button(text='^', command=lambda: get_input(input, '**'), width=45)
button_sq.grid(column=2, row=7, pady=5)
button_dot = Button(text='.', command=lambda: get_input(input, '.'), width=45)
button_dot.grid(column=1, row=7, pady=5)
button_clear = Button(text='C', command=lambda: clear(input), width=45)
button_clear.grid(column=2, row=3, pady=5)
button0 = Button(text='0', command=lambda: get_input(input, '0'), width=45)
button0.grid(column=0, row=7, pady=5)
button_bckspc = Button(text='<-', command=lambda: backspace(input), width=100)
button_bckspc.grid(column=0, row=3, columnspan=2)
button_div = Button(text='/', command=lambda: get_input(input, '/'), width=45)
button_div.grid(column=3, row=3, pady=5)
button_mult = Button(text='*', command=lambda: get_input(input, '*'), width=45)
button_mult.grid(column=3, row=4, pady=5)
button_sub = Button(text='-', command=lambda: get_input(input, '-'), width=45)
button_sub.grid(column=3, row=5, pady=5)
button_add = Button(text='+', command=lambda: get_input(input, '+'), width=45)
button_add.grid(column=3, row=6, pady=5)
button_eq = Button(text='=', command=lambda: calc(input), width=45)
button_eq.grid(column=3, row=7, pady=5)
button1 = Button(text='1', command=lambda: get_input(input, '1'), width=45)
button1.grid(column=0, row=6, pady=5)
button2 = Button(text='2', command=lambda: get_input(input, '2'), width=45)
button2.grid(column=1, row=6, pady=5)
button3 = Button(text='3', command=lambda: get_input(input, '3'), width=45)
button3.grid(column=2, row=6, pady=5)
button4 = Button(text='4', command=lambda: get_input(input, '4'), width=45)
button4.grid(column=0, row=5, pady=5)
button5 = Button(text='5', command=lambda: get_input(input, '5'), width=45)
button5.grid(column=1, row=5, pady=5)
button6 = Button(text='6', command=lambda: get_input(input, '6'), width=45)
button6.grid(column=2, row=5, pady=5)
button7 = Button(text='7', command=lambda: get_input(input, '7'), width=45)
button7.grid(column=0, row=4, pady=5)
button8 = Button(text='8', command=lambda: get_input(input, '8'), width=45)
button8.grid(column=1, row=4, pady=5)
button9 = Button(text='9', command=lambda: get_input(input, '9'), width=45)
button9.grid(column=2, row=4, pady=5)

win.mainloop()
