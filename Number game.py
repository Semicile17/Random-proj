from tkinter import *
import random
from PIL import ImageTk,Image
root=Tk()
root.title("The Number Game")
root.configure(bg="white")
def Play():
        
        but1.destroy()
       
        def check():
              
                s=e.get()
                if(random.randint(0,2)==int(s)):
                        def Playagain():
                                e.delete(0,END)
                                label3.destroy()
                                but4.destroy()
                                but3.destroy()
                        def Exit():
                                root.destroy()
                        label3=Label(root,text="You guessed the right number !")
                        label3.grid(row=4,column=0)
                        but3=Button(root,text="Play again",command=Playagain,borderwidth=1)
                        but3.grid(row=5,column=0)
                        but4=Button(root,text="Exit",command=Exit,borderwidth=1)
                        but4.grid(row=6,column=0)
                        
                else :
                        def Exit():
                                root.destroy()
                        def Tryagain():
                                e.delete(0,END)
                                label4.destroy()
                                but5.destroy()
                        label4=Label(root,text="Sorry , it's the wrong number !")
                        label4.grid(row=4,column=0)
                        but5=Button(root,text="Try again",command=Tryagain,borderwidth=1)
                        but5.grid(row=5,column=0)
                        but6=Button(root,text="Exit",command=Exit,borderwidth=1)
                        but6.grid(row=6,column=0)
                        
        label2=Label(root,text="Enter your number  ")
        label2.grid(row=2,column=0)
        e=Entry(root,width=30,borderwidth=1,bg="white")
        e.grid(row=3,column=0)
        but2=Button(root,text="Check",command=check,borderwidth=1)
        but2.grid(row=3,column=1)
        
label1=Label(root,text="Welcome to the Number Game")
label1.grid(row=0,column=0)
but1=Button(root,text="PLAY",command=Play,borderwidth=1)
but1.grid(row=1,column=0)


root.mainloop()
