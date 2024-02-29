import tkinter
from cProfile import label
from tkinter import ttk, Tk
from tkinter import *
from subprocess import call
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image
from numpy import imag

def Retour():
	root.destroy()
	call(["python", "algo.py"])

def supprimer():
    code = ecode.get()

    maBase = mysql.connector.connect(host = "Localhost", user = "root", password="", database = "patient")
    meConnect = maBase.cursor()

    try:
        sql = "delete from patients where numero= %s"
        val = (code,)
        meConnect.execute(sql, val)
        maBase.commit()
        messagebox.showinfo("information","Patient supprimer")
        root.destroy()
        call(["python", "algo.py"])
    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()


#ma fenetre
root = Tk()

root.title("SUPPRESSION")
root.geometry("600x300+400+200")
root.resizable(False, False)
root.configure(background="#292929")

def button(x, y, img1, img2, cmd):
    image_a = ImageTk.PhotoImage(Image.open(img1))
    image_b = ImageTk.PhotoImage(Image.open(img2))

    def on_e(e):
        mybtn['image'] = image_b

    def on_l(e):
        mybtn['image'] = image_a

    mybtn = Button(root, image=image_b, border=0, cursor='hand2', relief=FLAT, command=cmd)

    mybtn.bind("<Enter>", on_e)
    mybtn.bind("<Leave>", on_l)
    mybtn.place(x=x, y=y)

#ajouter titre
code = Label(root, bg = "red",)
code.place(x=0,y=0,width=600,height = 10)

lbltitre = Label(root,borderwidth = 3, text = "SUPPRIMER PATIENT", font = ("consolas",20), background = "#292929",border = 10, foreground = "white")
lbltitre.place( x = 0, y = 10, width = 600)


code = Label(root, text = "Code", font = ("consolas", 16), bg = "#292929", fg="white")
code.place(x=150,y=100,width=300)
ecode = Entry(root,font="consolas")
ecode.place(x=150,y=150,width=300, height=30)

codee = Label(root, bg = "#292929",)
codee.place(x=150,y=181,width=300,height = 10)

def button(x,y, img1,img2,cmd):
    image_a = ImageTk.PhotoImage(Image.open(img1))
    image_b = ImageTk.PhotoImage(Image.open(img2))


    def on_e(e):
        mybtn['image'] = image_b

    def on_l(e):
        mybtn['image'] = image_a


    mybtn = Button(root,image = image_b,border = 0,cursor = 'hand2',relief = SUNKEN,command = cmd)
    
    mybtn.bind("<Enter>", on_e)
    mybtn.bind("<Leave>", on_l)
    mybtn.place(x = x, y = y)


button(240,200,"sup1.png","sup2.png",supprimer)

button(240,250,"ret1.png","ret2.png",Retour)

#Execute
root.mainloop()
