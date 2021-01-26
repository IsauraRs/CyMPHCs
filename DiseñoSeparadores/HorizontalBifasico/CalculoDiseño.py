cdList = []
def restriccionCapacidad(gammam,rog,dm,mug, T, P, Z, qg ):

    rom = gammam * 62.43
    Cd = 0.34
    cdList.append(Cd)
    Vt = 0.0119 * (((rom - rog) / rog) * (dm/Cd)) ** 0.5
    Re = 0.0049 * ((rog*dm*Vt) / mug)
    Cd = (24 / Re) + (3 / (Re ** 0.5)) + 0.34
    cdList.append(Cd)

    ve = cdList[-1] - cdList[-2]
    '''print(rom)
    print(Re)
    print(Vt)
    print(Cd)
    print(ve)'''

    while ve > 0.00000000001:

        Vt = 0.0119 * (((rom - rog) / rog) * (dm/Cd)) ** 0.5
        Re = 0.0049 * ((rog*dm*Vt) / mug)
        Cd = (24 / Re) + (3 / (Re ** 0.5)) + 0.34
        cdList.append(Cd)

        ve = cdList[-1] - cdList[-2]
        '''print(Re)
        print(Vt)
        print(Cd)
        print(ve)'''

    #gas(T,P,Z,qg,rog,rom,Cd,dm)
    return T,P,Z,qg,rog,rom,Cd,dm

def gas(T,P,Z,qg,rog,rom, Cd,dm):

    d = 5
    #T = 
    #Leff = (420 * (((T*Z*qg) / P) * (rog / (rom - rog)) * (Cd/dm)) ** 0.5) / (d) #/12)
    Leff = (420 * (((T*Z*qg) / P)) * ((rog / (rom - rog)) * (Cd/dm)) ** 0.5) / (d)
    Lss = Leff + (d / 12)
    Re = Lss / (d / 12)

    counter = 0

    while Re > 3.51:
        
        #Leff = (420 * (((T*Z*qg) / P) * (rog / (rom - rog)) * (Cd/dm)) ** 0.5) / (d)# /12)
        Leff = (420 * (((T*Z*qg) / P)) * ((rog / (rom - rog)) * (Cd/dm)) ** 0.5) / (d)
        Lss = Leff + (d / 12)
        Re = Lss / (d/12)
        d += 0.01
        counter += 1
    
    print("Iteración: ", counter)
    print("Leff", Leff)
    print(Lss)
    print(Re)
    print(d)

    return Leff, Lss, Re, d

def liquido(gammam, ql, Leff):

    API = (141.5 / gammam) - 131.5
    vi = API
    d1 = 1

    if API >=20 or API <= 25:

        v1 = 25
        v2 = 20
        t1 = 3
        t2 = 4

        tr = t1 + ((t2-t1)/(v2-v1))*(vi-v1)
        #print(tr)
    
    elif API >=25 or API <= 30:
    
        v1 = 30
        v2 = 25
        t1 = 2
        t2 = 3

        tr = t1 + ((t2-t1)/(v2-v1))*(vi-v1)
        #print(tr)
    
    elif API >=30 or API <= 35:
    
        v1 = 35
        v2 = 30
        t1 = 1
        t2 = 2
       
        tr = t1 + ((t2-t1)/(v2-v1))*(vi-v1)
        #print(tr)

    Leffl = (tr * ql) / (0.7 * (d1**2))
    Lssl = (4 / 3) * Leffl
    Rel = Lssl / (d1 / 12)

    while Rel > 3.51:

        Leffl = (tr * ql) / (0.7 * (d1**2))
        Lssl = (4 / 3) * Leffl
        Rel = Lssl / (d1 / 12)
        d1 += 0.01

        '''
        print(Leffl)
        print(Lssl)
        print(Rel)'''

    if Leff > Leffl:

        #print("Leff: ", Leff)
        Leffinal = Leff 

    elif Leff < Leffl:

        #print("Leffl", Leffl)
        Leffinal = Leffl

    print(d1)
    print(Leffinal)
    
    return Leffl, Lssl, Rel, d1, Leffinal, tr




#restriccionCapacidad(0.94,0.135,67,0.02,610.7, 241.8, 0.83,7)
#liquido(28, 14174,6.17)
