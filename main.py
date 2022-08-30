import calculator
import tkinter as tk

root = tk.Tk()
root.geometry('530x750')
root.title("Calculator")
root.resizable(False, False)

expr = tk.StringVar()
entry = tk.Entry(
                    root,
                    font = ('helvetica', 70),
                    textvariable=expr, 
                    justify = 'right',
                    width = 13
                )

entry.grid(
            columnspan = 4, 
            padx  = (3, 3),
            pady  = (3, 3),
            ipadx = 0,
            ipady = 30
            )

flag_invalid = False

## Functions ##
def write(n):
    global flag_invalid
    if flag_invalid:
        flag_invalid = False
        expr.set(str(n))
        return
    buf = entry.get()
    expr.set(buf + str(n))

def writeOp(sym):
    buf = entry.get()
    syms = buf.split()
    try:
        num = float(syms[-1])
    except:
        return

    expr.set(buf + ' ' + sym + ' ')

def equate():
    global flag_invalid
    
    result = 0
    try:
        result = calculator.calculate(entry.get())
    except:
        flag_invalid = True
        expr.set("Invalid Expression")
        return

    expr.set(str(result))

def clear():
    expr.set('')
########


button_height = 2
button_width  = 4
button_font   = ('helvetica', 40)
button_padx   = (2, 2)
button_pady   = (2, 2)


buttons_num = list()
buttons_ops = {}
buttons_equal = tk.Button(
                            root, 
                            text = "=", 
                            font = button_font,
                            command = lambda: equate(),
                            height = button_height,
                            width  = button_width
                         )
buttons_clear = tk.Button(
                            root, 
                            text = "C", 
                            font = button_font,
                            command = lambda: clear(),
                            height = button_height,
                            width  = button_width
                         )

buttons_point = tk.Button(
                            root, 
                            text = ".", 
                            font = button_font,
                            command = lambda: write('.'),
                            height = button_height,
                            width  = button_width
                         )

buttons_negative = tk.Button(
                            root, 
                            text = "+/-", 
                            font = button_font,
                            command = lambda: write('-'),
                            height = button_height,
                            width  = button_width
                         )


## Numbers ##

buttons_num.append(tk.Button(
                                root, 
                                text = "0", 
                                font = button_font,
                                command = lambda: write(0),
                                height = button_height,
                                width  = button_width
                            ))
buttons_num.append(tk.Button(
                                root, 
                                text = "1", 
                                font = button_font,
                                command = lambda: write(1),
                                height = button_height,
                                width  = button_width
                            ))
buttons_num.append(tk.Button(
                                root, 
                                text = "2", 
                                font = button_font,
                                command = lambda: write(2),
                                height = button_height,
                                width  = button_width
                            ))
buttons_num.append(tk.Button(
                                root, 
                                text = "3", 
                                font = button_font,
                                command = lambda: write(3),
                                height = button_height,
                                width  = button_width
                            ))
buttons_num.append(tk.Button(
                                root, 
                                text = "4", 
                                font = button_font,
                                command = lambda: write(4),
                                height = button_height,
                                width  = button_width
                            ))
buttons_num.append(tk.Button(
                                root, 
                                text = "5", 
                                font = button_font,
                                command = lambda: write(5),
                                height = button_height,
                                width  = button_width
                            ))
buttons_num.append(tk.Button(
                                root, 
                                text = "6", 
                                font = button_font,
                                command = lambda: write(6),
                                height = button_height,
                                width  = button_width
                            ))
buttons_num.append(tk.Button(
                                root, 
                                text = "7", 
                                font = button_font,
                                command = lambda: write(7),
                                height = button_height,
                                width  = button_width
                            ))
buttons_num.append(tk.Button(
                                root, 
                                text = "8", 
                                font = button_font,
                                command = lambda: write(8),
                                height = button_height,
                                width  = button_width
                            ))
buttons_num.append(tk.Button(
                                root, 
                                text = "9", 
                                font = button_font,
                                command = lambda: write(9),
                                height = button_height,
                                width  = button_width
                            ))

########



## Operations ##
buttons_ops['+'] = tk.Button(
                            root, 
                            text = "+", 
                            font = button_font,
                            command = lambda: writeOp('+'),
                            height = button_height,
                            width  = button_width
                         )
buttons_ops['-'] = tk.Button(
                            root, 
                            text = "-", 
                            font = button_font,
                            command = lambda: writeOp('-'),
                            height = button_height,
                            width  = button_width
                         )
buttons_ops['*'] = tk.Button(
                            root, 
                            text = "*", 
                            font = button_font,
                            command = lambda: writeOp('*'),
                            height = button_height,
                            width  = button_width
                         )
buttons_ops['÷'] = tk.Button(
                            root, 
                            text = "÷", 
                            font = button_font,
                            command = lambda: writeOp('/'),
                            height = button_height,
                            width  = button_width
                         )
buttons_ops['^'] = tk.Button(
                            root, 
                            text = "^", 
                            font = button_font,
                            command = lambda: writeOp('^'),
                            height = button_height,
                            width  = button_width
                         )
buttons_ops['%'] = tk.Button(
                            root, 
                            text = "%", 
                            font = button_font,
                            command = lambda: writeOp('%'),
                            height = button_height,
                            width  = button_width
                         )
########

## row 1 ##

buttons_clear.grid(row = 1, column = 0,
                    padx = button_padx, pady = button_pady)

buttons_ops['^'].grid(row = 1, column = 1,
                    padx = button_padx, pady = button_pady)
buttons_ops['%'].grid(row = 1, column = 2,
                    padx = button_padx, pady = button_pady)
buttons_ops['÷'].grid(row = 1, column = 3,
                    padx = button_padx, pady = button_pady)

## row 2 ##

buttons_num[7].grid(row = 2, column = 0,
                    padx = button_padx, pady = button_pady)
buttons_num[8].grid(row = 2, column = 1,
                    padx = button_padx, pady = button_pady)
buttons_num[9].grid(row = 2, column = 2,
                    padx = button_padx, pady = button_pady)

buttons_ops['*'].grid(row = 2, column = 3,
                    padx = button_padx, pady = button_pady)

## row 3 ##

buttons_num[4].grid(row = 3, column = 0,
                    padx = button_padx, pady = button_pady)
buttons_num[5].grid(row = 3, column = 1,
                    padx = button_padx, pady = button_pady)
buttons_num[6].grid(row = 3, column = 2,
                    padx = button_padx, pady = button_pady)

buttons_ops['-'].grid(row = 3, column = 3,
                    padx = button_padx, pady = button_pady)

## row 4 ##

buttons_num[1].grid(row = 4, column = 0,
                    padx = button_padx, pady = button_pady)
buttons_num[2].grid(row = 4, column = 1,
                    padx = button_padx, pady = button_pady)
buttons_num[3].grid(row = 4, column = 2,
                    padx = button_padx, pady = button_pady)

buttons_ops['+'].grid(row = 4, column = 3,
                    padx = button_padx, pady = button_pady)

## row 5 ##

buttons_negative.grid(row = 5, column = 0,
                    padx = button_padx, pady = button_pady)

buttons_num[0].grid(row = 5, column = 1,
                    padx = button_padx, pady = button_pady)

buttons_point.grid(row = 5, column = 2,
                    padx = button_padx, pady = button_pady)

buttons_equal.grid(row = 5, column = 3,
                    padx = button_padx, pady = button_pady)


root.mainloop()
