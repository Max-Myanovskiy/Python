# Add Users and Scores to DB
# Selenium WebDriver

from tkinter import *
import sqlite3

def add():
    name = entry.get()
    name = str(name)
    grade = entry2.get()
    grade = str(grade)
    cursor.execute("""INSERT INTO testscores (name, grade)
        VALUES (?, ?)""", (name, grade))
    db.commit()
    entry.delete(0, END)
    entry2.delete(0, END)
    entry.focus()

def clear():
    entry.delete(0, END)
    entry2.delete(0, END)
    entry.focus()

with sqlite3.connect("TestScores.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS testscores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    grade TEXT NOT NULL)""")

window = Tk()
window.title("TestScores")
window.geometry("400x200")

label = Label(text="Enter student's name: ")
label.place(x=20, y=20, width=120, height=25)

entry = Entry(text="")
entry.place(x=140, y=20, width=230, height=25)
entry["justify"] = "center"
entry.focus()

label2 = Label(text="Enter student's grade: ")
label2.place(x=20, y=50, width=120, height=25)

entry2 = Entry(text="")
entry2.place(x=140, y=50, width=230, height=25)
entry2["justify"] = "center"

btn = Button(text="Add", command=add)
btn.place(x=150, y=90, width=100, height=25)

btn2 = Button(text="Clear", command=clear)
btn2.place(x=260, y=90, width=100, height=25)

window.mainloop()
db.close()