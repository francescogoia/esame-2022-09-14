import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}

    def _creaGrafo(self, durata):
        durataMilliSec = durata * 60 *1000
        allAlbums = DAO.getAllNodes()
        self._nodes = []
        for a in allAlbums:
            if a.durata > durataMilliSec:
                self._grafo.add_node(a)
                self._nodes.append(a)
        for u in self._nodes:
            for v in self._nodes:
                if u != v:
                    arco = DAO.getEdge(u.AlbumId, v.AlbumId)
                    if arco != []:
                        self._grafo.add_edge(u, v)


    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def _analisi(self, nodo):
        connessa = list(nx.node_connected_component(self._grafo, nodo))
        durataTot = 0
        for a in connessa:
            durataTot += a.durata
        durataMin = durataTot / (60*1000)
        return connessa, durataMin

    def percorso(self, partenza, durataMax):
        durataMaxMilliSec = durataMax * 60 * 1000
        self._bestPath = []
        self._bestDurata = 0
        self._ricorsione(partenza, [partenza], durataMaxMilliSec)
        return self._bestPath, self._bestDurata

    def _ricorsione(self, nodo, parziale, durataMaxMilli):
        durataParziale = self.getDurataParziale(parziale)
        if durataParziale > durataMaxMilli:
            return
        if len(parziale) > len(self._bestPath) and durataParziale < durataMaxMilli:
            self._bestPath = copy.deepcopy(parziale)
            self._bestDurata = durataParziale

        vicini = self._grafo.neighbors(nodo)
        for v in vicini:
            if v not in parziale:
                parziale.append(v)
                self._ricorsione(v, parziale, durataMaxMilli)
                parziale.pop()

    def filtroNodi(self, v, parziale):
        pass

    def filtroArchi(self, n, v, parziale):
        pass

    def getDurataParziale(self, parziale):
        totD = 0
        for a in parziale:
            totD += a.durata
        return totD
