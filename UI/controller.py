import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        durata = self._view._txtDurata.value
        try:
            intDurata = int(durata)
        except ValueError:
            print("Errore, durata inserita non numerica")
            self._view.txt_result1.controls.clear()
            self._view.txt_result1.controls.append(ft.Text("Errore, inserire un valore numerico intero in 'durata'."))
            self._view.update_page()
            return
        self._model._creaGrafo(intDurata)
        nNodi, nArchi = self._model.getGraphDetails()
        self._view.txt_result1.controls.clear()
        self._view.txt_result1.controls.append(ft.Text(f"Grafo correttamente creato.\n"
                                                       f"Il grafo ha {nNodi} nodi e {nArchi} archi."))
        self._view._ddAlbum.disabled = False
        self.fillDDAlbum()
        self._view._btnAnalisi.disabled = False
        self._view._txtSoglia.disabled = False
        self._view._btnSetAlbum.disabled = False

        self._view.update_page()

    def fillDDAlbum(self):
        albums = self._model._nodes
        for a in albums:
            self._view._ddAlbum.options.append(ft.dropdown.Option(data=a, text=a.Title, on_click=self._selectAlbum))
        self._view.update_page()

    def _selectAlbum(self, e):
        if e.control.data is None:
            self._choiceAlbum = None
        else:
            self._choiceAlbum = e.control.data

    def handle_analisi(self, e):
        connessa, durataConnessa = self._model._analisi(self._choiceAlbum)
        self._view.txt_result1.controls.append(ft.Text(f"Componente connessa - {self._choiceAlbum}:\n"
                                                       f"Lunghezza = {len(connessa)}\n"
                                                       f"Durata componente = {durataConnessa}"))
        self._view.update_page()

    def handle_set_album(self, e):
        durataMax = self._view._txtSoglia.value
        try:
            intDurataMax = int(durataMax)
        except ValueError:
            print("Errore, durata inserita non numerica")
            self._view.txt_result2.controls.clear()
            self._view.txt_result2.controls.append(ft.Text("Errore, inserire un valore numerico intero in 'durata'."))
            self._view.update_page()
            return
        setAlbum, durataTot = self._model.percorso(self._choiceAlbum, intDurataMax)
        self._view.txt_result2.controls.clear()
        self._view.txt_result2.controls.append(ft.Text(f"Set di album lungo {len(setAlbum)} di durata totale {durataTot / (60*1000)} minuti."))
        for a in setAlbum:
            self._view.txt_result2.controls.append(ft.Text(f"{a}"))
        self._view.update_page()
