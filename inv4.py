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


root = Tk()
root.title("Gestion des patient ")
root.geometry("1080x980")
root.configure(bg="#292929")


def button(x, y, img1, img2, cmd):
    image_a = ImageTk.PhotoImage(Image.open(img1))
    image_b = ImageTk.PhotoImage(Image.open(img2))

    def on_e(e):
        mybtn['image'] = image_b

    def on_l(e):
        mybtn['image'] = image_a

    mybtn = Button(root, image=image_b, border=0, cursor='hand2', relief=SUNKEN, command=cmd)

    mybtn.bind("<Enter>", on_e)
    mybtn.bind("<Leave>", on_l)
    mybtn.place(x=x, y=y)


button(900, 20, "ret1.png", "ret2.png", Retour)


Patient = Label(root, text = "DIFFERENTES CLASSIFICATION DES PATIENTS", font = ("consolas", 16), bg = "#292929", fg="white")
Patient.place(x=0,y=0,width=1080)

stePatient = Label(root, text = "PALUDISME", font = ("consolas", 16), bg = "#292929", fg="white")
stePatient.place(x=0,y=50,width=530)
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",
    background = "#292929",
    foreground = "white",
    rowheight = 25,
    fieldbackground = "#292929")

table4 = ttk.Treeview(root, columns = (1, 2), height = 5, show = "headings")
table4.place(x = 0,y = 100, width = 530, height = 400)

#Entete
table4.heading(1 , text = "CODE")
table4.heading(2 , text = "NOM")

#definir les dimentions des colonnes
table4.column(1,width = 50)
table4.column(2,width = 100)

# afficher les informations de la table
maBase = mysql.connector.connect(host = "localhost", user = "root", password="", database = "patient")
meConnect = maBase.cursor()
meConnect.execute("select * from palu")
for row in meConnect:
    table4.insert('', END, value = row)
maBase.close()


istePatient = Label(root, text = "FIEVRE", font = ("consolas", 16), bg = "#292929", fg="white")
istePatient.place(x=540,y=50,width=530)

table3 = ttk.Treeview(root, columns = (1, 2), height = 5, show = "headings")
table3.place(x = 540,y = 100, width = 530, height = 400)

#Entete
table3.heading(1 , text = "CODE")
table3.heading(2 , text = "NOM")

#definir les dimentions des colonnes
table3.column(1,width = 50)
table3.column(2,width = 100)

# afficher les informations de la table
maBase = mysql.connector.connect(host = "localhost", user = "root", password="", database = "patient")
meConnect = maBase.cursor()
meConnect.execute("select * from fievre")
for row in meConnect:
    table3.insert('', END, value = row)
maBase.close()


lListePatient = Label(root, text = "FATIGUE", font = ("consolas", 16), bg = "#292929", fg="white")
lListePatient.place(x=0,y=505,width=530)

table2 = ttk.Treeview(root, columns = (1, 2), height = 5, show = "headings")
table2.place(x = 0,y = 540, width = 530, height = 400)

#Entete
table2.heading(1 , text = "CODE")
table2.heading(2 , text = "NOM")

#definir les dimentions des colonnes
table2.column(1,width = 50)
table2.column(2,width = 100)

# afficher les informations de la table
maBase = mysql.connector.connect(host = "localhost", user = "root", password="", database = "patient")
meConnect = maBase.cursor()
meConnect.execute("select * from fatigue")
for row in meConnect:
    table2.insert('', END, value = row)
maBase.close()


blListePatient = Label(root, text = "CAS URGENT", font = ("consola", 16), bg = "#292929", fg="white")
blListePatient.place(x=540,y=505,width=530)

table1 = ttk.Treeview(root, columns = (1, 2), height = 5, show = "headings")
table1.place(x = 540,y = 540, width = 530, height = 400)

#Entete
table1.heading(1 , text = "CODE")
table1.heading(2 , text = "NOM")

#definir les dimentions des colonnes
table1.column(1,width = 50)
table1.column(2,width = 100)

# afficher les informations de la table
maBase = mysql.connector.connect(host = "localhost", user = "root", password="", database = "patient")
meConnect = maBase.cursor()
meConnect.execute("select * from urgent")
for row in meConnect:
    table1.insert('', END, value = row)
maBase.close()

root.mainloop()