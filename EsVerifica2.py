#Riccardo Giovenzana

tupla_consumi_energetici = (
    ("Milano", [("gennaio", ("elettrico", 300)),("gennaio", ("gas", 150)),
        ("febbraio", ("elettrico", 280)),("febbraio", ("gas", 120)),  
        ("marzo", ("elettrico", 190)),("marzo", ("gas", 240)),
        ("aprile", ("elettrico", 170)),("aprile", ("gas", 320)) 
    ]),

    ("Brescia", [("gennaio", ("elettrico", 280)),("gennaio", ("gas", 140)),
        ("febbraio", ("elettrico", 260)),("febbraio", ("gas", 130)),
        ("marzo", ("elettrico", 160)),("marzo", ("gas", 250)),
        ("aprile", ("elettrico", 180)),("aprile", ("gas", 165)) 
    ]),

    ("Vittuone", [("gennaio", ("elettrico", 500)),("gennaio", ("gas", 340)),
        ("febbraio", ("elettrico", 145)),("febbraio", ("gas", 245)),
        ("marzo", ("elettrico", 130)),("marzo", ("gas", 120)),
        ("aprile", ("elettrico", 120)),("aprile", ("gas", 195)) 
    ])
)

def analizza_consumi_energetici(cerca,nome):
    somma=0
    conta=0
    max_risorsa=0
    mese_max_risorsa=[]
    for tuplina in tupla_consumi_energetici:  #Tupla
        for citta,*resto in tupla_consumi_energetici:  #Milano, resto
            if(citta==cerca):
                for tupla in resto:  #(mese,("elettrico", 300))
                    for mese,*rilevazione in tupla:   #gennaio
                        for tipoC, consumo in  rilevazione:  #elettrico , 300
                            if(tipoC==nome):
                                somma=somma+consumo
                                conta=conta+1
                                if(consumo>max_risorsa):
                                    max_risorsa=consumo
    media_risorsa=somma/conta

    for tuplina in tupla_consumi_energetici:
        for citta,*resto in tupla_consumi_energetici:
            if(citta==cerca):
                for tupla in resto:
                    for mese,*rilevazione in tupla:
                        for tipoC, consumo in rilevazione:
                            if(tipoC==nome):
                                if(max_risorsa==consumo):
                                    mese_max_risorsa.append(mese)

    return (media_risorsa,(max_risorsa,mese_max_risorsa))                        

cerca=str(input("Inserisci il nome della città: "))
nome=str(input("Inserisci il nome della risorsa: "))
analizza=analizza_consumi_energetici(cerca,nome)
print(f"Media consumo risorsa: {analizza[0]}")
print(f"Massimo consumo risorsa : {analizza[1][0]}")
print(f"Mese massimo consumo risorsa : {analizza[1][1]}")