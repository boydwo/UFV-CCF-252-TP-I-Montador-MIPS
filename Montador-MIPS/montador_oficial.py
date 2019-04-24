
#contador de linhas do arquivo
arq = open('exemplo_entrada.asm', 'r')
cont = 0
arquivo = arq.readlines()

# contado linhas do arquivo
'''for line in arquivo:
    cont = cont + 1
print(cont) '''

#FOR PEGANDO LINHA POR LINHA
for line in arquivo:
    #TRATAMENTO
    vetor_linha = line.split(" ")
    vetor_linha = line.replace("\n", " ")  # substitui o \n por um espaço
    vetor_linha = vetor_linha.replace(",", "")  #retira a(virgula)
    vetor_linha = vetor_linha.split(" ") # muda o vetor string de caracter por um vetor palavra


    #posição 1 da entrada em add | sub | and | or | nor |
    if ((vetor_linha[0] == "add") | (vetor_linha[0] == "sub") | (vetor_linha[0] == "and") | (vetor_linha[0] == "or") | (vetor_linha[0] == "nor")):
        saida = [0] * 6
        if(vetor_linha[0] == "add"):
            saida[5] = '100001' #32
        elif (vetor_linha[0] == "sub"):
            saida[5] = "100010" #34
        elif(vetor_linha[0] == "and"):
            saida[5] = "100100" #36
        elif(vetor_linha[0] == "or"):
            saida[5] == "100101" #37
        elif(vetor_linha[0] == "nor"):
            saida[5] == "100111" #39
    print(vetor_linha)
    print(saida)


arq.close()
