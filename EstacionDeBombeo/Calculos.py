import math
from sklearn import tree
import re

def disenio(DE,Wu,roo,mu,qo, h2, h1, g, Psal, Pll, lVal):

    #Usando la fórmula general para obtener el espesor

    a = 10.69
    b = -10.69*DE
    c = Wu

    t = (-b - math.sqrt((b**2)-4*a*c))/(2*a)

    #Obteniendo diámetro interior

    DI = DE - 2 * t

    qom = qo * 0.006624 #m^3/h

    qof = (qo * 5.615) / 86400 #ft^3/s

    gammao = roo / 62.43 

    NRe = 92.2 * ((gammao * qo) / (mu * DI))

    f = 64 / NRe

    A = ((math.pi * (DI ** 2) ) / 4) / (12 ** 2) #ft^2

    v = qof / A

    h2 = h2 * 3.281
    h1 = h1 * 3.281

    #P2 = Pll * 14.223
    #P1 = Psal * 14.223


    P2 = Pll * 14.223
    P = Psal *14.223

    L = lVal * 0.6214 #Conversión de km a mi

    g = g * 3.281

    P1 = P2 + (2.158 * (10 **(-4))) * roo * g * (h2 - h1) + 13.676 * f * roo * (v**2) * (L/(2*DI))
    
    print("t",t)
    print("DI", DI)
    print("NRe",NRe)
    print("f",f)
    #print(P1)
    print("P2",P2)
    print("ɣ",gammao)
    print("g")
    print("h2",h2)
    print("h1",h1)
    print("P1",P1)
    print("v",v)
    print("L",L)
    print("h2-h1",h2-h1)
    print("Psal",P)

    #pumpChoice(qom, P1, P)
    return qom, P1, P



def pumpChoice(qom, P1, P, qs):

    Datos = [[1.05,0],[3.35,1],[7,2],[13.35,3],[10.4,4],[26.75,5],[16.85,6],[31,7],[24.5,8],[69,9],[40.5,10],[87,11],[55,12],[38,13],[121,14]]
    bbas = ["021S01","038S04","038L01","045L01","063S02","063L01","076S01","090S01","090S03","090L01","105S01","105L01","125S01","125S03","125L01"]
    clasifica = tree.DecisionTreeClassifier()
    clasifica = clasifica.fit(Datos,bbas)
    #while True:
    qo = qom #float(input("Qo: "))
    qoap  = qs #int(input("Ingresa [0] si el Qo se aproxima a 1.05, [1] si se aproxima a 3.35, [2] a 7, [3] a 13.5, [4] a 10.4, [5] a 26.75, [6] a 16.85, [7] a 31, [8] a 24.5, [9] a 69, [10] a 40.5, [11] a 87, [12] a 55, [13] a 38, [14] a 121: "))
    bba = clasifica.predict([[qo,qoap]])
    #print("BBa: ", bba) #clasifica.predict([[qo,qoap]])) 

    if(re.search('125S01', str(bba))):

        m = (22 - 15) / (74 - 36)    
        Nprom = (22 + 15) / 2
        qoprom = (74 + 36) / 2
        b = Nprom - m * qoprom
        Nf = m * qom + b

        Pout = 61.2
        Pasp = 6.5

        dP = (Pout-Pasp) #*14.223 
        PP = ((dP)/10) * 14.223
        nBbas = round((P1 - P)/PP) #* 14.223

        Nneta = Nf * nBbas
        
        #print(PP)
        #print(P1)
        #print(P)
        
        #print(nBbas)

    elif (re.search('125S03', str(bba))):

        m = (60 - 37) / (60 - 16)
        Nprom = (60 + 37) / 2
        qoprom = (60 + 16) / 2
        b = Nprom - m * qoprom
        Nf = m * qom + b

        Pout = 183.5
        Pasp = 6.5
        
        dP = (Pout-Pasp) #*14.223 
        PP = ((dP)/10) * 14.223
        nBbas = round((P1 - P)/PP) #* 14.223
        Nneta = Nf * nBbas

    elif (re.search('125L01', str(bba))):
    
        m = (37 - 22) / (160 - 82)
        Nprom = (37 + 22) / 2
        qoprom = (160 + 82) / 2
        b = Nprom - m * qoprom
        Nf = m * qom + b

        Pout = 61.2
        Pasp = 6.5
        
        dP = (Pout-Pasp) #*14.223 
        PP = ((dP)/10) * 14.223
        nBbas = round((P1 - P)/PP) #* 14.223
        Nneta = Nf * nBbas

    elif (re.search('105L01', str(bba))):
    
        m = (37 - 22) / (119 - 55)
        Nprom = (37 + 22) / 2
        qoprom = (119 + 55) / 2
        b = Nprom - m * qoprom
        Nf = m * qom + b

        Pout = 61.2
        Pasp = 6.5
        
        dP = (Pout-Pasp) #*14.223 
        PP = ((dP)/10) * 14.223
        nBbas = round((P1 - P)/PP) #* 14.223
        Nneta = Nf * nBbas


    elif (re.search('105S01', str(bba))):
    
        m = (18.5 - 11) / (57 - 24)
        Nprom = (18.5 + 11) / 2
        qoprom = (57 + 24) / 2
        b = Nprom - m * qoprom
        Nf = m * qom + b

        Pout = 61.2
        Pasp = 6.5
        
        dP = (Pout-Pasp) #*14.223 
        PP = ((dP)/10) * 14.223
        nBbas = round((P1 - P)/PP) #* 14.223
        Nneta = Nf * nBbas

    elif (re.search('090L01', str(bba))):
    
        m = (30 - 11) / (106 - 32)
        Nprom = (30 + 11) / 2
        qoprom = (106 + 32) / 2
        b = Nprom - m * qoprom
        Nf = m * qom + b

        Pout = 61.2
        Pasp = 6.5
        
        dP = (Pout-Pasp) #*14.223 
        PP = ((dP)/10) * 14.223
        nBbas = round((P1 - P)/PP) #* 14.223
        Nneta = Nf * nBbas

    elif (re.search('090S03', str(bba))):
    
        m = (30 - 22) / (33 - 16)
        Nprom = (30 + 22) / 2
        qoprom = (33 + 16) / 2
        b = Nprom - m * qoprom
        Nf = m * qom + b

        Pout = 183.5
        Pasp = 6.5

    elif (re.search('090S01', str(bba))):
    
        m = (18.5 - 11) / (47 - 15)
        print("m: ", m)
        Nprom = (18.5 + 11) / 2
        qoprom = (47 + 15) / 2
        b = Nprom - m * qoprom
        Nf = m * qom + b

        Pout = 61.2
        Pasp = 6.5
        
        dP = (Pout-Pasp) #*14.223 
        PP = ((dP)/10) * 14.223
        nBbas = round((P1 - P)/PP) #* 14.223
        Nneta = Nf * nBbas
        
        dP = (Pout-Pasp) #*14.223 
        PP = ((dP)/10) * 14.223
        nBbas = round((P1 - P)/PP) #* 14.223
        Nneta = Nf * nBbas

    elif (re.search('076S01', str(bba))):
    
        m = (11 - 4) / (28.5 - 5.2)
        Nprom = (11 + 4) / 2
        qoprom = (28.5 + 5.2) / 2
        b = Nprom - m * qoprom
        Nf = m * qom + b

        Pout = 61.2
        Pasp = 6.5

        dP = (Pout-Pasp) #*14.223 
        PP = ((dP)/10) * 14.223
        nBbas = round((P1 - P)/PP) #* 14.223
        Nneta = Nf * nBbas

    elif (re.search('063L01', str(bba))):
    
        m = (11 - 4) / (40.5 - 13)
        Nprom = (11 + 4) / 2
        qoprom = (40.5 + 13) / 2
        b = Nprom - m * qoprom
        Nf = m * qom + b

        Pout = 61.2
        Pasp = 6.5
        
        dP = (Pout-Pasp) #*14.223 
        PP = ((dP)/10) * 14.223
        nBbas = round((P1 - P)/PP) #* 14.223
        Nneta = Nf * nBbas

    elif (re.search('063S02', str(bba))):
    
        m = (11 - 4) / (17.5 - 3.3)
        Nprom = (11 + 4) / 2
        qoprom = (17.5 + 3.3) / 2
        b = Nprom - m * qoprom
        Nf = m * qom + b

        Pout = 122.3
        Pasp = 6.5
        
        dP = (Pout-Pasp) #*14.223 
        PP = ((dP)/10) * 14.223
        nBbas = round((P1 - P)/PP) #* 14.223
        Nneta = Nf * nBbas

    elif (re.search('045L01', str(bba))):
    
        m = (5.5 - 3) / (18.6 - 8.1)
        Nprom = (5.5 + 3) / 2
        qoprom = (18.6 + 8.1) / 2
        b = Nprom - m * qoprom
        Nf = m * qom + b

        Pout = 61.2
        Pasp = 6.5
        
        dP = (Pout-Pasp) #*14.223 
        PP = ((dP)/10) * 14.223
        nBbas = round((P1 - P)/PP) #* 14.223
        Nneta = Nf * nBbas

    elif (re.search('038L01', str(bba))):
    
        m = (4 - 2.2) / (9.8 - 4.2)
        Nprom = (4 + 2.2) / 2
        qoprom = (9.8 + 4.2) / 2
        b = Nprom - m * qoprom
        Nf = m * qom + b

        Pout = 61.2
        Pasp = 6.5

        dP = (Pout-Pasp) #*14.223 
        PP = ((dP)/10) * 14.223
        nBbas = round((P1 - P)/PP) #* 14.223
        Nneta = Nf * nBbas

    elif (re.search('038S04', str(bba))):
    
        m = (7.5 - 5.5) / (4.7 - 2)
        Nprom = (7.5 + 5.5) / 2
        qoprom = (4.7 + 2) / 2
        b = Nprom - m * qoprom
        Nf = m * qom + b

        Pout = 244.6
        Pasp = 6.5
        
        dP = (Pout-Pasp) #*14.223 
        PP = ((dP)/10) * 14.223
        nBbas = round((P1 - P)/PP) #* 14.223
        Nneta = Nf * nBbas

    elif (re.search('021S01', str(bba))):
    
        m = (1.1 - 0.55) / (1.5 - 0.6)
        Nprom = (1.1 + 0.55) / 2
        qoprom = (1.5 + 0.6) / 2
        b = Nprom - m * qoprom
        Nf = m * qom + b

        Pout = 40.8
        Pasp = 6.5

        dP = (Pout-Pasp) #*14.223 
        PP = ((dP)/10) * 14.223
        nBbas = round((P1 - P)/PP) #* 14.223
        Nneta = Nf * nBbas
    
    print("m: ", m)  
    print("b:m*q+b ", b)  
    print("Qprom: ", qoprom)
    print("Nprom: ", Nprom)
    print("N=: ", Nf)
    print("Nn: ", Nneta)
    print("ΔP",dP)
    print("P(form.campo: ", PP)
    
    return Nneta, nBbas, PP, str(bba)

#disenio(6.625,53.78,58.8,286,5600,45.7,37.2,9.7683,3.16,9.28,5.472, 183.5, 6.5)
#disenio(28,302.56,54.0296,10.4,7500,229.2,12.2,9.77,2.53,5.6950,5.632)