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

##EXERCICIO 10/100 > Se bollean for True retorne "Yes" se for False "No"
def bool_to_word(boolean):
    # TODO
    return "Yes" if boolean == True else "No"

##EXERCICIO 11/100 > retorna string se ela possuir tamanho 4 str
def friend(x):
    return [n for n in x if len(n) == 4
##return um nova lista 
##for n in x > itera sobre cada elemento N na Lista x
## if len(n) == 4 > filtra N incluindo-o na lista de return apenas se o tamanho/len de N dor 4 str

##EXERCICIO 12/100 > retorna True se o triangulo é possivel ou não
def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)
## desigualdade triangular afirma que a soma dos comprimentos de quaisquer lados de um triangulo deve ser maior
## que o comprimento do terceiro lado.

##EXERCICIO 13/100 > procurar o ano e recebe o seculo q o ano se encontra
def century(year):
    # Finish this :)
    return (year + 99) // 100

g = century(1709)
print(g) 
## seculo 18

##EXERCICIO 14/100 > contar os numeros que são divisiveis
def divisors(n):
    return len([ x for x in range(1, n + 1) if n % x == 0 ]);

# len calcula o tamanho da lista 
# abertura de [] cria lista com todos os x que dividem n
# x for x in range(1, n+1) > itera sobre a sequencia de numeros
# range (1, n+1) > gera sequencia de numeros de 1 a N
# if verifica se n é divisivel por x

##EXERCICIO 15/100 > entre dois numeros int positivo e negativo, achar a soma de todos inteiros
def get_sum(a,b):
    #good luck!
    return sum(range(min(a, b), max(a, b) + 1))
##range (min(a, b), max(a, b) + 1) > cria uma sequencia de numeros, a funçaõ min retorna o menor numero
## dois dois numeros, enquanto max retorna o maior. O +1 é necessario porque range não inclui o ultimo 
## numero...indice 0...1...2...etc

##EXERCICIO 16/100 > calcular o triple do numero
def row_sum_odd_numbers(n):
    #your code here
    return n ** 3

##EXERCICIO 17/100 > saber se sua nota é maior que a média da turma
def better_than_average(class_points, your_points):
    # Your code here
    return your_points > sum(class_points) / len(class_points)
    
## sum(class_points) / len(class_points)
## se sua nota for > que a divisão da soma de todos pontos por quantidade de pessoas que fizeram os pontos

##EXERCICIO 18/100 > remover (#) usando split
def remove_url_anchor(url):
    # TODO: complete
    return url.split("#")[0]
## split separa em duas parte o URL, 0 e 1, onde 0 retorna sem #

##EXERCICIO 19/100 > definir qual dos tres numeros inseridos ira ficar no meio > indice 0,1,2
def gimme(input_array):
    # Implement this function
    return input_array.index(sorted(input_array)[1])

##index > função que mostra a posição do elemento
##sorted > organiza de forma crescente 
##chamada da função > print(gimme([6,2,3]))




