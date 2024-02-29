#importer les tkinterimport tkinter
from cProfile import label
from tkinter import ttk, Tk
from tkinter import *
from subprocess import call
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image
from numpy import imag


def consul():
    root.destroy()
    call(["python","inv4.py"])

def Quitr():
    messagebox.showinfo("Information", "A biento")
    root.destroy()


nom1 = " "
def ajouter():
    nom = entrernom.get()
    prenom = entrerPrenom.get()
    telephone = entrertelephone.get()
    age = entrerage.get()
    endicap = entrerendicap.get()
    remarque = entrerremarque.get()

    nom1 = nom

    #Creeon la connexion
    maBase = mysql.connector.connect(host = "Localhost", user = "root", password="", database = "patient")
    meConnect = maBase.cursor()
    
    try:
        sql = "INSERT INTO patients (nom, prenom, telephone, age, endicap,remarque) VALUES (%s, %s, %s, %s, %s,%s)"
        val = (nom, prenom, telephone, age, endicap,remarque)
        meConnect.execute(sql,val)
        maBase.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information","patient bien Enregistrer")

        root.destroy()

        call(["python", "algo.py"])

    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()

def modifier():
        root.destroy()
        call(["python","inv2.py"])

def supprimer():
    
        root.destroy()
        call(["python", "inv.py"])


#titre general
root = Tk()
root.title("Gestion des patient ")
root.geometry("1300x700")
root.configure(bg = "#292929")


def button(x, y, img1, img2, cmd):
    image_a = ImageTk.PhotoImage(Image.open(img1))
    image_b = ImageTk.PhotoImage(Image.open(img2))

    def on_e(e):
        mybtn['image'] = image_b

    def on_l(e):
        mybtn['image'] = image_a

    mybtn = Button(root, image=image_b, border=0,relief=FLAT, cursor='hand2', command=cmd)

    mybtn.bind("<Enter>", on_e)
    mybtn.bind("<Leave>", on_l)
    mybtn.place(x=x, y=y)




#button(250, 250, "ret1.png", "ret2.png", Retour)


#Ajouter le titre
lbltitre = Label(root,bd =0, relief = SUNKEN, text = "GESTION DES PATIENTS DE LA CLINIQUE LES MERVEILLES", font = ("consolas", 28), bg = "#292929", fg="white")
lbltitre.place(x = 0, y = 0, width = 1300)

ode = Label(root, bg = "#007FFF",)
ode.place(x=0,y=50,width=1300,height = 10)

#Liste des patients
lblListePatient = Label(root, text = "LISTES DES PATIENTS ", font = ("consolas", 16), bg = "#292929", fg="white")
lblListePatient.place(x=600,y=100,width=760)

code = Label(root, bg = "#007FFF",)
code.place(x=600,y=130,width=750,height = 10)

#text nom
lblnom = Label(root, text = "Nom Patient", font = ("consolas", 16), bg = "#292929", fg="white")
lblnom.place(x=0,y=150,width=200)
entrernom = Entry(root,bg="#292929",fg="white",border=0,font="consolas")
entrernom.place(x=200,y=150,width=200,height=30)
codee = Label(root, bg = "white",)
codee.place(x=200,y=180,width=200,height = 2)

#text prenom
lblPrenom = Label(root, text = "Prenom Patient", font = ("consolas", 16), bg = "#292929", fg="white")
lblPrenom.place(x=0,y=200,width=200)
entrerPrenom = Entry(root,bg="#292929",fg="white",border=0,font="consolas")
entrerPrenom.place(x=200,y=200,width=200,height=30)
codeee = Label(root, bg = "white",)
codeee.place(x=200,y=230,width=200,height = 2)

#text age
lblage = Label(root, text = "Age Patient", font = ("consolas", 16), bg = "#292929", fg="white")
lblage.place(x=0,y=250,width=200)
entrerage = Entry(root,bg="#292929",fg="white",border=0,font="consolas")
entrerage.place(x=200,y=250,width=200,height=30)
ccodeee = Label(root, bg = "white",)
ccodeee.place(x=200,y=280,width=200,height = 2)

#text Telephone
lbltelephone = Label(root, text = "Telephone Patient", font = ("consolas", 14), bg = "#292929", fg="white")
lbltelephone.place(x=0,y=300,width=200)
entrertelephone = Entry(root,bg="#292929",fg="white",border=0,font="consolas")
entrertelephone.place(x=200,y=300,width=200,height=30)
codeee = Label(root, bg = "white",)
codeee.place(x=200,y=330,width=200,height = 2)

lblendicap = Label(root, text = " Endicap", font = ("#consola", 16), bg = "#292929", fg="white")
lblendicap.place(x=0,y=350,width=200)
entrerendicap = Entry(root,bg="#292929",fg="white",border=0,font="consolas")
entrerendicap.place(x=200,y=350,width=200,height=30)
codeee = Label(root, bg = "white",)
codeee.place(x=200,y=380,width=200,height = 2)

#text remarque
lblremarque = Label(root, text = "Remarque Patient", font = ("consolas", 16), bg = "#292929", fg="white")
lblremarque.place(x=0,y=400,width=200)
entrerremarque = Entry(root,bg="#292929",fg="white",border=0,font="consolas")
entrerremarque.place(x=200,y=400,width=200,height=30)
coddeee = Label(root, bg = "white",)
coddeee.place(x=200,y=430,width=200,height = 2)


#Enregistrer
button(30, 460, "enr1.png", "enr2.png", ajouter)

#modifier
button(270, 460, "mod1.png", "mod2.png", modifier)

#Supprimer
button(800, 600, "sup1.png", "sup2.png", supprimer)

button(600, 600, "con1.png", "con2.png", consul)

button(1000, 600, "qui1.png", "qui2.png", Quitr)
#Table
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",
    background = "#292929",
    foreground = "white",
    rowheight = 25,
    fieldbackground = "#292929")


table = ttk.Treeview(root, columns = (1, 2, 3, 4, 5, 6,7), height = 5, show = "headings")
table.place(x = 600,y = 150, width = 660, height = 400)


#Entete
table.heading(1 , text = "CODE")
table.heading(2 , text = "NOM")
table.heading(3 , text = "PRENOM")
table.heading(4 , text = "TELEPHONE")
table.heading(5 , text = "AGE")
table.heading(6 , text = "ENDICAPE")
table.heading(7 , text = "REMARQUE")

#definir les dimentions des colonnes
table.column(1,width = 50)
table.column(2,width = 100)
table.column(3,width = 100)
table.column(4,width = 100)
table.column(5,width = 50)
table.column(6,width = 100)
table.column(7,width = 100)




# afficher les informations de la table
maBase = mysql.connector.connect(host = "localhost", user = "root", password="", database = "patient")
meConnect = maBase.cursor()
meConnect.execute("select * from patients")
for row in meConnect:
    table.insert('', END, value = row)
maBase.close()

root.mainloop()