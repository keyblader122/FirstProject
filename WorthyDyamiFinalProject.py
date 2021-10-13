'''
    File name: WorthyDyamiFinalProject.py
    Author: Dyami Worthy
    Date created: 9/7/2021
    Date last modified: 10/12/2021
    Python Version: 3.9
'''



import tkinter
import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox
from PIL import Image, ImageTk
from random import randint

#=============================================================================
#Main Window/Launcher of game
#
#This part sets up the program to open in a launcher with it's own button.
#Each button is tied to a new window
#=============================================================================
root= Tk()
root.geometry('800x800')

#Image 1 for Main Window
bg = PhotoImage( file = "galaxy-transparent1.png")
label1 = Label( root, image = bg)
label1.place(x = 0,y = 0)

root.wm_title("HANGMAN LAUNCHER!!!")


#Exit button for Program
def exit1():
    exit()
    

#============================================================================
#Options Button/ Add info
#
#The User will enter info about themselves which will be put on the console
#============================================================================    
def optiongame():
    root1 = tkinter.Toplevel()
    root1.geometry('300x600')

    #Image 2 for Options Window
    bg = PhotoImage( file = "Homer-Settings.png")
    label2 = Label( root1, image = bg)
    label2.place(x = 0,y = 0)

    #Settings menu Window title
    root1.wm_title("Settings Menu")
    
    name_var = tk.StringVar(root1)
    age_var = tk.StringVar(root1)

    #Settings Label
    l = Label(root1, text='Settings Menu:' , fg='white', bg='black', font=("arial", 17)).pack()

    #Input Name/ Label
    name_label = Label(root1, text='Enter your name:', fg='black', bg='red', font=('arial', 12, 'bold'))
    name_label.place(x=10, y=90)

    
     
        
    
    entry1 = Entry(root1, textvariable=name_var, width=30)
    entry1.place(x=150, y=90)
    
    #Input Age/ Label
    age_label = Label(root1, text='Enter your age:', fg='black', bg='red', font=('arial', 12, 'bold'))
    age_label.place(x=10, y=140)
    
    entry2 = Entry(root1, textvar=age_var, width=30)
    entry2.place(x=150, y=140)
    name_var.set("Name here!...Erase Me!!!")
    age_var.set("Age Here!...Erase Me!!!")

    #Submit input info button/ back button
    def submit():
        tkinter.messagebox.showinfo("Game notification:", 'Information succesful saved!')
        
        name= name_var.get()
        age= age_var.get()
     
        print("Your name is : " + name_var.get())
        print("Your age is : " + age)
    
    def close_window():
        root1.destroy()

    
    submit = Button(root1, text='SUBMIT', fg='white', bg='blue', font=('arial', 17, 'bold'), command= submit)
    submit.place(x=100, y=300)
    backk = Button(root1, text='BACK', fg='white', bg='green', font=('arial', 14, 'bold'), command=close_window).place(x=100,y=350)

    
        
    root1.mainloop()


#===========================================================
# Hangman Code
#
# This section of code houses the main game of Hangman!
#
#===========================================================    
def game():
    
    #Initializing Empty List 
    mywords=[]
    file1 = open(r"commonword.txt","r")

    #Appending words from file to the list
    for x in file1:
        mywords.append(x.replace('\n', ''))

        word=random.choice(mywords)
        random_word=list(word)
        p=[]
        s='_ '*len(random_word)
        p=s.split(' ')
        p.pop(len(random_word))
        actual=random_word.copy()

    #Hangman class
    class Hangman:
        
        
        
        def __init__(self,master):
            self.count=0
            self.structure(master)
            self.rr=master
        
        def structure(self,master):
 
            """ Instruction Label """
 
        # Create instruction label for Program
            self.inst_lbl = Label(master, text = "Welcome to Hangman Game!")
            self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)

            """ Guess Input """ 
 
        # Create label for entering Guess  
            self.guess_lbl = Label(master, text = "Enter your Guess:")
            self.guess_lbl.grid(row = 1, column = 0, sticky = W)
 
        # Create entry widget to accept Guess  
            self.guess_ent = Entry(master)
            self.guess_ent.grid(row = 1, column = 1, sticky = W)

        
        # Create a space  
            self.gap2_lbl = Label(master, text = " ")
            self.gap2_lbl.grid(row = 2, column = 0, sticky = W)

        # Creating a submit button
            self.submit_bttn = Button(master, text = "Submit",command=self.submit,height=1, width=20)
            self.submit_bttn.grid(row = 3, column =1, sticky = W)
 
            master.bind('<Return>',self.submit)   
        
        # Create a space  
            self.gap2_lbl = Label(master, text = " ")
            self.gap2_lbl.grid(row = 4, column = 0, sticky = W)
 
            """ RESET """
         
        # Creating a Clear button
            self.clear_bttn = Button(master, text = "Clear Input",command=self.clear,height=2, width=20)
            self.clear_bttn.grid(row = 9, column = 2, sticky = W)
 
        # Create a space  
            self.gap2_lbl = Label(master, text = " ")
            self.gap2_lbl.grid(row = 5, column = 0, sticky = W)
        
            self.inst_lb2 = Label(master, text ='Life:10')
            self.inst_lb2.grid(row = 1, column = 2, columnspan = 2, sticky = W)

        #Creating a Label to Display Message
            self.inst_lb3 = Label(master, text ='')
            self.inst_lb3.grid(row = 6, column = 0, columnspan = 2, sticky = W)

        #Creating a label to display current Guessed Status of Word
            self.curr_char1 = Label(master, text =p)
            self.curr_char1.place(x=100,y=130)
            self.curr_char = Label(master, text ="Current Status:")
            self.curr_char.place(x=0,y=130)

        # Create a Hangman's Background
        
            self.c=Canvas(master,height=300,width=200)
            self.c.grid(row=9,column=0,sticky =W)
            self.l=self.c.create_line(70,20,70,250,width=2)
            self.l1=self.c.create_line(70,20,150,20,width=2)
            self.l2=self.c.create_line(150,20,150,50,width=2)
    
        
        def current_status(self,char):
            self.curr_char1 = Label(self.rr, text =char)
            self.curr_char1.place(x=100,y=130)

        def clear(self):
            self.guess_ent.delete(0, 'end')
        
    
    

        

        def submit(self,*args):

        #Taking Entry From Entry Field
            char=self.guess_ent.get()

        #Checking whether Entry Field is empty or not
            if(len(char)==0):
                messagebox.showwarning("Warning","Entry field is Empty")
            if(len(char)>1):
                messagebox.showwarning("Warning","Enter character of length 1")   

            if char in actual and len(char)==1:
                l=actual.count(char)
                for j in range(l):
                    i=actual.index(char)
                
                    p.insert(i,char)
                    p.pop(i+1)
                    actual.insert(i,'_')
                    actual.pop(i+1)
                self.inst_lb2.config(text='Life:'+ str(10-self.count))
                self.inst_lb3.config(text='Right Guessed!')
                self.guess_ent.delete(0, 'end')
                self.current_status(p)

            elif(len(char)==1):
                self.count=self.count+1
                self.inst_lb2.config(text='Life:'+str(10-self.count))
                self.inst_lb3.config(text='Wrong Guessed!')
                self.guess_ent.delete(0, 'end')
            
        #Creating Hangman's parts orderwise if wrong character is Guessed
            if(self.count==1):
                self.cir=self.c.create_oval(125,100,175,50,width=2)
            elif(self.count==2):
                self.el=self.c.create_line(135,65,145,65,width=2)
            elif(self.count==3):
                self.er=self.c.create_line(155,65,165,65,width=2)
            elif(self.count==4):
                self.no=self.c.create_line(150,70,150,85,width=2)
            elif(self.count==5):
                self.mo=self.c.create_line(140,90,160,90,width=2)
            elif(self.count==6):
                self.l3=self.c.create_line(150,100,150,200,width=2)
            elif(self.count==7):
                self.hl=self.c.create_line(150,125,100,150,width=2)
            elif(self.count==8):
                self.hr=self.c.create_line(150,125,200,150,width=2)
            elif(self.count==9):
                self.fl=self.c.create_line(150,200,100,225,width=2)
            elif(self.count==10):
                self.fr=self.c.create_line(150,200,200,225,width=2)


        #Condition of Player Won
            if( p==random_word):
                self.inst_lb3.config(text='You perfectly guessed the word!')
                messagebox.showinfo("Hello", "You Won")
                self.rr.destroy()

        #Condition Of player Loose
            elif(self.count>=10):
                self.inst_lb3.config(text='You lost.... the word is '+word)
                messagebox.showinfo("Hello", "You lost please try again!")
                self.rr.destroy()



     
            

        

    root2 = Tk()
    root2.title("Hangman Game")
    root2.geometry("580x480")
    app = Hangman(root2)
    print("The word is: ", word)

    #Exit Button for Hangman
    def close_window():
        root2.destroy()
    quit2 = Button(root2, text = 'EXIT', bg = 'red', fg ='white', font=('arial', 12, 'bold'), command = close_window)
    quit2.place(x= 250, y= 223)
        
    root2.mainloop()


    
#======================================================================    
#About Window    
#======================================================================    
def about1():
    aboutWindow = tkinter.Toplevel()
    aboutWindow.geometry('600x600')
    
    def close_window():
        aboutWindow.destroy()
        
    #Image 3 for About Window
    bg = PhotoImage( file = "earth.png")
    label4 = Label(aboutWindow, image=bg)
    label4.place(x = 0,y = 0,relwidth=1,relheight=1)

    #Text in About
    my_text=Label(aboutWindow,text='This game is created by: Dyami Worthy.',bg='red',fg='black',font=('arial',12,'bold')).pack()
    label2 = Label(aboutWindow, text='This game is developed using Python Tkinter!.', bg='red', fg='black',font=('arial', 12, 'bold')).pack()
    label3 = Label(aboutWindow, text='Lost a lot of sleep so I hope it nets some points...somehwere!', bg='red', fg='black',font=('arial', 12, 'bold')).pack()

    #Window Title(About)
    aboutWindow.wm_title("About")

    #Back button(About)
    backk = Button(aboutWindow, text='BACK', fg='white', bg='green', font=('arial', 14, 'bold'), command=close_window).place(x=100,y=350)
    aboutWindow.mainloop()
    
#==================================================================================
#MENU BUTTONS!~
#==================================================================================

#Start button(Opens Hangman)
start=Button(root, text = 'START', bg = 'cyan', fg= 'black', font=('arial', 17, 'bold'), command= game)
start.place(x=20, y=210)

#Options/User Info Button (Menu, cont.)
option = Button(root, text = 'OPTIONS', bg = 'cyan', fg='black', font=('arial', 14, 'bold'), command = optiongame)
option.place(x = 132, y = 217)

#Quit Button (Menu, cont.)
quit2 = Button(root, text = 'EXIT', bg = 'red', fg ='white', font=('arial', 12, 'bold'), command = exit1)
quit2.place(x= 250, y= 223)

#About Button (Menu, cont.)
about = Button(root, text = 'ABOUT', bg = 'gold', fg ='black', font=('arial', 12, 'bold'), command = about1).place(x=14, y= 550)

root.mainloop()


#==================================================================================
#CREDITS
#Parts of this code was originated by Rushikesh Gaikwad
#Or rushi718 on Github. Link: https://github.com/rushi718/Hangman-Game-using-tkinter-in-Python
#
#And Circle X: prostartprograming@gmail.com
#
#
#==================================================================================
