from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication

def Miroir(ch):
    ch1=""
    for i in range(len(ch)):
        ch1=ch[i]+ch1
    return ch1
def Rotation(ch):
    res=""
    for i in range(len(ch)):
        res=res+chr(97+(ord(ch[i])-97+13)%26)
    return res
def verif (ch):
    a=True
    i=0
    while a==True and i<len(ch):
        if not("a"<=ch[i]<="z"):
            a=False
        i=i+1
    return a 
def play():
    ch=w.texte.text()
    if len(ch)==0:
        w.res.setText("veullez introduire une chaine")
    elif len(ch)>=10:
        w.res.setText("veullez introduire une chaine valide")
    elif verif(ch)==False:
        w.res.setText("veullez introduire une chaine valide")
    else:
        ch1=Rotation(ch)
        ch2=Miroir(ch1)
        w.res.setText("la chane crypteé est : "+ch2)

app=QApplication([])
w=loadUi("InterfaceRotationMiroir.ui")
w.show()
w.btn.clicked.connect(play)
app.exec_()

