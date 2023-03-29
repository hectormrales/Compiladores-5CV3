import nltk #procesamiento del lenguaje natural y la lingüística computacional.
nltk.download('punkt')
import re #proporciona operaciones de coincidencia de expresiones regulares

f = open('CodigodeEntrada.c', 'r')
programa = f.read()
contador = 0

Salida_Identificadores = []
Salida_PalabrasReservadas = []
Salida_Simbolos = []
Salida_Operadores = []
Salida_Numeros = []


def eliminar_espacios(program):
    Escanear_Programa = []
    for line in prog:
        if (line.strip() != ''):
            Escanear_Programa.append(line.strip())
    return Escanear_Programa


def eliminar_comentarios(program):
    Varios_comentarios_eliminados = re.sub("/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", program)
    comentario_eliminado = re.sub("//.*", "", Varios_comentarios_eliminados)
    comentarios_eliminados = comentario_eliminado
    return comentarios_eliminados



RE_PalabrasRevervadas = "return|sizeof|static|struct|switch|typedef|void|while|string|class|break|case|char|const|continue|default|do|double|else|enum|float|for|if|int|long"
RE_Operadores = "(\++)|(-)|(=)|(\*)|(/)|(%)|(--)|(<=)|(>=)"
RE_Numeros = "^(\d+)$"
RE_CaracteresEspeciales = "[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
RE_Identificadores = "^[a-zA-Z_]+[a-zA-Z0-9_]*"


remover_comentarios = eliminar_comentarios(programa)
prog = remover_comentarios.split('\n')


Prog_escaneado = eliminar_espacios(prog)

programa_escaneado = '\n'.join([str(elemento) for elemento in Prog_escaneado])



lineas_escaneadas = programa_escaneado.split('\n')
contador_veces = 0


Codigo_fuente=[]
for line in lineas_escaneadas:
        Codigo_fuente.append(line)


mostrar_contador = 0
for line in Codigo_fuente:
    contador = contador + 1
    if(line.startswith("#include")):
        tokens = nltk.word_tokenize(line)
    else:
        tokens = nltk.wordpunct_tokenize(line)
    for token in tokens:
        if(re.findall(RE_PalabrasRevervadas, token)):
            Salida_PalabrasReservadas.append(token)
        elif(re.findall(RE_Operadores, token)):
            Salida_Operadores.append(token)
        elif(re.findall(RE_Numeros,token)):
            Salida_Numeros.append(token)
        elif (re.findall(RE_CaracteresEspeciales, token)):
            Salida_Simbolos.append(token)
        elif (re.findall(RE_Identificadores, token)):
            Salida_Identificadores.append(token)


print("Se encuentran ",len(Salida_PalabrasReservadas),"Palabras reservadas: ",Salida_PalabrasReservadas)
print("\n")
print("Se encuentran ",len(Salida_Identificadores),"Identificadores: ",Salida_Identificadores)
print("\n")
print("Se encuentran ",len(Salida_Simbolos),"Simbolos:",Salida_Simbolos)
print("\n")
print("Se encuentran ",len(Salida_Numeros),"Digitos:",Salida_Numeros)
print("\n")