from entorno.entorno import Entorno
from ast.ast import Ast
import grammar.gramatica as grammar

f = open("./entrada.txt", "r")
input = f.read()

entorno = Entorno(None)
obj = grammar.parse(input)

# Ast.eti += 1
# obj.true = f"L{Ast.eti}"
# Ast.eti += 1
# obj.false = f"L{Ast.eti}"

obj.genC3D(entorno)

print("\n# etiquetas verdaderas")
print(obj.lv)
print("# etiquetas falsas")
print(obj.lf)

# print("\n# etiquetas verdaderas")
# print(obj.true)
# print("# etiquetas falsas")
# print(obj.false)

print("\n")
print("\n")
print("\n")
print("\n")
print("digraph {")
obj.genParseTree()
print("}")