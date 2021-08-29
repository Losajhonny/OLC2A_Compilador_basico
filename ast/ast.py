from abc import ABC, ABCMeta

class Ast(ABC):
    temp = 0
    eti = 0

    def __init__(self):
        __metaclass__ = ABCMeta

    def newTemp(self):
        Ast.temp = Ast.temp + 1
        return f"t{Ast.temp}"

    def getTemp(self):
        return f"t{Ast.temp}"

    def newEti(self):
        Ast.eti = Ast.eti + 1
        return f"L{Ast.eti}"

    def getEti(self):
        return f"L{Ast.eti}"
