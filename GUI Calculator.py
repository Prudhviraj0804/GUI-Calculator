import tkinter as tk

# Function to update the input field
def button_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Function to clear the input field
def button_clear():
    global expression
    expression = ""
    input_text.set("")

# Function to evaluate the expression
def button_equal():
    global expression
    try:
        result = str(eval(expression))  # Evaluate the expression
        input_text.set(result)
        expression = result
    except Exception as e:
        input_text.set("Error")
        expression = ""

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(0, 0)

# StringVar to hold the input expression
expression = ""
input_text = tk.StringVar()

# Input frame
input_frame = tk.Frame(root, width=300, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=tk.TOP)

# Input field inside the frame
input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)  # Internal padding to increase the height

# Button frame
buttons_frame = tk.Frame(root, width=300, height=350, bg="grey")
buttons_frame.pack()

# First row of buttons
clear = tk.Button(buttons_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_clear())
clear.grid(row=0, column=0, columnspan=3)
divide = tk.Button(buttons_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click("/"))
divide.grid(row=0, column=3)

# Second row of buttons
seven = tk.Button(buttons_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(7))
seven.grid(row=1, column=0)
eight = tk.Button(buttons_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(8))
eight.grid(row=1, column=1)
nine = tk.Button(buttons_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(9))
nine.grid(row=1, column=2)
multiply = tk.Button(buttons_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click("*"))
multiply.grid(row=1, column=3)

# Third row of buttons
four = tk.Button(buttons_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(4))
four.grid(row=2, column=0)
five = tk.Button(buttons_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(5))
five.grid(row=2, column=1)
six = tk.Button(buttons_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(6))
six.grid(row=2, column=2)
subtract = tk.Button(buttons_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click("-"))
subtract.grid(row=2, column=3)

# Fourth row of buttons
one = tk.Button(buttons_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(1))
one.grid(row=3, column=0)
two = tk.Button(buttons_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(2))
two.grid(row=3, column=1)
three = tk.Button(buttons_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(3))
three.grid(row=3, column=2)
add = tk.Button(buttons_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click("+"))
add.grid(row=3, column=3)

# Fifth row of buttons
zero = tk.Button(buttons_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(0))
zero.grid(row=4, column=0, columnspan=2)
point = tk.Button(buttons_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click("."))
point.grid(row=4, column=2)
equals = tk.Button(buttons_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_equal())
equals.grid(row=4, column=3)

# Run the application
root.mainloop()