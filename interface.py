import tkinter as tk
from tkinter import messagebox
import os
from _functools import partial

window = tk.Tk()
window.title("Urbook")
window.geometry("920x800")
window.config(background='#dfcfc3')

def videfenetre(window):
    for widget in window.winfo_children().copy():
        widget.destroy()

l= os.listdir(".")
if "compte" not in l:
    os.mkdir("compte")

l1= os.listdir(".")
if "histoire" not in l1:
    os.mkdir("histoire")

def verif(user, mdp, mdprpt):
    Nom=user.get()
    Mdp=mdp.get()
    Mdp2=mdprpt.get()
    a=len(Mdp)
    if str(Mdp)!=str(Mdp2):
        messagebox.showerror("erreur", 'Vos mots de passe ne se correspondent pas')
        return

    if a<=6:
        messagebox.showinfo("Erreur", 'Votre mot de passe est trop court')
        return
    ch=str(Nom)+"="+str(Mdp)
    messagebox.showinfo("Bienvenue", 'Votre compte est enregistré')

    textfichier = str("")

    try:
        with open("compte/userandmdp.txt", "r") as fichier:
            textfichier=fichier.read()
            fichier.close()
    except Exception:
        pass

    with open("compte/userandmdp.txt", "w") as fichier:
        fichier.write(textfichier+"\n" + ch)
        fichier.close()

    return True

def verif1(user, mdp):
    Nom = user.get()
    Mdp = mdp.get()
    if  connection(Nom , Mdp):
        return True
    else :
        messagebox.showerror("identifiant et/ou mot de passe incorrecte")

def connection(Nom, Mdp):

    with open("compte/userandmdp.txt", "r")as fichier:
        lignes = fichier.readlines()
        fichier.close()
    ligne2 = []
    for ligne in lignes:
        ligne2.append(ligne.replace("\n","").split("="))
    for element in ligne2:
        if element[0]==Nom and element[1] == Mdp:
            return True

def accueilboutton(window):
    frame_accueil = tk.Frame(window)
    label_title = tk.Label(frame_accueil, text="Urbook", font=("Alegreya SC", 115), bg='#65391f', fg='white')
    label_title.pack(fill='x')

    frame = tk.Frame(frame_accueil, bg='#dfcfc3')
    consigne = tk.Label(frame, text="Choisissez votre camp\n", font=("Open Sans", 65), bg='#dfcfc3')
    b_createur = tk.Button(frame, text="créateur", font=("Open Sans", 60), bg='#ebe2dc', fg='#737373', bd=0, command= partial(changementcreateur, window))
    b_lecteur = tk.Button(frame, text="lecteur", font=("Open Sans", 60), bg='#ebe2dc', fg='#737373', bd=0, command= partial(changementverslecteur, window))
    consigne.pack()
    b_createur.pack(side='right')
    b_lecteur.pack(side='left')
    frame.pack(expand='True')

    barre_bas = tk.Frame(frame_accueil, bg='#926e54')
    nous = tk.Button(barre_bas, text="À propos de nous", font=("Open Sans", 30), bg='#926e54', fg='white', bd=0)
    nous.pack(side='left')
    barre_bas.pack(fill='x', anchor='s')
    frame_accueil.pack(fill='x')
    window.mainloop()

def retourmenu2(window,user, mdp, mdprpt):
    if verif(user, mdp, mdprpt):
        videfenetre(window)
        accueil(window)

def retouraccueilboutton(window, user, mdp):
    if verif1(user, mdp):
        videfenetre(window)
        accueilboutton(window)

def creationcompte(fen1):
    fond= tk.Canvas(fen1,width=800,height=800,bg='#dfcfc3')
    fond.grid()

    user= tk.Entry(fen1)
    mdp=tk.Entry(fen1,show="*")
    mdprpt=tk.Entry(fen1, show="*")
    label_title = tk.Label(fen1, text="création du compte", font=("Alegreya SC", 30), bg='#65391f', fg='white')
    usertxt=tk.Label(text="Nom d'utilisateur :",font=("Open Sans", 25), bg='#dfcfc3')
    mdptxt=tk.Label(text="Mot de passe :",font=("Open Sans", 25), bg='#dfcfc3')
    mdprpttxt=tk.Label(text="Mot de passe :",font=("Open Sans", 25), bg='#dfcfc3')

    buttonverif =tk.Button(fen1,font=("Open Sans", 30), text="valider", bg='#dfcfc3',fg='#737373', command=partial(retourmenu2, fen1, user , mdp, mdprpt ))

    fond.create_window(250,25,window=label_title)
    fond.create_window(380,100,window=user)
    fond.create_window(320,170,window=mdp)
    fond.create_window(320,230,window=mdprpt)
    fond.create_window(150,100,window=usertxt)
    fond.create_window(120,170,window=mdptxt)
    fond.create_window(120,230,window=mdprpttxt)
    fond.create_window(250,300,window=buttonverif)

def connexion(fen1):
    fond = tk.Canvas(fen1,width=800,height=800,bg='#dfcfc3')
    fond.grid()

    user= tk.Entry(fen1)
    mdp=tk.Entry(fen1,show="*")

    label_title = tk.Label(fen1, text="connexion", font=("Alegreya SC", 30), bg='#65391f', fg='white')
    usertxt=tk.Label(text="Nom d'utilisateur :",font=("Open Sans", 25), bg='#dfcfc3')
    mdptxt=tk.Label(text="Mot de passe :",font=("Open Sans", 25), bg='#dfcfc3')

    buttonverif =tk.Button(fen1, font=("Open Sans", 30), text="valider", bg='#dfcfc3', fg='#737373', command= partial(retouraccueilboutton, fen1, user, mdp))

    fond.create_window(250,25,window=label_title)
    fond.create_window(380,100,window=user)
    fond.create_window(320,170,window=mdp)
    fond.create_window(150,100,window=usertxt)
    fond.create_window(120,170,window=mdptxt)
    fond.create_window(250,300,window=buttonverif)
    fen1.mainloop()

def changementverscreacompte(window):
    videfenetre(window)
    creationcompte(window)

def changementverslecteur(window):
    videfenetre(window)
    lecteur(histoiredrame, histoirecomedie, histoirehorreur, histoirefantastique, histoireaction)

def changementcreateur(window):
    videfenetre(window)
    createur(window)

def changementversconnexion(window):
    videfenetre(window)
    connexion(window)

def accueil(window):
    frame_acceuil = tk.Frame(window)
    frame_acceuil.config( bg='#dfcfc3')
    label_title = tk.Label(frame_acceuil, text= "Urbook", font=("Alegreya SC", 115), bg='#65391f', fg='white')
    label_title.pack(fill='x')

    barre_haut = tk.Frame(frame_acceuil, bg='#926e54')
    connexion = tk.Button(barre_haut, text="connexion", font=("Open Sans", 30), bg='#926e54', fg='white', bd=0, command = partial(changementversconnexion, window))
    cree = tk.Button(barre_haut, text="créer un compte", font=("Open Sans", 30), bg='white', fg='#65391f', bd=0, command = partial(changementverscreacompte, window))
    cree.pack(side= 'right')
    connexion.pack(side = 'right')
    barre_haut.pack(fill= 'x')

    label_title1 = tk.Label(frame_acceuil, text="Bienvenue sur Urbook\n Veuillez vous connecter ou creer un compte", font=("Alegreya SC", 30), bg='#dfcfc3', fg='black')
    label_title1.pack(fill='x', pady='10', anchor='center')

    frame = tk.Frame(frame_acceuil, bg ='#dfcfc3')

    consigne = tk.Label(frame, text= "Choisissez votre camp\n", font= ("Open Sans", 65), bg='#dfcfc3', fg='#dfcfc3')
    b_createur = tk.Label(frame, text="créateur", font=("Open Sans", 60), bg='#dfcfc3', fg='#dfcfc3')
    b_lecteur = tk.Label(frame, text="lecteur", font=("Open Sans", 60), bg='#dfcfc3', fg='#dfcfc3')
    consigne.pack()
    b_createur.pack(side= 'right')
    b_lecteur.pack(side = 'left')
    frame.pack(expand = 'True')

    barre_bas= tk.Frame( frame_acceuil, bg='#926e54')
    nous= tk.Button(barre_bas, text="À propos de nous", font=("Open Sans", 30), bg='#926e54', fg='white',bd=0)
    nous.pack(side = 'left')

    frame_acceuil.pack()
    barre_bas.pack(fill='x', side='bottom')
    window.mainloop()

def createur(window):
    frame = tk.Frame(window, bg='#dfcfc3')
    label_title = tk.Label(frame, text="MODE CREATEUR", font=("Open sans", 70), bg='#65391f', fg='white')
    label_title.pack(anchor = 'center', fill='x')
    frame.pack(fill= 'x')

    frame = tk.Frame(window, bg ='#dfcfc3')
    consigne = tk.Label(frame, text= "Que voulez-vous faire ?\n", font= ("Open Sans", 60), bg='#dfcfc3')
    nouvellehistoire = tk.Button(frame, text="commencer une histoire", font=("Open Sans", 30), bg='#ebe2dc', fg='#737373', bd=0, command=partial(changementversnomhistoire, window))
    modifierhistoire = tk.Button(frame, text="modifier une histoire", font=("Open Sans", 30), bg='#ebe2dc', fg='#737373', bd=0)
    consigne.pack()
    nouvellehistoire.pack(side= 'right',padx=15)
    modifierhistoire.pack(side = 'left',padx=15)
    frame.pack(expand = 'True')

    barre_bas= tk.Frame(window, bg='#926e54')
    nous = tk.Button(barre_bas, text="A propos de nous", font=("Open Sans", 30), bg='#926e54', fg='white',bd=0)
    nous.pack(side = 'left')
    barre_bas.pack(fill= 'x')

    window.mainloop()

def changementversnomhistoire(window):
    videfenetre(window)
    nomhistoire(window)

def nomhistoire(window):
    ecrivezno = tk.Label(window, text="Veuillez ecrire le titre de votre histoire : ", font=("Open Sans", 20), bg='#dfcfc3', pady=10)
    ecrivezno.pack()

    nomhistoire = tk.Entry(window, width=40)
    nomhistoire.pack()

    enregistrer = tk.Button(window, text="enregistrer", font=("Open Sans", 30), bg='#dfcfc3', command=ecriturehistoire)
    enregistrer.pack()

def retourmenu8(window,nomhistoire):
    if save2(nomhistoire):
        videfenetre(window)
        ecriturehistoire(window)

def retourecriturehistoire(window, pages, numero):
    if save(pages, numero):
        videfenetre(window)
        ecriturehistoire(window)

def ecriturehistoire(window):

    ecrivez = tk.Label(window, text= "Veuillez ecrire votre histoire : ", font=("Open Sans", 20), bg='#dfcfc3', pady=10)
    ecrivez.pack()

    pages = tk.Text(window,height = 25, width= 100)
    pages.pack()

    numeropage = tk.Label(window, text="numero de la page : ", font=("Open Sans", 20), bg='#dfcfc3', pady= 10)
    numeropage.pack()
    numero = tk.Entry(window, width= 40)
    numero.pack()

    enregistrer = tk.Button(window, text= "enregistrer", font= ("Open Sans", 30), bg='#dfcfc3', command = partial(retourecriturehistoire, window, pages, numero))
    enregistrer.pack(side='left', anchor='s', padx=60 ,pady=40)

    nouvelle_page = tk.Button(window, text="nouvelle page", font= ("Open Sans", 30), bg='#dfcfc3', command=ecriturehistoire)
    nouvelle_page.pack(side='right', anchor='s', padx= 60, pady=40)

def save(pages, numero, nomhistoirev):
    histoire = pages.get("1.0","end")
    numeropa = numero.get()

    ch1 = str(histoire) + "=" + str(numeropa)
    textfichier1 = str("")

    try:
        with open("histoire/"+nomhistoirev+"txt", "r") as fichier1:
            textfichier1 = fichier1.read()
            fichier1.close()
    except Exception:
        pass

    with open("histoire/"+nomhistoirev+"txt", "w") as fichier1:
        fichier1.write(textfichier1+"\n" + ch1)
        fichier1.close()
    return True

def save2(nomhistoire):
    nomhistoirev = nomhistoire.get()
    open("histoire/"+nomhistoirev+".txt")

def histoiredrame(frame_button1):
    win = tk.Toplevel(frame_button1)
    window.title("Drame")
    window.geometry("1080x720")
    win.config(background='#dfcfc3')

    a_frame = tk.Frame(win)
    a_frame.config(bg='#dfcfc3')

def histoireaction(frame_button1):
    win = tk.Toplevel(frame_button1)
    window.title("Action")
    window.geometry("1080x720")
    win.config(background='#dfcfc3')

    a_frame = tk.Frame(win)
    a_frame.config(bg='#dfcfc3')

def histoireromance(frame_button1):
    win = tk.Toplevel(frame_button1)
    window.title("Romance")
    window.geometry("1080x720")
    win.config(background='#dfcfc3')

    a_frame = tk.Frame(win)
    a_frame.config(bg='#dfcfc3')

def histoirehorreur(frame_button2):
    win = tk.Toplevel(frame_button2)
    window.title("Horreur")
    window.geometry("1080x720")
    win.config(background='#dfcfc3')

    a_frame = tk.Frame(win)
    a_frame.config(bg='#dfcfc3')

def histoirecomedie(frame_button2):
    win = tk.Toplevel(frame_button2)
    window.title("Comedie")
    window.geometry("1080x720")
    win.config(background='#dfcfc3')

    a_frame = tk.Frame(win)
    a_frame.config(bg='#dfcfc3')

def histoirefantastique(frame_button2):
    win = tk.Toplevel(frame_button2)
    window.title("Fantastique")
    window.geometry("1080x720")
    win.config(background='#dfcfc3')

    a_frame = tk.Frame(win)
    a_frame.config(bg='#dfcfc3')

def lecteur(crea2, crea6, crea5, crea7, crea3):
    print("a")
    frame = tk.Frame(window, bg='#dfcfc3')
    modelecteur = tk.Label(frame, text="MODE LECTEUR", font=("Open sans", 70), bg='#65391f', fg='white', pady=10)
    modelecteur.pack(anchor='center', fill='x')
    frame.pack(fill='x')

    question = tk.Frame(window)
    question.config(bg='#dfcfc3')
    label_question = tk.Label(question, text="Choisissez un genre !", font=("Open sans", 60), bg='#dfcfc3', fg='white')
    label_question.pack(anchor='center', fill='x', pady=20)
    question.pack()

    frame_buttong = tk.Frame(window)
    frame_buttong.configure(bg='#dfcfc3')

    frame_button1 = tk.Frame(frame_buttong)
    frame_button1.config(bg='#dfcfc3')
    drame = tk.Button(frame_button1, text="Drame", font=("Open sans", 30), bg='#926e54', fg='white', bd=0,
                      command=partial(crea2, frame_button1))
    action = tk.Button(frame_button1, text="Action", font=("Open sans", 30), bg='#926e54', fg='white', bd=0,
                       command=partial(crea3, frame_button1))
    romance = tk.Button(frame_button1, text="Romance", font=("Open sans", 30), bg='#926e54', fg='white', bd=0,
                        command=partial(histoireromance, frame_button1))

    frame_button2 = tk.Frame(frame_buttong)
    frame_button2.config(bg='#dfcfc3')
    horreur = tk.Button(frame_button2, text="Horreur", font=("Open sans", 30), bg='#926e54', fg='white', bd=0,
                        command=partial(crea5, frame_button2))
    comedie = tk.Button(frame_button2, text="Comedie", font=("Open sans", 30), bg='#926e54', fg='white', bd=0,
                        command=partial(crea6, frame_button2))
    fantastique = tk.Button(frame_button2, text="Fantastique", font=("Open sans", 30), bg='#926e54', fg='white', bd=0,
                            command=partial(crea7, frame_button2))

    drame.pack(side='left', padx=20)
    action.pack(side='left', padx=20)
    romance.pack(side='right', padx=20)
    horreur.pack(side='left', padx=20)
    comedie.pack(side='left', padx=20)
    fantastique.pack(side='right', padx=20)

    frame_button1.pack(anchor='center', )
    frame_button2.pack(anchor='center', pady=40)
    frame_buttong.pack(anchor='center', expand='true')
    window.mainloop()

accueil(window)
accueilboutton(window)
createur(window)
lecteur(histoiredrame, histoirecomedie, histoirehorreur, histoirefantastique, histoireaction)