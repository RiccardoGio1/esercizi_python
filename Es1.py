dati_pioggia = (
    ("bergamo",[("gennaio",12),("febbraio",10),("marzo",4),("aprile",8),("dicembre",4)]),
    ("brescia",[("gennaio",9),("febbraio",10),("maggio",9),("aprile",13),("novembre",6)]),
    ("como",[("gennaio",12),("febbraio",10),("agosto",5),("aprile",12),("settembre",7)])
    )

def calcola(cerca):
    somma=0
    conta=0
    meseMax=[]
    meseMin=[]
    valoreMax=0
    valoreMin=1000
    for citta, rilevazioni in dati_pioggia:  
        if(citta==cerca):
            for mese,numero in rilevazioni:
                somma=somma+numero
                conta+=1
                if(numero=="N/D"):
                    conta-=1
                    somma=somma+0

                if(numero>valoreMax):
                    valoreMax=numero
                if(numero<valoreMin):
                    valoreMin=numero   

    for citta, rilevazioni in dati_pioggia:  
        if(citta==cerca):
            for mese,numero in rilevazioni:
                if(numero==valoreMax):
                    meseMax.append(mese)
                if(numero==valoreMin):
                    meseMin.append(mese)

    media=somma/conta
    return(media,(valoreMax,meseMax),(valoreMin,meseMin))
            
cerca=str(input("Inserisci il nome della città per misurare i dati pluviometrici:"))
dati=calcola(cerca)
print(f"Media per la citta {dati[0]}")
print(f"massima raggiunta nei mesi {dati[1][1]} con valore {dati[1][0]}")
print(f"minima raggiunta nei mesi {dati[2][1]} con valore {dati[2][0]}")
    