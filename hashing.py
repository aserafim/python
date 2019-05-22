""""
Implementando funcoes de hashing

Abaixo o metodo do meio do quadrado, considerando tabelas com 1000 posicoes
ou seja, as posicoes variam de 0 a 999
"""

def hashGM(key):
    sqr = key * key
    aux = sqr
    i = 0               #counter
    npos = 0            #contador de algarismos
    while (aux > 0):
        aux = aux // 10
        npos += 1
    print("Numero de algarismos:", npos)                #sai com a quantidade de algarismos de sqr
    if (npos < 4):                                      #se o numero tiver menos de 4 algarismos
        return sqr                                      #sua posicao na tabela sera o proprio nro
    aux = sqr
    middle = npos // 2
    print("Posicao do meio:", middle)                    #calcula o meio do nro
    while(i < middle):
        aux //= 10
        i += 1
        print("Valor de i:", i)
    return aux % 1000

print("Posicao da tabela: ", hashGM(258))
