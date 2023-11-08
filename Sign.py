from tkinter import *
from DataBase import showData,insertData


# Sign-in Button Command ---------------
     
def SignIn():
    user=user_entry.get()
    pas=pass_entry.get()   
    insertData(user,pas)
    print(showData())

root1=Tk()
root1.title("Sign-In Page")
root1.geometry("500x250")
        # Main  -------------------------------
canvas=Canvas(root1,background="whitesmoke")
canvas.pack()
        # User Entery -------------------
user_entry=Entry(root1)
canvas.create_window(200,60,window=user_entry)
        # User Label -------------------
user_label=Label(root1,text="User-Name : ",background="whitesmoke")
canvas.create_window(100,60,window=user_label)

        # Password Entry -------------------
pass_entry=Entry(root1)
canvas.create_window(200,100,window=pass_entry)
        # Password Label -------------------
pass_label=Label(root1,text="PassWord : ",background="whitesmoke")
canvas.create_window(100,100,window=pass_label)

        # Log in Button ----------------------
login=Button(root1,text="Sign-In..",command=SignIn)
canvas.create_window(200,150,window=login)

root1.mainloop()

