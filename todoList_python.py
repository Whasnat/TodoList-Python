from tkinter import *


# INCREMENT COUNT BY 1 AND INSERT ENTRIES TO LIST
def add_items():
    global COUNT
    COUNT += 1
    listbox.insert(END,str(COUNT) + ". " + taskName.get() + " " + taskDescription.get())
    taskName.delete("0", END)
    taskDescription.delete("0", END)
    taskName.focus()


# CREATE MAIN WINDOW
window = Tk()
window.title("Todo List")
window.geometry("800x600")
COUNT = 0

# DEFINE FRAMES
entryFrame = Frame(window)
entryFrame.pack()
listFrame = Frame(window)
listFrame.pack()

# CREATE A LISTBOX TO SHOW THE ITEMS
listbox = Listbox(listFrame)
listbox.pack()

# CREATE ENTRIES
name = StringVar()
taskName = Entry(entryFrame, textvariable=name)
taskName.pack()

description = StringVar()
taskDescription = Entry(entryFrame, textvariable=description)
taskDescription.pack()


# CREATE "ADD ITEM" BUTTON
button = Button(entryFrame, command=add_items, text="Add Item")         # CALL "add_items" WHEN BUTTON CLICKED
button.pack()

window.mainloop()




