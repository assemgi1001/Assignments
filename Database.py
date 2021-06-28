from tkinter import *
from PIL import ImageTk, Image
import sqlite3

app = Tk()
app.title('Quarter Register')
app.geometry("400x400")

# Creating a Database to connect with

connect = sqlite3.connect('student1.db')

c = connect.cursor()


#Table

#c.execute(""" CREATE TABLE registration (
 #first_name text,
 #last_name text,
 #student_id integer,
 #course_name text,
 #phone_number integer,
 #address text)
  #""")


def update():
    connect = sqlite3.connect('student1.db')
    c = connect.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE registration SET
    first_name = :first,
    last_name = :last,
    id_num = :id_num,
    course = :course,
    phone = :phone,
    address = :address

    WHERE oid = :oid""",
              {
                  'first': f_name_editor.get(),
                  'last': last_name_editor.get(),
                  'id_num': id_num_editor.get(),
                  'course': course_editor.get(),
                  'phone': phone_editor.get(),
                  'address': address_editor.get(),
                  'oid': record_id
              })

    connect.commit()
    connect.close()
    editor.destroy()


def edit():
    global editor

    editor = Tk()
    editor.title('Quarter Register')
    editor.geometry("400x400")
    connect = sqlite3.connect('student1.db')
    c = connect.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * From registration WHERE oid= " + record_id)
    records = c.fetchall()

    # Creating Global variables in order to use them outside the function
    global f_name_editor
    global l_name_editor
    global id_num_editor
    global course_editor
    global phone_editor
    global address_editor
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20)
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    id_num_editor = Entry(editor, width=30)
    id_num_editor.grid(row=2, column=1)
    course_editor = Entry(editor, width=30)
    course_editor.grid(row=3, column=1)
    phone_editor = Entry(editor, width=30)
    phone_editor.grid(row=4, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=5, column=1)

    f_name_label_editor = Label(editor, text="First Name")
    f_name_label_editor.grid(row=0, column=0)
    l_name_label_editor = Label(editor, text="Last Name")
    l_name_label_editor.grid(row=1, column=0)
    id_num_label_editor = Label(editor, text="Student ID Number")
    id_num_label_editor.grid(row=2, column=0)
    course_label_editor = Label(editor, text="Course")
    course_label_editor.grid(row=3, column=0)
    phone_label_editor = Label(editor, text="Phone Number")
    phone_label_editor.grid(row=4, column=0)
    address_label_editor = Label(editor, text="Address")
    address_label_editor.grid(row=5, column=0)
    # Creating a Save button after Editing
    edit_button = Button(editor, text="Save Records", command=edit)
    edit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
    # loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        id_num_editor.insert(0, record[2])
        course_editor.insert(0, record[3])
        phone_editor.insert(0, record[4])
        address_editor.insert(0, record[5])


def delete():
    connect = sqlite3.connect('student1.db')
    c = connect.cursor()
    c.execute("DELETE from registration WHERE oid= " + delete_box.get())

    connect.commit()
    connect.close()


def submit():
    connect = sqlite3.connect('student1.db')
    c = connect.cursor()

    c.execute("INSERT INTO registration VALUES (:f_name, :l_name, :id_num, :course, :phone, :address)",

              {'f_name': f_name.get(),
               'l_name': l_name.get(),
               'id_num': id_num.get(),
               'course': course.get(),
               'phone': phone.get(),
               'address': address.get()
               })
    connect.commit()
    connect.close()
    # Clear the boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    id_num.delete(0, END)
    course.delete(0, END)
    phone.delete(0, END)
    address.delete(0, END)


def query():
    connect = sqlite3.connect('student1.db')
    c = connect.cursor()

    c.execute("SELECT *, oid From registration")
    records = c.fetchall()
    print(records)
    # Loop through results

    print_records = ''
    for record in records:
        print_records += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[6]) + "\n"

    query_label = Label(app, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    connect.commit()
    connect.close()


# Text Boxes
f_name = Entry(app, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(app, width=30)
l_name.grid(row=1, column=1)
id_num = Entry(app, width=30)
id_num.grid(row=2, column=1)
course = Entry(app, width=30)
course.grid(row=3, column=1)
phone = Entry(app, width=30)
phone.grid(row=4, column=1)
address = Entry(app, width=30)
address.grid(row=5, column=1)
delete_box = Entry(app, width=30)
delete_box.grid(row=9, column=1)

# Create text box Labels
f_name_label = Label(app, text="First Name")
f_name_label.grid(row=0, column=0)
l_name_label = Label(app, text="Last Name")
l_name_label.grid(row=1, column=0)
id_num_label = Label(app, text="Student ID Number")
id_num_label.grid(row=2, column=0)
course_label = Label(app, text="Course")
course_label.grid(row=3, column=0)
phone_label = Label(app, text="Phone Number")
phone_label.grid(row=4, column=0)
address_label = Label(app, text="Address")
address_label.grid(row=5, column=0)
delete_box_label = Label(app, text="Select ID")
delete_box_label.grid(row=9, column=0)

submit_button = Button(app, text="Add a Record", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

query_button = Button(app, text="Show Records", command=query)
query_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

delete_button = Button(app, text="Delete Records", command=delete)
delete_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

edit_button = Button(app, text="Edit Records", command=update)
edit_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

connect.commit()
connect.close()

app.mainloop()