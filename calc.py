from tkinter import*
from tkinter import ttk
from tkinter import font

window = Tk()
window.title("Calculator")
window.columnconfigure(0, weight=1, minsize=75)
window.rowconfigure(0, weight=1, minsize=50)

lrg_font = font.Font(family="Helvetica", size=22, weight="bold")

calcu = "Calculate: "
calc_lbl = Label(master=window, text=calcu, font=lrg_font)
calc_lbl.pack(expand=True, fill=X)
get_calc = Entry(master=window, font=lrg_font, justify='right', name="get_calc", width=14)
get_calc.pack(expand=True, fill=X)
get_calc.focus_set()


frm = Frame(master=window, relief=FLAT, borderwidth=3, width=250, height=250)
frm.pack(fill=BOTH, expand=True)

def handle_keypress(x):
    return lambda: get_calc.insert(END, x)

def clear():
    get_calc.delete(0, 'end')
    return get_calc

def char_clear():
    txt = get_calc.get()[:-1]
    get_calc.delete(0, END)
    return get_calc.insert(0, txt)


count = 0
def brackets():
    global count
    count += 1
    if count % 2 == 0:
        get_calc.insert(END, ")")
    else:
        get_calc.insert(END, "(")

def ans():
    ans = eval(get_calc.get())
    get_calc.delete(0, 'end')
    get_calc.insert('end', ans)
    return get_calc

# get_calc.bind("<Return>", ans())


buttonRows = [['','','%','/'],['7','8','9','*'],
              ['4','5','6','-'],['1','2','3','+'], ['0','( )','.','']]

for row_index, row in enumerate(buttonRows):
    Grid.rowconfigure(frm, row_index)
    for cell_index, cell in enumerate(row):
        Grid.columnconfigure(frm, cell_index)
        if cell_index == 0 and row_index == 0:
            ac = Button(master=frm, text="AC", command=clear, width=6, height=3)
            ac.grid(row=0, column=0, sticky="nsew")
        elif cell_index == 1 and row_index == 0:
            delete = Button(master=frm, text="DEL", command=char_clear, bg="blue")
            delete.grid(row=0, column=1, sticky="nsew")
        elif cell_index == 1 and row_index == 4:
            brackets = Button(master=frm, command=brackets, text=cell, width=6, height=3)
            brackets.grid(row=4, column=1, sticky="nsew")
        elif cell_index == 3 and row_index == 4:
            equals = Button(master=frm, text="=", command=ans, width=6, height=3)
            equals.grid(row=4, column=3, sticky="nsew")
        # elif cell_index == 2 and row_index == 4:
        #     brackets = Button(master=frm, text=cell, command=handle_keypress(cell), width=1)
        #     brackets.grid(row=4, column=2, sticky = W)
        else:
            btns = CustomButton(master=frm, bg='#54FA9B', text=cell, command=handle_keypress(cell), width=6, height=3)
            btns.grid(row=row_index, column=cell_index, sticky="nsew")
window.mainloop()
