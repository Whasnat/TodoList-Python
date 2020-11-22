from tkinter import *


# INCREMENT COUNT BY 1 AND INSERT ENTRIES TO LIST
def add_items():
    global COUNT
    COUNT += 1

    listbox.insert(END, str(COUNT) + ". " + taskName.get() + ":   " + taskDescription.get())
    taskName.delete("0", END)
    taskDescription.delete("0", END)
    taskName.focus()


def delete_items():
    global COUNT
    COUNT -= 1
    listbox.delete(ANCHOR)


# CREATE MAIN WINDOW
window = Tk()
window.title("Todo List")
window.geometry("800x600")
COUNT = 0

# DEFINE FRAMES
entryFrame = Frame(window)
entryFrame.pack(side="left",)
listFrame = Frame(window)
listFrame.pack(side="left", fill=BOTH)

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
button_add_items = Button(entryFrame, command=add_items, text="Add Item")         # CALL "add_items" WHEN BUTTON CLICKED
button_add_items.pack()

button_delete_items = Button(entryFrame, command=delete_items, text="Delete")
button_delete_items.pack()

window.mainloop()
