import tkinter
from cProfile import label
from tkinter import ttk, Tk
from tkinter import *
from subprocess import call
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image
 
def categorie(a,b,c,d,e,f):
    if a == 1 and d == 1:
        return 1
    elif b == 1 and f == 1:
        return 2
    elif c == 1 and d == 1:
        return 3
    else:
     return 4 



def Retour():
    root.destroy()
    call(["python", "algo.py"])

def Ajouter():
    code = ecode.get()
    nom22 = nom2.get()
    nom = entrernom.get()
    prenom = entrerPrenom.get()
    telephone = entrertelephone.get()
    age = entrerage.get()
    endicap = entrerendicap.get()
    remarque = entrerremarque.get()

    a2 = categorie(nom,prenom,telephone,age,endicap,remarque)
    #Creeon la connexion
    maBase = mysql.connector.connect(host = "Localhost", user = "root", password="", database = "patient")
    meConnect = maBase.cursor()
    
    try:

        if a2 == 1:
            sql = "INSERT INTO palu(idpalu,nompatient) VALUES (%s,%s)"
            val = (code,nom22)
            meConnect.execute(sql,val)
            maBase.commit()
            derniereMatricule = meConnect.lastrowid

        elif a2 == 2:
            sql = "INSERT INTO fievre(numero,nom) VALUES (%s,%s)"
            val = (code,nom22)
            meConnect.execute(sql,val)
            maBase.commit()
            derniereMatricule = meConnect.lastrowid

        elif a2 == 3:
            sql = "INSERT INTO fatigue(numero,nom) VALUES (%s,%s)"
            val = (code,nom22)
            meConnect.execute(sql,val)
            maBase.commit()
            derniereMatricule = meConnect.lastrowid

        elif a2 == 4:
            sql = "INSERT INTO urgent(numero,nom) VALUES (%s,%s)"
            val = (code,nom22)
            meConnect.execute(sql,val)
            maBase.commit()
            derniereMatricule = meConnect.lastrowid




        sql = "INSERT INTO syntomes (numero,maux, vomis ,fiev , fatig , endicap ,malventre) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (code,nom, prenom, telephone, age, endicap, remarque)
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


#ma fenetre
root = Tk()

root.title("MODIFICATION")
root.geometry("600x900")
root.resizable(False, False)
root.configure(background="#292929")

style = ttk.Style()
style.theme_use("clam")
style.configure("combobox",
    background = "#292929",
    foreground = "white",
    rowheight = 25,
    fieldbackground = "#292929")


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
lbltitre = Label(root,borderwidth = 3, relief = FLAT
    , text = "SYNTOMES PATIENT", font = ("consolas",25), background = "#292929", foreground = "white")
lbltitre.place( x = 0, y = 0, width = 600)

code = Label(root, text = "Code ", font = ("consolas", 16), bg = "#292929", fg="#FEFEFE")
code.place(x=150,y=50,width=300)
ecode = Entry(root,bg="#292929",fg="white",border=0,font="consolas")
ecode.place(x=150,y=80,width=300, height=30)
codee = Label(root, bg = "#FEFEFE",)
codee.place(x=150,y=105,width=300,height =5)

nom1 = Label(root, text = "Nom Patient", font = ("consolas", 16), bg = "#292929", fg="white")
nom1.place(x=150,y=150,width=300)
nom2 = Entry(root,bg="#292929",fg="white",border=0,font="consolas")
nom2.place(x=150,y=180,width=300, height=30)
c = Label(root, bg = "#FEFEFE",)
c.place(x=150,y=205,width=300,height =5)

lblnom = Label(root, text = "Maux De Tete", font = ("consolas", 16), bg = "#292929", fg="white")
lblnom.place(x=150,y=250,width=300)

entrernom = ttk.Combobox(root,font=("consolas",14))
entrernom['value'] = ['1','0']
entrernom.place(x=150,y=280,width=300,height=30)
c = Label(root, bg = "#FEFEFE",)
c.place(x=150,y=305,width=300,height =5)

lblPrenom = Label(root, text = "Vomissement", font = ("consolas", 16), bg = "#292929", fg="white")
lblPrenom.place(x=150,y=350,width=300)

entrerPrenom = ttk.Combobox(root,font=("consolas",14))
entrerPrenom['value'] = ['1','0']
entrerPrenom.place(x=150,y=380,width=300,height=30)
ca = Label(root, bg = "#FEFEFE",)
ca.place(x=150,y=405,width=300,height =5)

#text age
lblage = Label(root, text = "Fievre", font = ("consolas", 14), bg = "#292929", fg="white")
lblage.place(x=150,y=450,width=300)

entrerage = ttk.Combobox(root,font=("consolas",14))
entrerage['value'] = ['1','0']
entrerage.place(x=150,y=480,width=300,height=30)
ca = Label(root, bg = "#FEFEFE",)
ca.place(x=150,y=505,width=300,height =5)


#text Telephone
lbltelephone = Label(root, text = "Fatigue", font = ("consolas", 14), bg = "#292929", fg="white")
lbltelephone.place(x=150,y=550,width=300)

entrertelephone = ttk.Combobox(root,font=("consolas",14))
entrertelephone['value'] = ['1','0']
entrertelephone.place(x=150,y=580,width=300,height=30)
cae = Label(root, bg = "#FEFEFE",)
cae.place(x=150,y=605,width=300,height =5)

lblendicap = Label(root, text = "Maux de ventre", font = ("consola", 14), bg = "#292929", fg="white")
lblendicap.place(x=150,y=650,width=300)

entrerendicap =ttk.Combobox(root,font=("consolas",14))
entrerendicap['value'] = ['1','0']
entrerendicap.place(x=150,y=680,width=300,height=30)
cdae = Label(root, bg = "#FEFEFE",)
cdae.place(x=150,y=705,width=300,height =5)

#text remarque
lblremarque = Label(root, text = "Endicaper", font = ("consola", 14), bg = "#292929", fg="white")
lblremarque.place(x=150,y=750,width=300)

entrerremarque =ttk.Combobox(root,font=("Arial",12))
entrerremarque['value'] = ['1','0']
entrerremarque.place(x=150,y=780,width=300,height=30)
cdaee = Label(root, bg = "#FEFEFE",)
cdaee.place(x=150,y=805,width=300,height =5)

button(450, 50, "ret1.png", "ret2.png", Retour)
button(200, 820, "enr2.png", "enr1.png", Ajouter)
#Execute
root.mainloop()
