from tkinter import *
from tkinter import ttk
import requests

def pass_values(*args):
    try:
        access_token= str(access_token_value.get())
        print(access_token)
        if access_token== "":
            print("Please enter access token")
            return
    except:
        print("Please check the value entered in access token field!")
        return

    try:
        birthday= str(date_value.get())
        print(birthday)
        if birthday== "":
            print("Please enter your birthday")
            return
        date, month= birthday.split("/")
        if len(date)!= 2 or len(month)!= 2:
            print("Please check the value entered in birthday date field!")
            return
        print(date, month)
    except:
        print("Please check the value entered in birthday date field!")
        return

    like= like_value.get()
    print(like)

    comment= comment_value.get()
    print(comment)

    save= save_value.get()
    print(save)



root = Tk()
root.title("Sonny- Automatically responds to birthday wishes")

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

access_token_value = StringVar()
date_value = StringVar()

ttk.Label(mainframe, text="Enter the access token: ").grid(column=1, row=1, sticky=W)
access_token_entry = ttk.Entry(mainframe, width=30, textvariable=access_token_value)
access_token_entry.grid(column=2, row=1, sticky=(W))

ttk.Label(mainframe, text="Enter your birthday (DD/MM): ").grid(column=1, row=2, sticky=W)
date_entry = ttk.Entry(mainframe, width=15, textvariable=date_value)
date_entry.grid(column=2, row=2, sticky=(W))

like_value = IntVar()
comment_value = IntVar()
save_value = IntVar()

ttk.Label(mainframe, text="Like the birthday wish").grid(column=1, row=3, sticky=W)
like_check = ttk.Checkbutton(mainframe, text='', variable=like_value)
like_check.grid(column=2, row=3, sticky=(W))

ttk.Label(mainframe, text="Comment on the birthday wish").grid(column=1, row=4, sticky=W)
comment_check = ttk.Checkbutton(mainframe, text='', variable=comment_value)
comment_check.grid(column=2, row=4, sticky=(W))

ttk.Label(mainframe, text="Save the wishes to a text file").grid(column=1, row=5, sticky=W)
save_check = ttk.Checkbutton(mainframe, text='', variable=save_value)
save_check.grid(column=2, row=5, sticky=(W))

ttk.Button(mainframe, text="Start", command=pass_values).grid(column=2, row=6, sticky=E)

access_token_entry.focus()
root.bind('<Return>', pass_values)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)


root.mainloop()