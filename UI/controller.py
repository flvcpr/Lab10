import flet as ft
import networkx as nx


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()
        if 1816<=int(self._view._txtAnno.value)<=2016:
            self._model.creaGrafo(self._view._txtAnno.value)
        else:
            self._view.create_alert("L'anno inserito non è corretto")
            return

        num = self._model.connessioni()

        self._view._txt_result.controls.append(ft.Text(f"Componenti connesse: {num}"))

        for c in self._model.grafo.nodes:
            self._view._txt_result.controls.append(ft.Text(f"{c.StateNme} -- {self._model.contavicini(c)}"))

        self._view.update_page()
