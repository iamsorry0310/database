from tkinter import *

User="Daya"
pas="2550"


def main():
    Main=Tk()
    Main.mainloop()
def welcome():

    userin=user_entry.get()
    passin=pass_entry.get()
    if User == userin and pas==passin:
        cheak_label=Label(root,text="WELCOME.....")
        canvas.create_window(100,200,window=cheak_label)
    else:
        main()

    


def fails():
    cheak_label=Label(root,text="BSDK")
    canvas.create_window(100,200,window=cheak_label)

root=Tk()
root.geometry("500x250")
canvas=Canvas(root)
canvas.pack()
user_entry=Entry(root)
canvas.create_window(200,80,window=user_entry)
user_label=Label(root,text="User-Name : ")
canvas.create_window(100,80,window=user_label)

pass_entry=Entry(root)
canvas.create_window(200,100,window=pass_entry)
pass_label=Label(root,text="PassWord : ")
canvas.create_window(100,100,window=pass_label)

login=Button(root,text="Log-In..",command=welcome)
canvas.create_window(100,150,window=login)

root.mainloop()
