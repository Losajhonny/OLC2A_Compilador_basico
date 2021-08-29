from ast.expresion.expresion import Expresion
from ast.enums import OpeAritmetica, Tipo
from ast.ast import Ast

class Aritmetica(Expresion):
    def __init__(self, op, exp1, exp2, linea):
        super().__init__()
        self.op = op
        self.exp1 = exp1
        self.exp2 = exp2
        self.linea = linea

    '''
        Genera codigo de 3 direcciones
        tn = tn-1 + tn-2
        En tn se puede definir
            - una constante
            - un literal
    '''
    def genC3D(self, ent):
        if self.exp2 == None:
            return self.getUnario(ent)
        else:
            # expresiones
            t1 = self.exp1.genC3D(ent)
            t2 = self.exp2.genC3D(ent)
            # tn = self.newTemp()
            # print(f"{tn} = {t1} {self.getOp()} {t2}")

            # reutilizacion de temporales
            Ast.temp = Ast.temp - self.exp1.num - self.exp2.num + 1
            tn = self.getTemp()
            self.num = 1
            print(f"{tn} = {t1} {self.getOp()} {t2}")

            return tn

    def getUnario(self, ent):
        t1 = self.exp1.genC3D(ent)
        tn = self.newTemp()
        print(f"{tn} = - {t1}")
        return tn

    def getOp(self):
        if self.op == OpeAritmetica.SUMA:
            return "+"
        elif self.op == OpeAritmetica.RESTA:
            return "-"
        elif self.op == OpeAritmetica.MULTIPLICACION:
            return "*"
        elif self.op == OpeAritmetica.DIVISION:
            return "/"
        elif self.op == OpeAritmetica.MODULO:
            return "%"
        else:
            return "^"
