import csv

from clases.cars import 

class Graph:

    def __init__(self, source_file):

        self.board = self.load_board(source_file)

    def load_board(self, source_file):
        
