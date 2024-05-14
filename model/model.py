import networkx as nx
from UI.view import View

from database.DAO import DAO


class Model:

    def __init__(self):
        self.grafo = nx.Graph()
        self.idMap = {}

    def creaGrafo(self,anno):

        #ho aggiunto 2 print per vedere meglio le stampe
        self.grafo.clear()
        #il grafo andava pulito a ogni clock del tasto, altrimenti andava solo ad aggiungere
        #nodi a un grafo gia esistente (che quindi rimaneva pieno dato che ne aveva aggiunti
        #gia al click precedente, se aggiugno un nodo a un grafo che ha gia quel nodo, il grafo
        #rimane uguale

        print("sono in crea Grafo")
        nodi = DAO.getAllCountryYearNodes(anno)

        #un altro errore non so se anche tu l'abbia fatto cosi era quello di costruire prima gli archi
        #e poi i nodi, quidni andavano invertite le get, prima fai i nodi e poi gli archi
        self.grafo.add_nodes_from(nodi)

        #qui c'è l'errore un po piu grande, prima tu stavi passando un arco con tutti i parametri
        #del contiguity senza dirgli quali fossero i due nodi in cui inserire l'arco, puoi fare sta roba
        #ma non so bene come usare il metodo "add_edge_from" che abbiamo usato noi, percio ho fatto
        #una mappa con il parametro in comune tra Country e Contiguity (ho scelto il codice per comodita)

        for n in nodi:
            self.idMap[n.CCode] = n

        print("nodi aggiunti alla mappa")

        #salvo tutti i nodi (che sono oggetti di tipo contiguity con tutti i parametri scritti nel dataclass
        #della classe Contiguity di Model
        edges = DAO.getAllContiguityYearEdge(anno)

        #devo aggiungere per forza 1 arco alla volta, tutti insieme non so :(
        for e in edges:
            u = self.idMap[e.state1no] #prendo l'oggetto country dal codice in comune
            v = self.idMap[e.state2no] #stessa cosa
            self.grafo.add_edge(u,v) #aggiungo il singolo non pesato

        print("ponti aggiunti")

    def connessioni(self):
        return len(list(nx.connected_components(self.grafo)))

    def contavicini(self,c):
        return self.grafo.degree(c)

