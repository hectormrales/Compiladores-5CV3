import re #proporciona operaciones de coincidencia de expresiones regulares

import nltk #procesamiento del lenguaje natural y la lingüística computacional.
nltk.download('punkt')

Entrada_Programa = input("Introduzca su codigo: ");
Entrada_Tokens = nltk.wordpunct_tokenize(Entrada_Programa);

print(Entrada_Tokens);


RE_PalabrasRevervadas = "return|sizeof|static|struct|switch|typedef|void|while|string|class|break|case|char|const|continue|default|do|double|else|enum|float|for|if|int|long"
RE_Operadores = "(\++)|(-)|(=)|(\*)|(/)|(%)|(--)|(<=)|(>=)"
RE_Numeros = "^(\d+)$"
RE_CaracteresEspeciales = "[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
RE_Identificadores = "^[a-zA-Z_]+[a-zA-Z0-9_]*"


#Para categorizar los tokes

for token in Entrada_Tokens:
    if(re.findall(RE_PalabrasRevervadas,token)):
        print(token , "-------> Palabra Reservada")
    elif(re.findall(RE_Operadores,token)):
        print(token, "-------> Operador")
    elif(re.findall(RE_Numeros,token)):
        print(token, "-------> Numero")
    elif(re.findall(RE_CaracteresEspeciales,token)):
        print(token, "-------> Simbolo/Caracter especial")
    elif(re.findall(RE_Identificadores,token)):
        print(token, "-------> Identificador")
    else:
        print("Valor desconocido")