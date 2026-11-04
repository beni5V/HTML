from tkinter import *

window = Tk()
window.title('My Profile Card')
window.geometry('450x600')

title = Label(window, text='My Profile Card',
              fg='white', bg='DarkBlue', width=40)
title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

name_label = Label(window, text='Name:')
name_label.grid(row=1, column=0, padx=10, pady=5)

name_entry = Entry(window, bg='lightyellow')
name_entry.grid(row=1, column=1, padx=10, pady=5)

age_label = Label(window, text='Age:')
age_label.grid(row=2, column=0, padx=10, pady=5)

age_entry = Entry(window, bg='lightyellow')
age_entry.grid(row=2, column=1, padx=10, pady=5)

address_label = Label(window, text='Address:')
address_label.grid(row=3, column=0, padx=10, pady=5)

address_entry = Entry(window, bg='lightyellow')
address_entry.grid(row=3, column=1, padx=10, pady=5)

phone_label = Label(window, text='Phone:')
phone_label.grid(row=4, column=0, padx=10, pady=5)

phone_entry = Entry(window, bg='lightyellow')
phone_entry.grid(row=4, column=1, padx=10, pady=5)

hobby_label = Label(window, text='Hobby:')
hobby_label.grid(row=5, column=0, padx=10, pady=5)

hobby_entry = Entry(window, bg='lightyellow')
hobby_entry.grid(row=5, column=1, padx=10, pady=5)

about_frame = Frame(window, relief=RAISED, borderwidth=3)
about_frame.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

about_label = Label(about_frame, text='About Me:')
about_label.pack()

about_text = Text(about_frame, bg='lightyellow',
                  fg='green', width=40, height=4)
about_text.pack()
window.mainloop()