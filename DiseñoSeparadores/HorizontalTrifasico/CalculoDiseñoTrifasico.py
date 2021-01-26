cdList = []
def Trifasico(roo, rw, dmw ,muo, pw, ql, api, qo, qw):

    if roo == 0:

        gammao = 141.5 / (131.5 + api)
        roo = gammao * 62.43

    else:
        gammao = roo / 62.43

    gammaw = rw / 62.43

    if api == 0:
        
        API = (141.5 / gammao) - 131.5

    else:
        API = api

    vi = API

    if API >=30 or API <= 40:
    
        v1 = 40
        v2 = 30
        t1 = 5
        t2 = 7.5

        tr = t1 + ((t2-t1)/(v2-v1))*(vi-v1)
        #print(tr)
    
    elif API >=20 or API <= 30:
    
        v1 = 30
        v2 = 20
        t1 = 7.5
        t2 = 10

        tr = t1 + ((t2-t1)/(v2-v1))*(vi-v1)

    elif API >=10 or API <= 20:

        v1 = 20
        v2 = 10
        t1 = 10
        t2 = 12.5

        tr = t1 + ((t2-t1)/(v2-v1))*(vi-v1)

    elif API >=40 or API <= 50:
        
        v1 = 50
        v2 = 40
        t1 = 2
        t2 = 5

        tr = t1 + ((t2-t1)/(v2-v1))*(vi-v1)

    dSG = abs(gammao - gammaw)

    if pw != 0:
        
        qw = (pw * ql) / 100
        qo = ql - qw
    
    else:

        qw = qw
        qo = qo
    
    ho = (0.00128 * tr * dSG * (dmw**2)) / muo

    AwA = 0.5 * ((qw * tr) / (tr * qo + tr * qw))

    return AwA, ho, tr

def dimCapacidadGas(ho, roo, tr, mug, dm, qg, T, Z, P, rog, pw, ql,qo,qw, api, AwA, rw):
    #Beta, ho, roo, tr, mug, dm, qg, T, Z, P, rog, pw, ql,qo,qw, api
    Beta = 0.8214 * (AwA**2) - (1.3879 * AwA) + 0.495
    dmax = ho / Beta

    if roo == 0:

        gammao = 141.5 / (131.5 + api)
        roo = gammao * 62.43
    
    else:

        roo = roo
        gammao = roo / 62.43

    gammaw = rw / 62.43

    #rom = roo
    if pw != 0:
        
        qw = (pw * ql) / 100
        qo = ql - qw
    
    else:
        qo = qo
        qw  = qw
        pw = (qw * 100) / (qo + qw) 

    gammam = (gammao * ((100 - pw) / 100)) + ((gammaw * pw / 100))
    rom = gammam * 62.43
    print("rom: ", rom)


    #Coeficiente de arrastre por método iterativo
    
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

    d = dmax

    Leff = (420 * (((T*Z*qg) / P)) * ((rog / (rom - rog)) * (Cd/dm)) ** 0.5) / (d)
    Lss = Leff + (d / 12)
    Red = Lss / (d/12)

    while Red < 3.51:
        
        Leff = (420 * (((T*Z*qg) / P)) * ((rog / (rom - rog)) * (Cd/dm)) ** 0.5) / (d)
        Lss = Leff + (d / 12)
        Red = Lss / (d/12)
        d -= 0.01
    
    '''else:

        if Red < 3.5:

            while Red < 3.5:

                Leff = (420 * (((T*Z*qg) / P)) * ((rog / (rom - rog)) * (Cd/dm)) ** 0.5) / (d)
                Lss = Leff + (d / 12)
                Red = Lss / (d/12)
                d += 0.0001
    '''

    #Dimensionamiento por tiempo de retención

    d1 = dmax
    Leffr = (1.42 * ((qw * tr) + (qo * tr))) / (d1**2)
    Lssr = (4 / 3) * Leffr
    Rer = Lssr / (d1 / 12)

    while Rer < 3.51:

        Leffr = (1.42 * ((qw * tr) + (qo * tr))) / (d1**2)
        Lssr = (4 / 3) * Leffr
        Rer = Lssr / (d1 / 12)
        d1 -= 0.01

    '''else:
        if Rer < 3.5:
            while Rer < 3.5:

                Leffr = (1.42 * ((qw * tr) + (qo * tr))) / (d1**2)
                Lssr = (4 / 3) * Leffr
                Rer = Lssr / (d1 / 12)
                d1 += 0.0001
    '''


    if Leff > Leffr:

        Leffg = Leff

    else:

        Leffg = Leffr

    print("Cd: ", Cd)
    print("dmax: ", dmax)
    print("qo:", qo)
    print("qw", qw)
    print("Vt", Vt)
    print("Reg", Red)
    print("Leffg", Leff)
    print("Lssg", Lss)
    print("dg", d)
    print("Leffr", Leffr)
    print("Lssr", Lssr)
    print("Rer", Rer)
    print("dr: ", d1)
    print("Leffin", Leffg)


    return Cd, dmax, qo, qw, Vt, Red, Leff, Lss, d, Leffr, Lssr, Rer, d1, Leffg 


#dimCapacidadGas(0.33,26.11,56.19,8.6,0.02,120,20,610.6,0.83,121.32,0.094,26,7600,0,0,0)






