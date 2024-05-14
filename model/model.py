import networkx as nx
from UI.view import View

from database.DAO import DAO


class Model:

    def __init__(self):
        self.grafo = nx.Graph()
        self.idMap = {}

    def creaGrafo(self,anno):
        self.grafo.clear()
        print("sono in crea Grafo")
        nodi = DAO.getAllCountryYearNodes(anno)
        self.grafo.add_nodes_from(nodi)
        for n in nodi:
            self.idMap[n.CCode] = n

        print("nodi aggiunti alla mappa")

        edges = DAO.getAllContiguityYearEdge(anno)

        for e in edges:
            u = self.idMap[e.state1no]
            v = self.idMap[e.state2no]
            self.grafo.add_edge(u,v)

        print("ponti aggiunti")

    def connessioni(self):
        return len(list(nx.connected_components(self.grafo)))

    def contavicini(self,c):
        return self.grafo.degree(c)

