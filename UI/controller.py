import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """""
        # TODO
        self._model.G.clear ()
        self._model.buildWeightedGraph ()

        self._view.lista_visualizzazione_1.controls.clear ()
        self._view.lista_visualizzazione_1.controls.append (
            ft.Text (f"I nodi presenti nel grafo sono: {self._model.get_num_nodes()}")
        )
        self._view.lista_visualizzazione_1.controls.append (
            ft.Text (f"Gli archi presenti nel grafo sono: {self._model.get_num_edges()}")
        )
        self._view.page.update ()

    def handle_conta_edges(self, e):
        """ Handler per gestire il conteggio degli archi """""
        # TODO

    def handle_ricerca(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """""
        # TODO