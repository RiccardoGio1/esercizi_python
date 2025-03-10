import random 
#Punto 1
lista1=[("antipasti",(8,7,9),"Junior Chef"),("primi",(7,8,8),"Junior Chef"),("secondi",(9,9,8),"Junior Chef"),("dessert",(8,8,9),"Junior Chef")]
lista2=[("antipasti",(7,7,8),"Senior Chef"),("primi",(8,9,7),"Senior Chef"),("secondi",(7,8,7),"Senior Chef"),("dessert",(9,8,8),"Senior Chef")]
lista3=[("antipasti",(9,8,8),"Junior Chef"),("primi",(8,7,9),"Junior Chef"),("secondi",(8,8,8),"Junior Chef"),("dessert",(7,9,8),"Junior Chef")]

dizionario={
    "Mario Rossi":lista1,
    "Luigi Bianchi":lista2,
    "Giulia Verdi":lista3
}

print(dizionario)

#Punto 2
gusto=11%10
lista4=[("antipasti",(9,gusto,8),"Senior Chef"),("primi",(8,7,9),"Senior Chef"),("secondi",(8,8,8),"Senior Chef"),("dessert",(7,9,8),"Senior Chef")]
dizionario["Riccardo Giovenzana"]=lista4

#print(dizionario)

#Punto 3
def aggiungiCategoria():
    #lista1=[]
    tuplaX=()
    for nome,lista in dizionario.items():
            for tipologia,voti,categoria in lista:
                n1=random.randint(1,10)
                n2=random.randint(1,10)
                n3=random.randint(1,10)
                tupla=(n1,n2,n3)

                if(categoria=="Junior Chef"):
                    tuplaX=(("piatti unici",(tupla),"Junior Chef"))

                if(categoria=="Senior Chef"):
                    tuplaX=(("piatti unici",(tupla),"Senior Chef"))
            print(tuplaX)           
            dizionario[nome]=tuplaX
    print(dizionario)
aggiungiCategoria()


#Punto 4
def stampaDati(nomeCompleto):
    if(nomeCompleto in dizionario.keys()):
        for nome,lista in dizionario.items():
            if(nomeCompleto == nome):      
                for categoriaPiatto,punti,categoriaChef in lista:
                        print(f"Categoria di Chef: {categoriaChef}")
                        print(f"Nome e Cognome: {nome}")
                        print(f"Punteggi {categoriaPiatto}:")
                        print(f"Creatività: {punti[0]}")
                        print(f"Gusto: {punti[1]}")
                        print(f"Presentazione: {punti[2]}")
    else:
        print("Chef NON trovato")
        
nome=str(input("Inserisci il nome dello chef: "))
cognome=str(input("Inserisci il cognome dello chef: "))

nomeCompleto = nome+" "+cognome
stampaDati(nomeCompleto)


#Punto 5
def stampaPiatto(categoriaP):
    for nome,lista in dizionario.items():
        for categoriaPiatto,punti,categoriaChef in lista:
            if(categoriaP==categoriaPiatto):
                print(f"Categoria Piatto: {categoriaPiatto}")
                print(f"Chef: {nome}")
                print(f"Creatività: {punti[0]}")
                print(f"Gusto: {punti[1]}")
                print(f"Presentazione: {punti[2]}")


categoriaP=str(input("Inserisci la categoria del piatto: "))
stampaPiatto(categoriaP)

#Punto 7
def inserisci_dati_nuovo_chef():
    tuplaVoti=()
    lista=[]
    nome=str(input("Inserisci il nome dello chef: "))
    cognome=str(input("Inserisci il cognome dello chef: "))

    while(nome+ " "+cognome in dizionario.keys()):
        print("Errore - REINSERISCI")
        nome=str(input("Inserisci il nome dello chef: "))
        cognome=str(input("Inserisci il cognome dello chef: "))
        

    for i in range (0,5):

        categoriaP=str(input("Insersci la tipologia del piatto: "))

        votoC=int(input("Inserisci il voto della creatività: "))

        while(votoC<=0 or votoC>10):
            votoC=int(input("Errore, Reinserisci il voto della creatività"))

        votoG=int(input("Inserisci il voto del gusto: "))
        while(votoG<=0 or votoG>10):
            votoG=int(input("Errore, Reinserisci il voto del gusto"))

        votoP=int(input("Inserisci il voto della presentazione: "))
        while(votoP<=0 or votoP>10):
            votoP=int(input("Errore, Reinserisci il voto della presentazione"))

        tuplaVoti=(votoC,votoG,votoP)
        
        categoriaChef=str(input("Insersci la categoria dello chef: "))

        tupla1=(categoriaP,tuplaVoti,categoriaChef)
        lista.append(tupla1)

        dizionario[nome+" "+cognome]=lista
    print(dizionario)
    
inserisci_dati_nuovo_chef()  


"""
Correzione:
punto 3: al posto di utilizzare categoria ho utilizzato tipologia
punto 4: mancante l'if che controlla la tipologia del piatto
punto 6 (A-B): non fatti
"""