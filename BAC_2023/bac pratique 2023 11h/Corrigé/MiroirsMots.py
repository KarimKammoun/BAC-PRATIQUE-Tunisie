from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication


def Miroir (m):
    m=m+" "
    m2=""
    a=0
    for i in range(len(m)):
        if m[i]==" ":
            ch=m[a:i]
            if len(m2)!=0:
                m2=m2+" "
            a=i+1
            ch1=""
            for i in range(len(ch)):
                ch1=ch[i]+ch1
            m2=m2+ch1
    return m2
                
def verif(ch):
    i=0
    a=True
    while a==True and i<len(ch):
        if len(ch)==0:
            a=False
            w.res.setText("veuillez introduir une chane")
        elif ch[i]==" " and i!=len(ch)-1:
            if ch[i+1]==" ":
                a=False
                w.res.setText("entre deux mots un seul espace est autorisé")
        elif not("a"<=ch[i]<="z") and ch[i]!=" " :
            a=False
            w.res.setText("la chaine doit contient seulement des lettres alphabétiques en minuscule")
        i=i+1
    return a
def play():
    ch=w.texte.text()
    if 0<len(ch)<50 and verif(ch)==True:
        w.res.setText(Miroir(ch))

app = QApplication([])
w=loadUi ("InterfaceMiroirsMots.ui")
w.show()
w.btn.clicked.connect (play)
app.exec_()
