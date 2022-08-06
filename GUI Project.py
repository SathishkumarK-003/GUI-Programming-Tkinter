from tkinter import *
root=Tk()
T=Text(root,height=30,width=50)
T.pack()
root.title('Hello mouse world')

def my_call():
    T.insert(INSERT,"Hello\n")
           
def my_callback():
    T.insert(INSERT,"\tGoodbye\n")

button1=Button(root,text="Hello",command=my_call)
button1.pack()
button2=Button(root,text="Goodbye",command=my_callback)
button2.pack()
root.mainloop()

