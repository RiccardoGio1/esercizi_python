import math

class Pagella():

    def __init__(self,voti):
        self.voti = voti
    
    def __repr__(self):
        return f'{self.voti}'
    
    def media(self):
        somma=0
        conta=0
        for i in range (0,len(self.voti)):
            somma+=self.voti[i]
            conta+=1
        media=somma/conta
        return media
    
    def __getitem__(self,i):
        return self.voti.__getitem__(i)
    

    def __eq__(self,pagella):

        if(len(self.voti)!=len(pagella.voti)):       
            print("Le pagelle hanno un numero diverso di materie e non possono essere confrontate")
            return None
        
        conta=0
        for i in range (0,len(self.voti)):
            for z in pagella:
                if(self.voti[i]==z):
                    conta+=1

        if(len(self.voti)==conta):
            return True 
        else:
            return False

    def __sub__(self,pagella):

        if(len(self.voti)!=len(pagella.voti)):       
            print("Le pagelle hanno un numero diverso di materie e non possono essere confrontate")
            return None

        lista=[]
        for a,b in zip(self.voti,pagella.voti):
            lista.append(a-b)
        return Pagella(lista)
     
    
    def impegno(self):
        lista=[]
        somma=0
        pagella1=self.voti

        for a,b in zip(self.voti,pagella1):
            lista.append(a*b)

        for i in range (0,len(self.voti)): 
            somma+=lista[i]
        
        return math.sqrt(somma)    
     

p = Pagella([6, 8, 7])
p1 = Pagella([3, 4, 3])
p2 = Pagella([6, 8])
print(f"1)",p)
print(f"2)",p.media()) 
print(f"3)",p[1])  # stampa 8   
print(f"4)",p==p1)
print(f"5)",p-p1)
print(f"6)",p2.impegno())

