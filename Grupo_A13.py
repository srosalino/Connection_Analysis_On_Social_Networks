# --------------------------------------------------- Enquadramento ----------------------------------------------------
# Trabalho de Projeto Final
# UC - Estruturas de Dados e Algoritmos da Licenciatura de Ciência de Dados
#
# Grupo 11
# Elaborado por:
# Catarina Brito, nº 98521
# Sebastião Rosalino, n.º 98437
#
# Coordenadora da UC:
# Professora Ana Maria de Almeida
# Docentes:
# Professora Ana Maria de Almeida
# Professor Filipe Santos
# Professor Ricardo António

# Licenciatura de Ciência de Dados - 1º ano - Turna CDA1
# Ano Letivo 2020/2021 - 2º Semestre

# ---------------------------------------------------------------------------------------------------------------------


"""Bibliotecas importadas"""

import numpy as np
import csv
# import networkx as nx
# import matplotlib.pyplot as plt


class Vertex:
    """Reserva os atributos da classe"""
    __slots__ = "_key"

    def __init__(self, key):
        """Método construtor que recebe como input a identificação """
        self._key = key

    @property
    def key(self):             # Propriedade iden da classe Vertex
        return self._key

    def __str__(self):          # Método para utilização do comando print sobre os objetos da classe
        return "Vertex: {}".format(self._key)

    def __eq__(self, other):    # Método para avaliar a igualdade entre dois objetos
        if isinstance(other, Vertex):
            return self._key == other._key
        return False

    def __hash__(self):         # Método para garantir a unicidade dos objetos
        return hash(self._key)


class Edge:
    __slots__ = "_origem", "_destino", "_peso"          # Reserva dos únicos atributos da classe

    def __init__(self, origem, destino, peso=None):     # Inicialização do construtor da classe
        self._origem = origem
        self._destino = destino
        self._peso = peso

    @property       # Propriedade origem dos objetos
    def origem(self):
        return self._origem

    @property        # Propriedade destino dos objetos
    def destino(self):
        return self._destino

    @property       # Propriedade peso dos objetos
    def peso(self):
        return self._peso

    def endpoints(self):    # Método para retornar em forma de tuplo a origem e o destino de um objeto
        return self._origem, self._destino

    def opposite(self, v):  # Método para retornar a localização oposta de um objeto
        return self._destino if v is self._origem else self._origem

    def __str__(self):      # Método para utilização do comando print sobre os objetos da classe
        return f"Edge:({self._origem}, {self._destino})"

    def __eq__(self, other):    # Método para avaliar a igualdade entre dois objetos
        if isinstance(other, Edge):
            return self._origem == other._origem and self._destino == other._destino and self._peso == other._peso
        return False

    def __hash__(self):         # Método para garantir a unicidade dos objetos
        return hash((id(self._origem), id(self._destino)))


class Grafo:
    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._incoming is not self._outgoing

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing

    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2

    def edges(self):
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v):
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def exists_vertex(self, x):
        return x in self._outgoing and x in self._incoming

    def insert_vertex(self, x=None):
        v = Vertex(x)
        self._outgoing[v.key] = {}
        if self.is_directed():
            self._incoming[v.key] = {}
        return v.key

    def insert_edge(self, u, v, x=None):
        e = Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

    def remove_vertex(self, v):
        for i in self.incident_edges(v):
            self.remove_edge(v, i)
        del self._outgoing[v]
        if self.is_directed():
            for i in self.incident_edges(v, False):
                self.remove_edge(i, v)
            del self._incoming[v]
        return v

    def remove_edge(self, u, v):
        for e in self._outgoing[u]:
            x, y = e.endpoints()
            if u == x and v == y:
                self._outgoing[u].remove(e)
                self._incoming[v].remove(e)

    def top10_interligados(self):   # Assumi que mais interligados = mais followeds
        all_users = {}
        for user in self._outgoing:
            all_users[user] = self.degree(user)
        all_users_sorted = sorted(all_users.items(), key=lambda x: x[1], reverse=True)
        final_top = []
        for e in all_users_sorted[0:10]:
            final_top.append(e[0])
        return final_top

    def top10_least_followed(self):     # Os 10 utilizadores com menos seguidores
        all_users = {}
        for user in self._outgoing:
            all_users[user] = self.degree(user)
        all_users_sorted = sorted(all_users.items(), key=lambda x: x[1])
        final_top = []
        for e in all_users_sorted[0:10]:
            final_top.append(e[0])
        return final_top

    def shortest_path(self, source):
        distance = {}
        for v in self.vertices():
            if v == source:
                distance[v] = 0
            else:
                distance[v] = np.inf
        dict_distance = {source: 0}
        while dict_distance:
            current_source_node = min(dict_distance, key=lambda k: dict_distance[k])
            del dict_distance[current_source_node]
            for node_dist in self.vertices()[current_source_node].values():
                adjnode = node_dist.destino
                lenght_to_adjnode = node_dist.peso
                if distance[adjnode] > distance[current_source_node] + lenght_to_adjnode:
                    distance[adjnode] = distance[current_source_node] + lenght_to_adjnode
                    dict_distance[adjnode] = distance[adjnode]
        return distance

    def degree_centrality(self, v):
        popularidade = self.degree(v, False)
        influencia = self.degree(v, True)
        return "Este utilizador tem {} de popularidade e {} de influência".format(popularidade, influencia)

    def closeness(self, v):
        total_distance = 0
        for distance in self.shortest_path(v).values():
            if distance != np.inf:
                total_distance += distance
        if total_distance == 0:
            final_closeness = 0
        else:
            final_closeness = 1 / total_distance
        return final_closeness

    def top10_closeness(self):
        all_users = {}
        for user in self._outgoing:
            all_users[user] = self.closeness(user)
        all_users_sorted = sorted(all_users.items(), key=lambda x: x[1], reverse=True)
        final_top = []
        for e in all_users_sorted[0:10]:
            final_top.append(e[0])
        return final_top


def leitura_csv():           # Função para leitura do ficheiro
    filename = 'Github.csv'
    with open(filename, 'r') as file:   # Abertura do ficheiro para leitura
        data = csv.reader(file, delimiter=",")
        next(data)      # A primeira linha não deve ser lida
        for valores in data:    # Para cada linha
            id_origem = valores[0]      # O id_origem será a primeira posição da linha, ou seja, o follower
            id_destino = valores[1]     # O id_origem será a segunda posição da linha, ou seja, o followed
            peso = int(valores[2] if len(valores) == 3 else 1)   # O peso será a terceira posição caso ela exista, se não, será por default 1
            if not g.exists_vertex(id_origem):      # Caso o vértice não exista
                g.insert_vertex(id_origem)          # Procede-se à sua inserção
            if not g.exists_vertex(id_destino):     # Caso o vértice não exista
                g.insert_vertex(id_destino)         # Procede-se à sua inserção
            g.insert_edge(id_origem, id_destino, peso)     # Posteriormente, é inserida a edge correspondente


''' 
    Função usada para visualizar o grafo 

def visualizar(file):
    g = nx.DiGraph()
    filename = file
    with open(filename, 'r') as file:
        data = csv.reader(file, delimiter=",")
        next(data)
        for valores in data:
            id_origem = valores[0]
            id_destino = valores[1]
            peso = int(valores[2] if len(valores) == 3 else 1)
            g.add_edges_from([(id_origem,id_destino)],weight=peso)
            pos = nx.spring_layout(g)
        nx.draw_networkx_nodes(g, pos, node_size=100)
        nx.draw_networkx_edges(g, pos, edgelist=g.edges(), edge_color='black')
        nx.draw_networkx_labels(g, pos)
        plt.show()
'''

if __name__ == '__main__':
    g = Grafo(True)
    leitura_csv()
    print(g.top10_interligados())
    print(g.top10_least_followed())
    print(g.shortest_path('1570'))
    print(g.degree_centrality('1570'))
    print(g.closeness('1570'))
    print(g.top10_closeness())

# -------------------------------------------------- fim de código -----------------------------------------------------
