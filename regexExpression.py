##EXERCICIO 01/100

import re ## permite uso de expressoes regulares em PY

def validate_usr(username):
    #your code here
    return bool(re.fullmatch(r'^[a-z0-9_]{4,16}$', username))
##re.fullmatch > verifica se str é uma expressão regular
## ela busca expreção q começa ^ e termina em $, com 4 a 16 caracteres que podem ser de a-z,
## numeros 0-9 ou sublinhados _
## retorna True ou False