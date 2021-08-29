from entorno.entorno import Entorno
import grammar.gramatica as grammar

f = open("./entrada.txt", "r")
input = f.read()

entorno = Entorno(None)
obj = grammar.parse(input)
obj.genC3D(entorno)

