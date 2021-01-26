from tkinter import *
from PIL import Image

from CalculoDiseñoTrifasico import Trifasico, dimCapacidadGas

class Data():

    def __init__(self):

        self.root = Tk()
        self.root.title("Separador trifásico horizontal")

        self.rog = StringVar()
        self.roo = StringVar()
        self.rw = StringVar()
        self.P = StringVar()
        self.qg = StringVar()
        self.ql = StringVar()
        self.pw = StringVar()
        self.T = StringVar()
        self.dmg = StringVar()
        self.mug = StringVar()
        self.muo = StringVar()
        self.dmw = StringVar()
        self.Z = StringVar()
        self.Awa = StringVar()
        self.ho = StringVar()
        self.tr = StringVar()
        self.Beta = StringVar()
        self.qo = StringVar()
        self.qw = StringVar()
        self.Vt = StringVar()
        self.dmax = StringVar()
        self.api = StringVar()
        self.Qo = StringVar()
        self.Qw = StringVar()


        self.cdR = StringVar()
        self.LeffR = StringVar()
        self.LssR = StringVar()
        self.ReR = StringVar()
        self.dR = StringVar()
        self.LefflR = StringVar()
        self.LsslR = StringVar()
        self.RelR = StringVar()
        self.dlR = StringVar()
        self.Lefffinal = StringVar()

        global roo, rw, dm, muo, P, qg, Beta,mug,qg,T,Z,P,rog,pw,ql, dmw
        
    
        def datos():

            global t, roo, rw, dm, muo, P, qg, Beta,mug,qg,T,Z,P,rog,pw,ql, dmw,qo,qw,api

            rog = float(self.rog.get())
            roo = float(self.roo.get())
            rw = float(self.rw.get())
            P = float(self.P.get())
            qg = float(self.qg.get())
            ql = float(self.ql.get())
            pw = float(self.pw.get())
            T = float(self.T.get())
            dm = float(self.dmg.get())
            mug = float(self.mug.get())
            muo = float(self.muo.get())
            dmw = float(self.dmw.get())
            Z = float(self.Z.get())
            qo = float(self.Qo.get())
            qw = float(self.Qw.get())
            api = float(self.api.get())

            t = Trifasico(roo, rw, dmw, muo, pw, ql, api, qo, qw)
            self.Awa.set(t[0])
            self.ho.set(t[1])
            self.tr.set(t[2])

        
        def dimensionamiento():

            Beta = float(self.Beta.get())
            
            cg = dimCapacidadGas(t[1],roo, t[2],mug,dm,qg,T,Z,P,rog,pw,ql,qo,qw, api, t[0],rw)

            self.cdR.set(cg[0])
            self.dmax.set(cg[1])
            self.qo.set(cg[2])
            self.qw.set(cg[3])
            self.Vt.set(cg[4])
            self.ReR.set(cg[5])
            self.LeffR.set(cg[6])
            self.LssR.set(cg[7])
            self.dR.set(cg[8])
            self.LefflR.set(cg[9])
            self.LsslR.set(cg[10])
            self.RelR.set(cg[11])
            self.dlR.set(cg[12])
            self.Lefffinal.set(cg[13])




        def bGraph():

            self.bG = Toplevel()
            self.bG.title("Gráfico de β")

            self.graph = PhotoImage(file = "BGraph.png")
            self.graph1 = Label(self.bG, image = self.graph)
            self.graph1.grid(column = 0, row = 0)


        rogLabel = Label(self.root, text = "ρg[lbm/ft^3]: ")
        rogLabel.grid(column = 0, row = 0)

        rogEntry = Entry(self.root)
        rogEntry.config(textvariable = self.rog)
        rogEntry.grid(column = 1, row = 0)

        rooLabel = Label(self.root, text = "ρo[lbm/ft^3]: ")
        rooLabel.grid(column = 0, row = 1)

        rooEntry = Entry(self.root)
        rooEntry.config(textvariable = self.roo)
        rooEntry.grid(column = 1, row = 1)

        rwLabel = Label(self.root, text = "ρw[lbm/ft^3]: ")
        rwLabel.grid(column = 0, row = 2)

        rwEntry = Entry(self.root)
        rwEntry.config(textvariable = self.rw)
        rwEntry.grid(column = 1, row = 2)

        dmLabel = Label(self.root, text = "dm(gas)[μm]: ")
        dmLabel.grid(column = 0, row = 3)

        dmEntry = Entry(self.root)
        dmEntry.config(textvariable = self.dmg)
        dmEntry.grid(column = 1, row = 3)

        mugLabel = Label(self.root, text = "μg[cP]: ")
        mugLabel.grid(column = 0, row = 4)

        mugEntry = Entry(self.root)
        mugEntry.config(textvariable = self.mug)
        mugEntry.grid(column = 1, row = 4)

        TLabel = Label(self.root, text = "T[R]: ")
        TLabel.grid(column = 0, row = 5)

        TEntry = Entry(self.root)
        TEntry.config(textvariable = self.T)
        TEntry.grid(column = 1, row = 5)

        PLabel = Label(self.root, text = "P[psi]: ")
        PLabel.grid(column = 0, row = 6)

        PEntry = Entry(self.root)
        PEntry.config(textvariable = self.P)
        PEntry.grid(column = 1, row = 6)

        ZLabel = Label(self.root, text = "Z: ")
        ZLabel.grid(column = 0, row = 7)

        ZEntry = Entry(self.root)
        ZEntry.config(textvariable = self.Z)
        ZEntry.grid(column = 1, row = 7)

        qgLabel = Label(self.root, text = "Qg[MMpcd]: ")
        qgLabel.grid(column = 0, row = 8)

        qgEntry = Entry(self.root)
        qgEntry.config(textvariable = self.qg)
        qgEntry.grid(column = 1, row = 8)

        qLabel = Label(self.root, text = "Ql[bpd]: ")
        qLabel.grid(column = 0, row = 9)

        qEntry = Entry(self.root)
        qEntry.config(textvariable = self.ql)
        qEntry.grid(column = 1, row = 9)

        pwLabel = Label(self.root, text = "Corte de agua[%]: ")
        pwLabel.grid(column = 0, row = 10)

        pwEntry = Entry(self.root)
        pwEntry.config(textvariable = self.pw)
        pwEntry.grid(column = 1, row = 10)

        muoLabel = Label(self.root, text = "μo[cP]")
        muoLabel.grid(column = 0, row = 11)

        muoEntry = Entry(self.root)
        muoEntry.config(textvariable = self.muo)
        muoEntry.grid(column = 1, row = 11)

        dmwLabel = Label(self.root, text = "dm(agua)[μm]: ")
        dmwLabel.grid(column = 0, row = 12)

        dmwEntry = Entry(self.root)
        dmwEntry.config(textvariable = self.dmw)
        dmwEntry.grid(column = 1, row = 12)

        apiLabel = Label(self.root, text = "°API: ")
        apiLabel.grid(column = 0, row = 13)

        apiEntry = Entry(self.root)
        apiEntry.config(textvariable = self.api)
        apiEntry.grid(column = 1, row = 13)

        qoiLabel = Label(self.root, text = "Qo[bpd]: ")
        qoiLabel.grid(column = 0, row = 14)

        qoiEntry = Entry(self.root)
        qoiEntry.config(textvariable = self.Qo)
        qoiEntry.grid(column = 1, row = 14)

        qwiLabel = Label(self.root, text = "Qw[bpd]: ")
        qwiLabel.grid(column = 0, row = 15)

        qwiEntry = Entry(self.root)
        qwiEntry.config(textvariable = self.Qw)
        qwiEntry.grid(column = 1, row = 15)



        cdLabel = Label(self.root, text = "CD: ")
        cdLabel.grid(column = 2, row = 0)

        cdRes = Label(self.root, textvariable = self.cdR)
        cdRes.grid(column = 3, row = 0)
        cdRes.config(bg = "firebrick1", font = ('Helvetica' , 16))

        LeffLabel = Label(self.root, text = "Leff(gas): ")
        LeffLabel.grid(column = 2, row = 1)

        LeffRes = Label(self.root, textvariable = self.LeffR)
        LeffRes.grid(column = 3, row = 1)
        LeffRes.config(bg = "firebrick1", font = ('Helvetica' , 16))

        LssLabel = Label(self.root, text = "Lss(gas): ")
        LssLabel.grid(column = 2, row = 2)

        LssRes = Label(self.root, textvariable = self.LssR)
        LssRes.grid(column = 3, row = 2)
        LssRes.config(bg = "firebrick1", font = ('Helvetica' , 16))

        ReRLabel = Label(self.root, text = "Re(gas): ")
        ReRLabel.grid(column = 2, row = 3)

        ReRes = Label(self.root, textvariable = self.ReR)
        ReRes.grid(column = 3, row = 3)
        ReRes.config(bg = "firebrick1", font = ('Helvetica' , 16))

        dLabel = Label(self.root, text = "d(gas): ")
        dLabel.grid(column = 2, row = 4)

        dRes = Label(self.root, textvariable = self.dR)
        dRes.grid(column = 3, row = 4)
        dRes.config(bg = "firebrick1", font = ('Helvetica' , 16))

        LefflLabel = Label(self.root, text = "Leff(tiempo de retención): ")
        LefflLabel.grid(column = 2, row = 5)

        LefflRes = Label(self.root, textvariable = self.LefflR)
        LefflRes.grid(column = 3, row = 5)
        LefflRes.config(bg = "firebrick1", font = ('Helvetica' , 16))

        LsslLabel = Label(self.root, text = "Lss(tiempo de retención): ")
        LsslLabel.grid(column = 2, row = 6)

        LsslRes = Label(self.root, textvariable = self.LsslR)
        LsslRes.grid(column = 3, row = 6)
        LsslRes.config(bg = "firebrick1", font = ('Helvetica' , 16))

        RelRLabel = Label(self.root, text = "Re(tiempo de retención): ")
        RelRLabel.grid(column = 2, row = 7)

        RelRes = Label(self.root, textvariable = self.RelR)
        RelRes.grid(column = 3, row = 7)
        RelRes.config(bg = "firebrick1", font = ('Helvetica' , 16))

        dlLabel = Label(self.root, text = "d(tiempo de retención): ")
        dlLabel.grid(column = 2, row = 8)

        dlRes = Label(self.root, textvariable = self.dlR)
        dlRes.grid(column = 3, row = 8)
        dlRes.config(bg = "firebrick1", font = ('Helvetica' , 16))

        LefnLabel = Label(self.root, text = "Leff_final: ")
        LefnLabel.grid(column = 2, row = 9)

        LefnRes = Label(self.root, textvariable = self.Lefffinal)
        LefnRes.grid(column = 3, row = 9)
        LefnRes.config(bg = "firebrick1", font = ('Helvetica' , 16))

        trLabel = Label(self.root, text = "Tiempo de retención: ")
        trLabel.grid(column = 2, row = 10)

        trRes = Label(self.root, textvariable= self.tr)
        trRes.grid(column = 3, row = 10)
        trRes.config(bg = "firebrick1", font = ('Helvetica' , 16))

        awaLabel = Label(self.root, text = "Aw/A: ")
        awaLabel.grid(column = 2, row = 11)

        awaRes = Label(self.root, textvariable = self.Awa)
        awaRes.grid(column = 3, row = 11)
        awaRes.config(bg = "firebrick1", font = ('Helvetica' , 16))

        hoLabel = Label(self.root, text = "ho: ")
        hoLabel.grid(column = 2, row = 12)

        hoRes = Label(self.root, textvariable = self.ho)
        hoRes.grid(column = 3, row = 12)
        hoRes.config(bg = "firebrick1", font = ('Helvetica' , 16))

        qoLabel = Label(self.root, text = "Qo[bpd]: ")
        qoLabel.grid(column = 2, row = 13)

        qoRes = Label(self.root, textvariable = self.qo)
        qoRes.grid(column = 3, row = 13)
        qoRes.config(bg = "firebrick1", font = ('Helvetica' , 16))

        qwLabel = Label(self.root, text = "Qw[bpd]: ")
        qwLabel.grid(column = 2, row = 14)

        qwRes = Label(self.root, textvariable = self.qw)
        qwRes.grid(column = 3, row = 14)
        qwRes.config(bg = "firebrick1", font = ('Helvetica' , 16))

        vtLabel = Label(self.root, text = "Vt: ")
        vtLabel.grid(column = 2, row = 15)

        vtRes = Label(self.root, textvariable = self.Vt)
        vtRes.grid(column = 3, row = 15)
        vtRes.config(bg = "firebrick1", font = ('Helvetica' , 16))

        dmaxLabel = Label(self.root, text = "dmáx: ")
        dmaxLabel.grid(column = 2, row = 16)

        dmaxRes = Label(self.root, textvariable = self.dmax)
        dmaxRes.grid(column = 3, row = 16)
        dmaxRes.config(bg = "firebrick1", font = ('Helvetica' , 16))

        BetaLabel = Label(self.root, text = "β: ")
        BetaLabel.grid(column = 0, row = 18)

        BetaEntry = Entry(self.root)
        BetaEntry.config(textvariable = self.Beta)
        BetaEntry.grid(column = 1, row = 18)



        selectButton = Button(self.root, text = "Calcular", command = datos)
        selectButton.grid(column = 1, row = 16)

        bGraphButton = Button(self.root, text = "Gráfico para β", command = bGraph)
        bGraphButton.grid(column = 1, row = 17)

        dimButton = Button(self.root, text = "Dimensionar", command = dimensionamiento)
        dimButton.grid(column = 0, row = 19)


        self.root.mainloop()

def main():
    Diseño = Data()

if __name__ == '__main__':
    main()

    

    






        



