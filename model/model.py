import networkx as nx
from database.dao import DAO

class Model:
    def __init__ (self) :
        self.G = nx.Graph ()

        self.get_nodes ()
        self.get_edges ()


    def get_nodes (self) :
        nodes = []
        cromosomi = DAO.read_cromosomi ()
        for c in cromosomi :
            nodes.append (c)
        return nodes

    def get_edges (self) :
        interazioni_totali = []
        interazioni = DAO.read_interazione ()

        edges_finali = []
        for i in interazioni :
            interazioni_totali.append ([(i.cromosoma1, i.cromosoma2) , i.correlazione])

        for edge in edges_finali :
            print  (edge)

        return edges_finali

    def buildWeightedGraph (self)  :
        self.G.add_nodes_from (self.get_nodes())

    def get_num_nodes (self) :
        num_nodes = self.G.number_of_nodes()
        return num_nodes

    def get_num_edges (self) :
        num_edges = self.G.number_of_edges()
        return num_edges