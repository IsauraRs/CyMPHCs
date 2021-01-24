from tkinter import *

from CalculoDiseño import restriccionCapacidad, gas, liquido

class IngresoDatos():

    def __init__(self):

        self.root = Tk()
        self.root.title("Separador bifásico horizontal")

        self.rog = StringVar()
        self.gammam = StringVar()
        self.dm = StringVar()
        self.mug = StringVar()
        self.T = StringVar()
        self.P = StringVar()
        self.Z = StringVar()
        self.qg = StringVar()
        self.qm = StringVar()
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
        self.tr = StringVar()



        def data():

            rog = float(self.rog.get())
            gammam = float(self.gammam.get())
            dm = float(self.dm.get())
            mug = float(self.mug.get())
            T = float(self.T.get())
            P = float(self.P.get())
            Z = float(self.Z.get())
            qg = float(self.qg.get())
            qm = float(self.qm.get())

            rc = restriccionCapacidad(gammam,rog,dm,mug,T,P,Z,qg)
            g = gas(rc[0],rc[1],rc[2],rc[3],rc[4],rc[5],rc[6],rc[7])
            self.cdR.set(rc[6])
            self.LeffR.set(g[0])
            self.LssR.set(g[1])
            self.ReR.set(g[2])
            self.dR.set(g[3])
            l = liquido(gammam,qm,g[0])
            self.LefflR.set(l[0])
            self.LsslR.set(l[1])
            self.RelR.set(l[2])
            self.dlR.set(l[3])
            self.Lefffinal.set(l[4])
            self.tr.set(l[5])

        rogLabel = Label(self.root, text = "ρg[lbm/ft^3]: ")
        rogLabel.grid(column = 0, row = 0)

        rogEntry = Entry(self.root)
        rogEntry.config(textvariable = self.rog)
        rogEntry.grid(column = 1, row = 0)

        gammamLabel = Label(self.root, text = "ɣm: ")
        gammamLabel.grid(column = 0, row = 1)

        gammamEntry = Entry(self.root)
        gammamEntry.config(textvariable = self.gammam)
        gammamEntry.grid(column = 1, row = 1)

        dmLabel = Label(self.root, text = "dm[μm]: ")
        dmLabel.grid(column = 0, row = 2)

        dmEntry = Entry(self.root)
        dmEntry.config(textvariable = self.dm)
        dmEntry.grid(column = 1, row = 2)

        mugLabel = Label(self.root, text = "μg[cP]: ")
        mugLabel.grid(column = 0, row = 3)

        mugEntry = Entry(self.root)
        mugEntry.config(textvariable = self.mug)
        mugEntry.grid(column = 1, row = 3)

        TLabel = Label(self.root, text = "T[R]: ")
        TLabel.grid(column = 0, row = 4)

        TEntry = Entry(self.root)
        TEntry.config(textvariable = self.T)
        TEntry.grid(column = 1, row = 4)

        PLabel = Label(self.root, text = "P[psi]: ")
        PLabel.grid(column = 0, row = 5)

        PEntry = Entry(self.root)
        PEntry.config(textvariable = self.P)
        PEntry.grid(column = 1, row = 5)

        ZLabel = Label(self.root, text = "Z: ")
        ZLabel.grid(column = 0, row = 6)

        ZEntry = Entry(self.root)
        ZEntry.config(textvariable = self.Z)
        ZEntry.grid(column = 1, row = 6)

        qgLabel = Label(self.root, text = "Qg[MMpcd]: ")
        qgLabel.grid(column = 0, row = 7)

        qgEntry = Entry(self.root)
        qgEntry.config(textvariable = self.qg)
        qgEntry.grid(column = 1, row = 7)

        qLabel = Label(self.root, text = "Qm[bpd]")
        qLabel.grid(column = 0, row = 8)

        qEntry = Entry(self.root)
        qEntry.config(textvariable = self.qm)
        qEntry.grid(column = 1, row = 8)


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

        LefflLabel = Label(self.root, text = "Leff(líquido): ")
        LefflLabel.grid(column = 2, row = 5)

        LefflRes = Label(self.root, textvariable = self.LefflR)
        LefflRes.grid(column = 3, row = 5)
        LefflRes.config(bg = "firebrick1", font = ('Helvetica' , 16))

        LsslLabel = Label(self.root, text = "Lss(líquido): ")
        LsslLabel.grid(column = 2, row = 6)

        LsslRes = Label(self.root, textvariable = self.LsslR)
        LsslRes.grid(column = 3, row = 6)
        LsslRes.config(bg = "firebrick1", font = ('Helvetica' , 16))

        RelRLabel = Label(self.root, text = "Re(líquido): ")
        RelRLabel.grid(column = 2, row = 7)

        RelRes = Label(self.root, textvariable = self.ReR)
        RelRes.grid(column = 3, row = 7)
        RelRes.config(bg = "firebrick1", font = ('Helvetica' , 16))

        dlLabel = Label(self.root, text = "d(líquido): ")
        dlLabel.grid(column = 2, row = 8)

        dlRes = Label(self.root, textvariable = self.dR)
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

        selectButton = Button(self.root, text = "Calcular", command = data)
        selectButton.grid(column = 0, row = 9)

        self.root.mainloop()

def main():

    HB = IngresoDatos()

if __name__ == '__main__':
    main()