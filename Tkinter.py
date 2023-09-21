from tkinter import *

def clicked():
    num = selection.get()
    artref = num + ".png"
    photo = PhotoImage(file = artref)
    photobox.image = photo
    photobox["image"] = photo
    photobox.update()

window = Tk()
window.title("Art")
window.geometry("600x550")

art = PhotoImage(file = "1.png")
photobox = Label(window, image = art)
photobox.image = art
photobox.place(x = 100, y = 20, width = 400, height = 250)

label = Label(text = "Select Art Number: ")
label.place(x = 50, y = 300, width = 100, height = 25)

selection = Entry(text = "")
selection.place(x = 200, y = 300, width = 100, height = 25)
selection.focus()

button = Button(text = "See Art", command = clicked)
button.place(x = 150, y = 350, width = 100, height = 25)

window.mainloop()
