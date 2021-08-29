from ast.expresion.expresion import Expresion

class Literal(Expresion):

    def __init__(self, tipo, valor, linea):
        super().__init__()
        self.tipo = tipo
        self.valor = valor
        self.linea = linea

    def genC3D(self, ent):
        return self.valor
