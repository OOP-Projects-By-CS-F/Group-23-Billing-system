import os
from tkinter import *

home=Tk()
home.geometry("1366x768")
home.resizable(1,1)
home.title("Welcome Window")
def main():
    home.withdraw()
    os.system("main.py")
    home.deiconify()

labelA=Label(home)
labelA.place(relx=0, rely=0, width=1366, height=768)
imgA = PhotoImage(file="./images/home.png")
labelA.configure(image=imgA)

buttonA = Button(home)
buttonA.place(relx=0.440, rely=0.350, width=170, height=120)
buttonA.configure(relief="flat")
buttonA.configure(overrelief="flat")
buttonA.configure(activebackground="#ffffff")
buttonA.configure(cursor="hand2")
buttonA.configure(foreground="#ffffff")
buttonA.configure(background="#ffffff")
buttonA.configure(borderwidth="0")
img2 = PhotoImage(file="./images/a.png")
buttonA.configure(image=img2)
buttonA.configure(command=main)
   

home.mainloop()
