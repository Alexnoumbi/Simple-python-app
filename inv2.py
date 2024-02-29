from cProfile import label
from tkinter import *
from subprocess import call
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image

def Retour():
    root.destroy()
    call(["python", "algo.py"])

def Modifier():
    code = ecode.get()
    nom = entrernom.get()
    prenom = entrerPrenom.get()
    telephone = entrertelephone.get()
    age = entrerage.get()
    endicap = entrerendicap.get()
    remarque = entrerremarque.get()

    #Creeon la connexion
    maBase = mysql.connector.connect(host = "Localhost", user = "root", password="", database = "patient")
    meConnect = maBase.cursor()
    
    try:
        sql = "update patients set nom = %s, prenom = %s, telephone = %s, age = %s, endicap = %s ,remarque = %s where numero = %s"
        val = (nom, prenom, telephone, age, endicap, remarque,code)
        meConnect.execute(sql,val)
        maBase.commit()
        derniereMatricule = meConnect.lastrowid
        messagebox.showinfo("information","patient bien Enregistrer")
        root.destroy()
        call(["python", "inv3.py"])
    except Exception as e:
        print(e)
        #retour
        maBase.rollback()
        maBase.close()


#ma fenetre
root = Tk()

root.title("MODIFICATION")
root.geometry("600x800+400+200")
root.resizable(False, False)
root.configure(background="#292929")


def button(x, y, img1, img2, cmd):
    image_a = ImageTk.PhotoImage(Image.open(img1))
    image_b = ImageTk.PhotoImage(Image.open(img2))

    def on_e(e):
        mybtn['image'] = image_b

    def on_l(e):
        mybtn['image'] = image_a

    mybtn = Button(root, image=image_b, border=0, cursor='hand2', command=cmd)

    mybtn.bind("<Enter>", on_e)
    mybtn.bind("<Leave>", on_l)
    mybtn.place(x=x, y=y)

#ajouter titre
lbltitre = Label(root,borderwidth = 0, relief = SUNKEN
	, text = "MODIFIER PATIENT", font = ("consolas",28), background = "#292929", foreground = "#FEFEFE")
lbltitre.place( x = 0, y = 0, width = 600)
c = Label(root, bg = "#007FFF",)
c.place(x=0,y=40,width=600,height =5)

code = Label(root, text = "Code Patient a modif", font = ("consolas", 16), bg = "#292929", fg="white")
code.place(x=150,y=70,width=300)
ecode = Entry(root,bg="#292929",fg="white",border=0,font="consolas")
ecode.place(x=150,y=100,width=300, height=30)
c = Label(root, bg = "#007FFF")
c.place(x=150,y=120,width=300,height =2)

lblnom = Label(root, text = "Nom Patient", font = ("consolas", 16), bg = "#292929", fg="white")
lblnom.place(x=150,y=170,width=300)
entrernom = Entry(root,bg="#292929",fg="white",border=0,font="consolas")
entrernom.place(x=150,y=200,width=300,height=30)
ce = Label(root, bg = "#007FFF")
ce.place(x=150,y=220,width=300,height =2)

#text prenom
lblPrenom = Label(root, text = "Prenom Patient", font = ("consolas", 16), bg = "#292929", fg="white")
lblPrenom.place(x=150,y=270,width=300)
entrerPrenom = Entry(root,bg="#292929",fg="white",border=0,font="consolas")
entrerPrenom.place(x=150,y=300,width=300,height=30)
cee = Label(root, bg = "#007FFF")
cee.place(x=150,y=320,width=300,height =2)

#text age
lblage = Label(root, text = "Age Patient", font = ("consolas", 16), bg = "#292929", fg="white")
lblage.place(x=150,y=370,width=300)
entrerage = Entry(root,bg="#292929",fg="white",border=0,font="consolas")
entrerage.place(x=150,y=400,width=300,height=30)
ace = Label(root, bg = "#007FFF")
ace.place(x=150,y=420,width=300,height =2)

#text Telephone
lbltelephone = Label(root, text = "Telephone Patient", font = ("consolas", 16), bg = "#292929", fg="white")
lbltelephone.place(x=150,y=470,width=300)
entrertelephone = Entry(root,bg="#292929",fg="white",border=0,font="consolas")
entrertelephone.place(x=150,y=500,width=300,height=30)
ace = Label(root, bg = "#007FFF")
ace.place(x=150,y=520,width=300,height =2)

lblendicap = Label(root, text = " Endicap", font = ("consolas", 16), bg = "#292929", fg="white")
lblendicap.place(x=150,y=570,width=300)
entrerendicap = Entry(root,bg="#292929",fg="white",border=0,font="consolas")
entrerendicap.place(x=150,y=600,width=300,height=30)
ace = Label(root, bg = "#007FFF")
ace.place(x=150,y=620,width=300,height =2)

#text remarque
lblremarque = Label(root, text = "Remarque Patient", font = ("consolas", 16), bg = "#292929", fg="white")
lblremarque.place(x=150,y=670,width=300)
entrerremarque = Entry(root,bg="#292929",fg="white",border=0,font="consolas")
entrerremarque.place(x=150,y=700,width=300,height=30)
ace = Label(root, bg = "#007FFF")
ace.place(x=150,y=720,width=300,height =2)

button(450, 50, "ret1.png", "ret2.png", Retour)
button(200, 750, "enr2.png", "enr1.png", Modifier)

#Execute
root.mainloop()
