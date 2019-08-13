# problem 1091

# k numero_casas
# m, n: cordenadas do ponto divisor
# k linhas seguinte:
#   X, Y: cordenadas das residencias
#   se apertar 0 encerra


X, Y = 0, 1

def row_input():
    return input().split()

def int_list(arraY):
    return [int(element) for element in arraY]

def esta_na_divisa(casa, divisa):
    global X, Y
    
    if casa[X] == divisa[X] or casa[Y] == divisa[Y]:
        return True
    return False

def regioes_do_quadrante(X_is_positive, Y_is_positive):
    regiao = ''
    regiao += 'N' if Y_is_positive else 'S'
    regiao += 'E' if X_is_positive else 'O'
    return regiao

    
def regiao_casa(casa, divisa):
    global X, Y

    X_is_positive = casa[X] > divisa[X]
    Y_is_positive = casa[Y] > divisa[Y]

    return regioes_do_quadrante(X_is_positive, Y_is_positive)


result = []
while True:
    numero_casas = int(input())
    if numero_casas == 0:
        break
    divisa = int_list(row_input())
    for numero_casa in range(numero_casas):
        casa = int_list(row_input())
        if esta_na_divisa(casa, divisa):
            result.append('divisa')
        else:
            result.append(regiao_casa(casa, divisa))
for answer in result:
    print(answer)

