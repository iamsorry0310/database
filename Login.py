from tkinter import *
from DataBase import showData,insertData
from Sign import Sign_in
    
def LoginSuccess():
    pass

# Login Button Command ---------------
def sign():
    sgn=Sign_in()
    sgn.start()


def CheakUserData(userinput,passinput):
    username = user_entry.get()
    password = pass_entry.get()
    

root=Tk()
root.title("Login Page")
root.geometry("500x250")
# Main  -------------------------------
canvas=Canvas(root,background="whitesmoke")
canvas.pack()
# User Entery -------------------
user_entry=Entry(root)
canvas.create_window(200,60,window=user_entry)
# User Label -------------------
user_label=Label(root,text="User-Name : ",background="whitesmoke")
canvas.create_window(100,60,window=user_label)

# Password Entry -------------------
pass_entry=Entry(root)
canvas.create_window(200,100,window=pass_entry)
# Password Label -------------------
pass_label=Label(root,text="PassWord : ",background="whitesmoke")
canvas.create_window(100,100,window=pass_label)

# Log in Button ----------------------
login=Button(root,text="Log-In..",command=LoginSuccess)
canvas.create_window(200,150,window=login)



sign=Button(root,text="Sign-In..",command=sign)
canvas.create_window(200,200,window=sign)

root.mainloop()

n=Sign_in()
print(n.user)
print(n.pas)