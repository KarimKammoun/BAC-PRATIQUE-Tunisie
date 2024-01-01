from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from numpy import*

def trie(ch):
    t=array([int()]*(len(ch)))
    for i in range(len(ch)):
        t[i]=int(ch[i])
    for i in range(len(ch)-1):
        for j in range(len(ch)-1):
            if t[j]>t[j+1]:
                t[j],t[j+1]=t[j+1],t[j]
    ch1=""
    for i in range(len(ch)):
        ch1=ch1+str(t[i])
    return ch1
    

def verifier(a,b):
    ch=trie(str(a)+str(b))
    a=True
    i=0
    b=1
    while a==True and i<len(ch)-1:
        if not(int(ch[i])+b==int(ch[i+1])):
            a=False
        i=i+1
    return a
    
    
    
def play():
    M=int(w.texte1.text())
    N=int(w.texte2.text())
    if not(N>=0 and M>=0):
        w.res.setText("veullez introduire deux entier positifs !")
    else:
        a=verifier(N,M)
        if a==True: 
            w.res.setText(str(M)+" et "+str(N)+" forment une succssetion parfaite")
        else:
            w.res.setText(str(M)+" et "+str(N)+" ne forment pas une succssetion parfaite")

app=QApplication([])
w=loadUi("InterfaceSuccession.ui")
w.show()
w.btn.clicked.connect(play)
app.exec_()