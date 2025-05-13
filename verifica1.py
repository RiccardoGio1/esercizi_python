class Libro:
    def __init__(self, isbn, titolo, autore, anno):
        # Inizializza gli attributi del libro
        self.isbn=isbn
        self.titolo=titolo
        self.autore=autore
        self.anno=anno

    def __str__(self):
        # Restituisce una descrizione leggibile del libro
        return f'{self.titolo} di {self.autore}, ({self.anno}) - ISBN {self.isbn}'


class Biblioteca:
    def __init__(self):
        # Inizializza la lista dei libri
        self.libri=[]

    def aggiungi_libro(self, libro):
        # Aggiunge un libro alla lista
        self.libri.append(libro)

    def rimuovi_libro(self, isbn):
        # Rimuove un libro in base all'ISBN
        for libro in self.libri:
            if(libro.isbn==isbn):
                print(f"Libro: {libro} rimosso con successo.")
                self.libri.remove(libro)

    def elenco_libri(self):
    # Restituisce la lista dei libri nella biblioteca
     print("Lista di libri:")
     for libro in self.libri:
        print(libro)


    def cerca_libro(self, isbn):
     # Restituisce il libro trovato o None se non esiste
     i=0
     for libro in self.libri: 
        if(libro.isbn==isbn):
            return libro
     return None


biblioteca=Biblioteca()


while(True):
    print("----------------")
    print("0)Termina Programma\n1)Aggiungi Libri\n2)Rimuovi Libro\n3)Stampa Libri\n4)Cerca Libro")
    print("----------------")
    scelta=int(input("Inserisci la tua scelta: "))

    if(scelta==0):
        print("Programma terminato")
        break
    elif(scelta==1):
        libro1=Libro("9781234567897","Il nome della rosa","Umberto Eco","1980")
        libro2=Libro("9789876543210","1984","George Orwell","1949")
        libro3=Libro("9780007117116","Il Signore degli Anelli","J.R.R. Tolkien","1954")

        biblioteca.aggiungi_libro(libro1)
        biblioteca.aggiungi_libro(libro2)
        biblioteca.aggiungi_libro(libro3)

    elif(scelta==2):
        isbn=str(input("Inserisci l'ISBN del libro che vuoi rimuovere: "))
        biblioteca.rimuovi_libro(isbn)

    elif(scelta==3):
        
        biblioteca.elenco_libri()

    elif(scelta==4):
        isbn1=str(input("Inserisci l'ISBN del libro che vuoi cercare: "))
        print(biblioteca.cerca_libro(isbn1))

