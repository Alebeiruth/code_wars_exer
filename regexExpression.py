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
##exemplo str = "0" > se for valor valido ele executa

##EXERCICIO 05/100 > pede para contar o numero de sheep 

def count_sheeps(sheep):
  ## Todo May the force be with you
  return sheep.count(True)

##utiliza count para contar

##EXERCICIO 06/100 > pede para trocar str 
def DNA_strand(dna):
    # code here
     return dna.translate(str.maketrans("ATCG","TAGC")) 

# translate() retorna uma string onde alguns caracteres especificados são substituídos pelo caracter descrito em um dicionário, ou em uma tabela de mapeamento.
# método maketrans() cria uma tabela de mapeamento

##EXERCICIO 07/100 >
def positive_sum(arr):
    # Your code here
    return sum(map(lambda x: x if x > 0 else 0, arr))

## FUCTION SUM
""" a = (1, 2, 3, 4, 5)
 x = sum(a)
 x = 15""" 

## FUCTION MAP
"""def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

print(x)
<map object at 0x034244F0>

#convert the map into a list, for readability:
print(list(x))
['appleorange', 'bananalemon', 'cherrypineapple']
"""

##EXERCICIO 08/100 > verificar se a primeira str é igual a ultima exp solution('abc', 'bc') = True

def solution(text, ending):
    # your code here...
    return text.endswith(ending)
# metodo endswith retorna True se a str terminar com valor especificado, se não False  

##EXERCICIO 09/100 > esse exercicio solicita retorno do número de pessoas que ainda estão no ônibus após o último ponto de ônibus 
def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])
    
# for stop in bus_stops > para cada elemento stop na lista bus_stops
# stop[0] - stop[1] > calcula diferença entre n de passageiros q entram e os que saem
# (stop[0] - stop[1] for stop in bus_stops) > cria um iterados pra cada parada
# sum() soma todos o valores da expressão anterior e geradora de valor
# EXP: bus_stops = [(10, 0), (3, 5), (2, 3)] > 10 - 0 = 10 / 3 - 5 = -2 / 10 - 2 = 8 / 2 - 3 = -1 / 8 - 1 = 7
#      print(number(bus_stops)) = 7
