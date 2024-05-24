from tkinter import Tk, Label, Entry, Button

def get_number():
  """
  This function retrieves the user input from the entry field and prints it.
  """
  number = entry.get()
  return number
  # You can add further logic here to process the number (e.g., convert to integer)

# Create the main window
window = Tk()
window.title("First Time ?")

# Create a label
label = Label(window, text="First Time ?\nEnter 1 | 0")
label.pack()

# Create an entry field for user input
entry = Entry(window)
entry.pack()

# Create a button to trigger the get_number function
button = Button(window, text="Submit", command=get_number)
button.pack()

# Start the event loop to display the window
window.mainloop()