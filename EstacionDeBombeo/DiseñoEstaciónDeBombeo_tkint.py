from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image

from Calculos import disenio as d
from Calculos import pumpChoice as pd

qoSel = ["[0] si el Qo se aproxima a 1.05","[1] si se aproxima a 3.35","[2] a 7",
"[3] a 13.5","[4] a 10.4","[5] a 26.75", "[6] a 16.85", "[7] a 31","[8] a 24.5",
"[9] a 69", "[10] a 40.5", "[11] a 87", "[12] a 55", "[13] a 38", "[14] a 121"]
class MainData():

    def __init__(self):

        self.root = Tk()
        self.root.title("Inicio")

        self.roo = StringVar()
        self.DE = StringVar()
        self.Wu = StringVar()
        self.g = StringVar()
        self.qo = StringVar()
        self.mu = StringVar()
        self.l = StringVar()
        self.Psal = StringVar()
        self.h2 = StringVar()
        self.h1 = StringVar()
        self.Pllegada = StringVar()
        self.qom = StringVar()
        self.nbba = StringVar()
        self.bbaMod = StringVar()
        self.Nnet = StringVar()

        frm = Frame(self.root)
        scroll = Scrollbar(self.root , orient = VERTICAL)

        listbox = Listbox(self.root, yscrollcommand = scroll.set, selectmode = MULTIPLE) #,selectmode = 'multiple',exportselection=0, cursor = 'man', selectforeground = 'red')
        scroll.config(command = listbox.yview)
        #scroll.pack(side = RIGHT, fill = Y) 
        scroll.grid(column = 4, row = 2)
        #listbox.pack()
        listbox.grid(column = 3, row = 2)

        for i in range(len(qoSel)):
            listbox.insert(END , qoSel[i])

        def dataGather():

            global m

            rooVal = float(self.roo.get())
            DEVal = float(self.DE.get())
            WuVal = float(self.Wu.get())
            muVal = float(self.mu.get())
            qoVal = float(self.qo.get())
            gVal = float(self.g.get())
            lVal = float(self.l.get())
            PsalVal = float(self.Psal.get())
            h2Val = float(self.h2.get())
            h1Val = float(self.h1.get())
            PllegadaVal = float(self.Pllegada.get())

            m = d(DEVal,WuVal, rooVal, muVal, qoVal, h2Val, h1Val, gVal, PsalVal, PllegadaVal, lVal)

            print("m0: ", m[0])
            self.qom.set(m[0])

        def selectQ():
    
            global qop, r

            resul = ''

            for g in listbox.curselection():
                resul += str(listbox.get(g))
                qop = qoSel.index(resul)
                print("Resul",qop)

            r = pd(m[0], m[1], m[2], qop)
            print(r)
            self.Nnet.set(r[0])
            self.nbba.set(r[1])
            self.bbaMod.set(r[3])

        def catalogo():
            self.cb = Toplevel()
            self.cb.title("Catálogo de bombas")

            self.cat = PhotoImage(file = "catalogoBbas.png")
            self.catal = Label(self.cb, image = self.cat)
            self.catal.grid(column = 0, row = 0)

        catalogueButton = Button(self.root, text = "Catálogo de bombas", command = catalogo)
        catalogueButton.grid(column = 0, row = 12)


        qSButton = Button(self.root, text = "Seleccionar", command = selectQ )
        qSButton.grid(column = 3, row = 3)


        rooLabel = Label(self.root, text = "ρo[lbm/ft^3]: ")
        rooLabel.grid(column = 0, row = 0)

        rooEntry = Entry(self.root)
        rooEntry.config(textvariable = self.roo)
        rooEntry.grid(column = 1, row = 0)

        DELabel = Label(self.root, text = "Diámetro externo[in]: ")
        DELabel.grid(column = 0, row = 1)

        DEEntry = Entry(self.root)
        DEEntry.config(textvariable = self.DE)
        DEEntry.grid(column = 1, row = 1)

        WuLabel = Label(self.root, text = "Libraje: ")
        WuLabel.grid(column = 0, row = 2)

        WuEntry = Entry(self.root)
        WuEntry.config(textvariable = self.Wu)
        WuEntry.grid(column = 1, row = 2)

        qoLabel = Label(self.root, text = "Qo[bpd]: ")
        qoLabel.grid(column = 0, row = 3)

        qoEntry = Entry(self.root)
        qoEntry.config(textvariable = self.qo)
        qoEntry.grid(column = 1, row = 3)

        lLabel = Label(self.root, text = "L[km]: ")
        lLabel.grid(column = 0, row = 4)

        lEntry = Entry(self.root)
        lEntry.config(textvariable = self.l)
        lEntry.grid(column = 1, row = 4)

        gLabel = Label(self.root, text = "g[m/s^2]: ")
        gLabel.grid(column = 0, row = 5)

        gEntry = Entry(self.root)
        gEntry.config(textvariable = self.g)
        gEntry.grid(column = 1, row = 5)

        muLabel = Label(self.root, text = "μ[cP]: ")
        muLabel.grid(column = 0, row = 6)

        muEntry = Entry(self.root)
        muEntry.config(textvariable = self.mu)
        muEntry.grid(column = 1, row = 6)

        PsalLabel = Label(self.root, text = "Psalida[kg/cm^2]: ")
        PsalLabel.grid(column = 0, row = 7)

        PsalEntry = Entry(self.root)
        PsalEntry.config(textvariable = self.Psal)
        PsalEntry.grid(column = 1, row = 7)

        PllLabel = Label(self.root, text = "Pllegada[kg/cm^2]: ")
        PllLabel.grid(column = 0, row = 8)

        PllEntry = Entry(self.root)
        PllEntry.config(textvariable = self.Pllegada)
        PllEntry.grid(column = 1, row = 8)

        h1Label = Label(self.root, text = "Elevación inicial al N.M[m]: ")
        h1Label.grid(column = 0, row = 9)

        h1Entry = Entry(self.root)
        h1Entry.config(textvariable = self.h1)
        h1Entry.grid(column = 1, row = 9)

        h2Label = Label(self.root, text = "Elevación final al N.M[m]: ")
        h2Label.grid(column = 0, row = 10)

        h2Entry = Entry(self.root)
        h2Entry.config(textvariable = self.h2)
        h2Entry.grid(column = 1, row = 10)

        qomflag = Label(self.root, text = "Qo[m^3/h]: ")
        qomflag.grid(column = 3, row = 0)

        qomLabel = Label(self.root, textvariable = self.qom)
        qomLabel.grid(column = 4, row = 0)
        qomLabel.config(bg = "firebrick1", font = ('Helvetica' , 16))

        selLabel = Label(self.root, text = "Seleccione el gasto más próximo: ")
        selLabel.grid(column = 3, row = 1)

        sendButton = Button(self.root, text = "Calcular", command = dataGather)
        sendButton.grid(column = 0, row = 11)

        modelLabel = Label(self.root, text = "Modelo: ")
        modelLabel.grid(column = 3, row = 4)

        modelSet = Label(self.root, textvariable = self.bbaMod)
        modelSet.grid(column = 4, row = 4)
        modelSet.config(bg = "firebrick1", font = ('Helvetica' , 16))

        nbaLabel = Label(self.root, text = "Número de bombas: ")
        nbaLabel.grid(column = 3, row = 5)

        nbaSet = Label(self.root, textvariable = self.nbba)
        nbaSet.grid(column = 4, row = 5)
        nbaSet.config(bg = "firebrick1", font = ('Helvetica' , 16))

        nnetaLabel = Label(self.root, text = "N neta[kW]: ")
        nnetaLabel.grid(column = 3, row = 6)

        nnetaSet = Label(self.root, textvariable = self.Nnet)
        nnetaSet.grid(column = 4, row = 6)
        nnetaSet.config(bg = "firebrick1", font = ('Helvetica' , 16))

        self.root.mainloop()

def main():

    Disenio = MainData()

if __name__ == '__main__':
    main()

    

