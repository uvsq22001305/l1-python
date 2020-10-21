def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    jts = temps[0] * 86400
    hts = temps[1] * 3600
    mts = temps[2] * 60
    return jts + hts + mts +temps[3]

temps = (3 ,23 ,1 ,34)
print(type(temps))
print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    stj = seconde // 84600
    sth = seconde // 3600 % 24
    stm = seconde // 60 % 60
    return stj, sth, stm, seconde%60


def strJour(temps):
    if temps[0] == 0 :
        return " "
    elif temps[0] == 1:
        return "un jour"
    else:
        return str(temps[0]) + " jours"

def strHeure(temps):
    if temps[1] == 0 :
        return " "
    elif temps[1] == 1:
        return " , une heure"
    else:
        return ", " + str(temps[1]) + " heures"

def strminute(temps):
    if temps[2] == 0 :
        return " "
    elif temps[2] == 1:
        return " , une minute"
    else:
        return ", " + str(temps[2]) + " minutes"

def strseconde(temps):
    if temps[3] == 0 :
        return " "
    elif temps[3] == 1:
        return " , une seconde "
    else:
        return ", " + str(temps[3]) + " secondes"


def afficheTemps(temps):
    print(strJour(temps) + strHeure(temps) + strminute(temps) + strseconde(temps))


def demandeTemps():
    jour = int(input("définir un nombre de jours"))
    heure = int(input("définir un nombre  d'heures"))
    minute = int(input("définir un nombre de minutes"))
    seconde = int(input("définir un nombre de secondes"))

    while(jour< 0):
        jour = int(input("le nombre de jours défini est incorecte , redéfinir un nombre de jours"))
    
    while(heure < 0 or heure >= 24):
        hour = int(input(" l'heure ,défini est incorecte , redéfinir un nombre d'heures "))
    
    while(minute < 0 or minute >=60):
        minute = int(input(" les minutes définis sont incorecte , redéfinir un nombre de minutes"))
    
    while(seconde < 0  or seconde >=60):
        seconde = int(input(" les secondes définis est incorecte , redéfinir un nombre de secondes"))
    return(jour, heure, minute, seconde)

def sommeTemps(temps1,temps2):
    res = [0,0,0,0]
    for i in range(0, 4):
        res[i] = temps1[i] + temps2[i]

    if(res[3] >= 60):
        res[2] += res[3]//60
        res[3] %= 60
    if(res[2]   >= 60):
        res[1] += res[2]//60
        res[2] %= 60
    if(res[1] >=  24):
        res[0] += res[1]//24
        res[1] %= 24
    return res


