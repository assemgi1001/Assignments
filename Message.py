import tkinter
from tkinter import *
import pandas as pd
A = pd.read_excel('Midterm.xlsx')

app = Tk()
app.geometry("500x350")
app.title("Top Universities")

Label(app, text="Chose the University:").pack()
Choose = StringVar()
Choose.set(None)
options = pd.read_excel('Midterm.xlsx')
OptionMenu(app, Choose, *options).pack()




app.mainloop()