from tkinter import *
import tkinter.messagebox
def save_data():
    try:
        fileD = open("deliveries.txt", "a")
        fileD.write("Depot:\n")
        fileD.write("%s\n" % depot.get())
        fileD.write("Description:\n")
        fileD.write("%s\n" % description.get())
        fileD.write("Address:\n")
        fileD.write("%s\n" % address.get("1.0", END))
        depot.delete(0, END)
        description.delete(0, END)
        address.delete("1.0", END)
    except Exception as ex:
        tkinter.messagebox.showerror("Error!", "Can't write to the file\n %s" % ex)
def read_depots(file):
 depots = []
 depots_f = open(file)
 for line in depots_f:
  depots.append(line.rstrip())
 return depots

