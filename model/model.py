import networkx as nx
from UI.view import View

from database.DAO import DAO


class Model:

    def __init__(self):
        self.grafo = nx.Graph()

    def creaGrafo(self,anno):
        self.grafo.add_edges_from(DAO.getAllContiguityYearEdge(anno))
        self.grafo.add_nodes_from(DAO.getAllCountryYearNodes(anno))

    def connessioni(self):
        return len(list(nx.connected_components(self.grafo)))

    def contavicini(self,c):
        return self.grafo.degree(c)

