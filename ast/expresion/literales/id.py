from ast.enums import Tipo
from ast.expresion.expresion import Expresion

class Id(Expresion):

    def __init__(self, id, linea):
        super().__init__()
        self.id = id
        self.linea = linea

    def genC3D(self, ent):
        return self.id
