from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from numpy import *


def remplir(T,ch):
    global c
    a=0
    b=0
    c=0
    for i in range(len(ch)):
        if ch[i]=="." and i==len(ch)-1:
            T[a]=ch[b:i-1]
            c=c+1
        elif ch[i]==" ":
            T[a]=ch[b:i]
            a=a+1
            b=i+1
            c=c+1
def Trier(ch):
    remplir(T,ch)
    for i in range(c):
        for j in range(1,c):
            if len(T[j])<len(T[j-1]):
                T[j-1],T[j]=T[j],T[j-1]
    ch1=""
    for i in range(c):
        ch1=ch1+T[i]+" "
    return ch1

def verif(ch):
    i=1
    a=True
    while a==True and i<len(ch):
        if ch[i]==" "and ch[i-1]==" ":
            a=False
        i=i+1
    return a
def Play():
    ch=f.text.text()
    if len(ch)==0:
        f.res.setText("veuillez introduire une phrase")
    elif len(ch)>=50:
        f.res.setText("veuillez introduire une phrase de taille inférieure à 50")
    elif not("A"<=ch[0].upper()<="Z"):
        f.res.setText("la chaine doit  commence par une lettre")
    elif ch[-1]!=".":
        f.res.setText("la chaine doit terminer par un point")
    elif verif(ch)==False:
        f.res.setText("entre deux mots un seul espace est otorisé")
    else:
        f.res.setText(Trier(ch))
    
T=array([str]*50)


app=QApplication([])
f=loadUi("InterfaceTriage.ui")
f.show()
f.btn.clicked.connect(Play)
app.exec()