#Riccardo Giovenzana

while(True):

    
    print("Media goal parite = 1 \nMedia goal squadra=2 \nPartia con piu goal=3 \nPartita con meno goal=4")
    scelta=int(input("Inserisci un opzione: (0 per uscire) :"))

    tupla_partite = (
        ("SquadraA", "SquadraB", 3, 2),
        ("SquadraC", "SquadraD", 1, 1),
        ("SquadraB", "SquadraC", 2, 4),
        ("SquadraD", "SquadraA", 0, 3),
        ("SquadraB", "SquadraD", 1, 2)
    )
    if(scelta==1):
        def media_gol_partite(tupla_partite):
            somma1=0
            somma2=0
            somma3=0
            conta=0
            for squadraCasa,squadraOspite,goal1,goal2 in tupla_partite:
                somma1=somma1+goal1
                somma2=somma2+goal2
                conta+=2
            somma3=somma1+somma2       
            media=somma3/conta
            return(media)

        mediaGoal=media_gol_partite(tupla_partite)
        print(f"Media goal partite {mediaGoal}")
        print("--------------------------------------------\n")
    elif(scelta==2):
        def media_gol_squadra(tupla_partite,squadra):
            somma=0
            conta=0
            media=0
            for squadraCasa,squadraOspite,goal1,goal2 in tupla_partite:
                if(squadraCasa==squadra):
                    somma=somma+goal1
                    conta=conta+1
                    media=somma/conta
                    return media
                elif(squadraOspite==squadra):
                    somma=somma+goal2
                    conta=conta+1
                    media=somma/conta
                    return media
            
        squadra=str(input("Inserisci la squadra: "))
        mediaSquadra=media_gol_squadra(tupla_partite,squadra)       
        print(f"Media goal squadra {mediaSquadra}")
        print("--------------------------------------------\n")
    elif(scelta==3):
        def partita_con_più_goal(tupla_partite):
            maxgoal=0
            
            for squadraCasa,squadraOspite,goal1,goal2 in tupla_partite:
                totgoal=goal1+goal2
                if(totgoal>maxgoal):
                    maxgoal=totgoal
                    squadra1=squadraCasa
                    squadra2=squadraOspite
                    maxgoal1=goal1
                    maxgoal2=goal2

            return (maxgoal,squadra1, squadra2,maxgoal1,maxgoal2)   
        maxgoal = partita_con_più_goal(tupla_partite)
        print(f"Goal totali: {maxgoal[0]}")
        print(f"Squadra di casa {maxgoal[1]} : {maxgoal[3]} goal")
        print(f"Squadra di ospite {maxgoal[2]} : {maxgoal[4]} goal ")
        print("--------------------------------------------\n")
    elif(scelta==4):
        def partita_con_meno_goal(tupla_partite):
            mingoal=100000000
            for squadraCasa,squadraOspite,goal1,goal2 in tupla_partite:
                totgoal=goal1+goal2
                if(totgoal<mingoal):
                    mingoal=totgoal
                    squadra1=squadraCasa
                    squadra2=squadraOspite
                    mingoal1=goal1
                    mingoal2=goal2
            return (mingoal,squadra1, squadra2,mingoal1,mingoal2)
        mingoal = partita_con_meno_goal(tupla_partite)
        print(f"Goal totali: {mingoal[0]}")
        print(f"Squadra di casa {mingoal[1]}, con {mingoal[3]} goal")
        print(f"Squadra di ospite {mingoal[2]}, con {mingoal[4]} goal")
        print("--------------------------------------------\n")
    elif(scelta==0):
        break
print(f"FINE ESECUZIONE PROGRAMMA")