
from tkinter import Tk, Label, Button, StringVar, Entry
class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.expression = StringVar()

        
        self.entry = Entry(master, textvariable=self.expression, bd=20, insertwidth=1, width=15, font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4)

        
        self.create_buttons()
        
    def create_buttons(self):
        # Button labels
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        # Create buttons and add them to the grid
        for (text, row, col) in buttons:
            button = Button(self.master, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

    def on_button_click(self, text):
        if text == '=':
            # Evaluate the expression and update the entry widget
            try:
                result = eval(self.expression.get())
                self.expression.set(result)
            except Exception as e:
                self.expression.set('Error')
        elif text == 'C':
            # Clear the entry widget
            self.expression.set('')
        else:
            # Append the clicked button's text to the expression
            current_expression = self.expression.get()
            self.expression.set(current_expression + text)
            
if __name__ == "__main__":
    root = Tk()
    calculator = Calculator(root)
    root.mainloop()
