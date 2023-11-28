##EXERCICIO 01/100
import re ## permite uso de expressoes regulares em PY

def validate_usr(username):
    #your code here
    return bool(re.fullmatch(r'^[a-z0-9_]{4,16}$', username))


##re.fullmatch > verifica se str é uma expressão regular
## ela busca expreção q começa ^ e termina em $, com 4 a 16 caracteres que podem ser de a-z,
## numeros 0-9 ou sublinhados _
## retorna True ou False

##EXERCICIO 02/100 > se fizer +10 ou = retorna mensagem boa, se não msg ruim/tente

def hoop_count(n):
    # Good Luck!
    return "Great, now move on to tricks" if n >= 10 else "Keep at it until you get it"

##EXERCICIO 03/100 > remoção de quaisquer zero ou str no final do numero

def no_boring_zeros(n):
    # your code
    return int(str(n).rstrip('0')) if n else 0

#rstrip > remove qualquer espaço em branco ou str que vc define no final

##EXERCICIO 04/100 > demostrar uma saida assim ('+', 4, 7) --> 11

def basic_op(operator, value1, value2):
    #your code here
    return eval("{}{}{}".format(value1, operator, value2))

##eval > avalia o valor da expressão, se for valor valido ele executa 

##EXERCICIO 05/100 > pede para contar o numero de sheep 

def count_sheeps(sheep):
  ## Todo May the force be with you
  return sheep.count(True)

##uitliza count para contar