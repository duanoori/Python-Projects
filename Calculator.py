from tkinter import *

# Function to handle button clicks
def button_click(event):
    # Get the current text in the display
    current = display.get()

    # Get the button text
    button = event.widget
    text = button['text']
    if text == '=':
        try:
            # Evaluate the expression and update the display
            result = eval(current)
            display.delete(0, END)
            display.insert(END, str(result))
        except:
            # If there's an error in the expression, clear the display
            display.delete(0, END)
            display.insert(END, "Error")
    else:
        # Append the button's text to the current display text
        display.insert(END, text)
    
def clear_display():
    display.delete(0, END) 


# ----- Create the main window ----- #
root = Tk()
root.title("Calculator")
root.geometry("400x500")
root.resizable(False, False)  # Prevent resizing the window


# ----- Create the display and buttons ----- #
# Create the display entry widget
display = Entry(root, width=18, font=("Arial", 20) , borderwidth=2, relief="sunken")
display.grid(row=0, column=0, columnspan=4, ipadx= 46, ipady= 25, pady= 30, padx= 10)

# Define button labels
button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]
row, col= 1,0
buttons = []
for label in button_labels:
    button = Button(root, text=label, width=5, height=2, font=("Arial", 18), borderwidth=1, relief="raised")
    button.grid(row=row, column=col)
    buttons.append(button)
    col += 1
    if col > 3:
        col = 0
        row += 1

for button in buttons:
    button.bind("<Button-1>", button_click)

# Create a clear button
clear_button = Button(root, text='Clear', width=10, height=1, font=("Arial", 18), command=clear_display)
clear_button.grid(row=6, column=0, columnspan=4, padx=5, pady=10)


root.mainloop()
