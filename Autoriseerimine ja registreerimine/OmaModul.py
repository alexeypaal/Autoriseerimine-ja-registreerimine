from random import *
import string
def Parooli_muutmine(nimi, vana_salasõna, uus_salasõna, user_list):
    """
    Funktsioon muudab kasutaja parooli, kui vana parool klapib ja kasutaja on loendis.
    """
    for i, user in enumerate(user_list):
        if user[0] == nimi and user[1] == vana_salasõna:
            user_list[i] = (nimi, uus_salasõna)
            print("Parool muudetud edukalt.")
            return
    print("Parooli muutmine ebaõnnestus.")



def lähtestada_salasõna(nimi, user_list):
    """
    Funktsioon genereerib uue parooli ja asendab vana parooli kasutajanimi järgi, kui kasutaja on loendis.
    """
    for i, user in enumerate(user_list):
        if user[0] == nimi:
            uus_salasõna = "korova123"
            user_list[i] = (nimi, uus_salasõna)
            print("Uus parool genereeritud ja saadetud e-posti teel.")
            return
    print("Parooli taastamine ebaõnnestus.")



def Salasona(k: int):
    saladus=""
    for i in range(k):
        t=choice(string.ascii_letters) #Aa...Zz
        num=choice([1,2,3,4,5,6,7,8,9,0])
        sym=choice(["*","-",".","!","_"])
        t_num=[t,str(num),sym]
        saladus+=choice(t_num)
    return saladus

def Registreerimine(l:list,p:list):
    nimi=input("Sisesta oma nimi:")
    v=int(input("1-Ese koostan parooli\n2-Arvuti genireerib\n"))
    if v==1:
        pass
    else:
        salasona=Salasona(5)
        l.append(nimi)
        p.append(salasona)

    return l,p


def Autoriseerimine(l:list,p:list):
    nimi=input("Sisesta oma nimi:")
    salasona=input("Sisesta oma salasõna:")
    if nimi in l:
        ind=l.index(nimi)
        if salasona==p[ind]:
            print("Tere tulemast!")
        else:
            print("Vale salasõna!")
    else:
        print("Nimi ei ole nimekirjas!")





