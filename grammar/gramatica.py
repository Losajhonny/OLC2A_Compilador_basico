# Definir palabras reservads

reserved = {
    'and': 'and',
    'or': 'or',
    'not': 'not',
}

# Definir tokens
tokens = [
    'igual',
    'pyc',
    'coma',

    'pari',
    'pard',

    'mas',
    'men',
    'por',
    'div',
    'mod',
    'pow',
    
    'mayigual',
    'menigual',
    'mayque',
    'menque',
    'igualque',
    'difque',

    'decimal',
    'entero',
    'cadena',
    'caracter',
    'id',

    'comentario_multilinea',
    'comentario_simple',

] + list(reserved.values())

# Tokens
t_igual             = r'='
t_pyc               = r';'
t_coma              = r'\,'

t_pari              = r'\('
t_pard              = r'\)'

t_mas               = r'\+'
t_men               = r'-'
t_por               = r'\*'
t_div               = r'/'
t_mod               = r'%'
t_pow               = r'\^'

t_mayigual          = r'>='
t_menigual          = r'<='
t_mayque            = r'>'
t_menque            = r'<'
t_igualque          = r'=='
t_difque            = r'!='

def t_decimal(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_entero(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_cadena(t):
    r'\".*?\"'
    t.value = t.value[1: -1] # remuevo las comillas
    return t

def t_caracter(t):
    r'\'.\''
    t.value = t.value[1: -1]
    return t

def t_id(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.lower(),'id')    # Check for reserved words
    return t

# Comentario de múltiples líneas /* .. */
def t_comentario_multilinea(t):
    r'\#=(.|\n)*?=\#'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_comentario_simple(t):
    r'\#.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()

# Asociación de operadores y precedenciaz
precedence = (
    ('right', 'igual'), # asignacion
    ('left', 'or'),
    ('left', 'and'),
    ('right', 'not'),
    # ('right', 'or', 'and', 'not'),
    ('nonassoc', 'mayque', 'menque', 'mayigual', 'menigual', 'igualque', 'difque'),
    ('left','mas','men'),
    ('left','por','div', 'mod'),
    ('right','umen'),
    ('right', 'pow'),
    )

# Definición de la gramática
from ast.enums import Tipo
from ast.enums import *
from ast.expresion.operacion.aritmetica import Aritmetica
from ast.expresion.operacion.logica import Logica
from ast.expresion.operacion.relacional import Relacional
from ast.expresion.literales.literal import Literal
from ast.expresion.literales.id import Id

def p_init(t):
    '''init :   expresion'''
    t[0] = t[1]

# -------------------- condiciones --------------------
# def p_condicion(t):
#     '''condicion    :   condicion and condicion
#                     |   condicion or condicion'''
#     if t[2] == "and":
#         t[0] = Logica(OpeLogica.AND, t[1], t[3],  t.lineno(2))
#     else:
#         t[0] = Logica(OpeLogica.OR, t[1], t[3],  t.lineno(2))

# def p_condicion_not(t):
#     'condicion  :   not condicion'
#     t[0] = Logica(OpeLogica.NOT, t[2], None,  t.lineno(1))

# def p_condicion_parentesis(t):
#     'condicion  :   pari condicion pard'
#     t[0] = t[2]

# def p_condicion_relacional(t):
#     '''condicion    :   expresion mayque expresion
#                     |   expresion menque expresion
#                     |   expresion mayigual expresion
#                     |   expresion menigual expresion
#                     |   expresion igualque expresion
#                     |   expresion difque expresion'''
#     if t[2] == ">":
#         t[0] = Relacional(OpeRelacional.MAYORQUE, t[1], t[3],  t.lineno(2))
#     elif t[2] == "<":
#         t[0] = Relacional(OpeRelacional.MENORQUE, t[1], t[3],  t.lineno(2))
#     elif t[2] == ">=":
#         t[0] = Relacional(OpeRelacional.MAYORIGUAL, t[1], t[3],  t.lineno(2))
#     elif t[2] == "<=":
#         t[0] = Relacional(OpeRelacional.MENORIGUAL, t[1], t[3],  t.lineno(2))
#     elif t[2] == "==":
#         t[0] = Relacional(OpeRelacional.IGUALQUE, t[1], t[3],  t.lineno(2))
#     else:
#         t[0] = Relacional(OpeRelacional.DIFQUE, t[1], t[3],  t.lineno(2))




# -------------------- expresiones --------------------

def p_expresion(t):
    '''expresion    :   expresion mas expresion
                    |   expresion men expresion
                    |   expresion por expresion
                    |   expresion div expresion
                    |   expresion mod expresion
                    |   expresion pow expresion'''
    if t[2] == "+":
        t[0] = Aritmetica(OpeAritmetica.SUMA, t[1], t[3],  t.lineno(2))
    elif t[2] == "-":
        t[0] = Aritmetica(OpeAritmetica.RESTA, t[1], t[3],  t.lineno(2))
    elif t[2] == "*":
        t[0] = Aritmetica(OpeAritmetica.MULTIPLICACION, t[1], t[3],  t.lineno(2))
    elif t[2] == "/":
        t[0] = Aritmetica(OpeAritmetica.DIVISION, t[1], t[3],  t.lineno(2))
    elif t[2] == "%":
        t[0] = Aritmetica(OpeAritmetica.MODULO, t[1], t[3],  t.lineno(2))
    else:
        t[0] = Aritmetica(OpeAritmetica.POTENCIA, t[1], t[3],  t.lineno(2))

def p_expresion_unaria(t):
    'expresion  :   men expresion %prec umen'
    t[0] = Aritmetica(OpeAritmetica.RESTA, t[2], None, t.lineno(1))

def p_expresion_parentesis(t):
    'expresion  :   pari expresion pard'
    t[0] = t[2]

def p_expresion_entero(t):
    'expresion  :   entero'
    t[0] = Literal(Tipo.INT64, t[1], t.lineno(1))

def p_expresion_decimal(t):
    'expresion  :   decimal'
    t[0] = Literal(Tipo.FLOAT64, t[1], t.lineno(1))

def p_expresion_cadena(t):
    'expresion  :   cadena'
    t[0] = Literal(Tipo.STRING, t[1], t.lineno(1))

def p_expresion_caracter(t):
    'expresion  :   caracter'
    t[0] = Literal(Tipo.CHAR, t[1], t.lineno(1))

def p_expresion_id(t):
    'expresion  :   id'
    t[0] = Id(t[1], t.lineno(1))




# ----------------- produccion error ------------------

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)



    
import ply.yacc as yacc
parser = yacc.yacc()

def parse(input) :
    return parser.parse(input)
