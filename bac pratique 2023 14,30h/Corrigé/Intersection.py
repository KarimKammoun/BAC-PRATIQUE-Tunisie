from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication 

def recherche(ch1,ch2):
    res=""
    for i in range(len(ch1)):
        if ch2.find(ch1[i])!=0 and res.find(ch1[i])==-1:
            res=res+ch1[i]
    return res
def play():
    ch1=f.text1.text()
    ch2=f.text2.text()
    if 1<=len(ch1)<30 and ch1.lower()==ch1 and 1<=len(ch2)<30 and ch2.lower()==ch2:
        f.res.setText(recherche(ch1,ch2))
    elif len(ch1)==0 or len(ch2)==0:
        f.res.setText("veuillez introduire deux chaine non vide")
    elif len(ch1)>30 or len(ch2)>30:
        f.res.setText("veuillez introduire deux chaine de longueurs inferieures à 30 ")
    elif ch1.lower()!=ch1 or ch2.lower()!=ch2:
        f.res.setText("veuillez introduire deux chaine valide")
    else:
        a=recherche(ch1,ch2)
        f.res.setText(a)

app=QApplication([])
f=loadUi("InterfaceIntersection.ui")
f.show()
f.bnt.clicked.connect(play)
app.exec()