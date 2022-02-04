
from abc import ABC, abstractmethod

import numpy as np
import networkx as nx


class PieceObject:
    def __init__(self, team, name, info):
        self.team = team
        self.name = name
        self.info = info


class Board(ABC):
    def initialize_board(self, nodedict, edges):
        self.nodes_info = nodedict
        self.board = nx.Graph()
        self.board.add_nodes_from(nodedict.keys())
        self.board.add_edges_from(edges)

    @abstractmethod
    def render(self):
        pass
