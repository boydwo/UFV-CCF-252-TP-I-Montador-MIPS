
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
    vetor_linha = line.replace("\n", "")  # substitui o \n por um espaço
    vetor_linha = vetor_linha.replace(",", "")  #retira a(virgula)
    vetor_linha = vetor_linha.split(" ") # muda o vetor string de caracter por um vetor palavra

    saida = [0] * 6

#entrada em add | sub | and | or | nor |
    if ((vetor_linha[0] == "add") or (vetor_linha[0]== "sub") or (vetor_linha[0]=="and") or (vetor_linha[0]=="or") or (vetor_linha[0]=="nor") ):
       
        #definindo o funct
        if(vetor_linha[0] == "add"):
            saida[5] = 32 #32 decimal
        elif (vetor_linha[0] == "sub"):
            saida[5] = 34 #34 decimal
        elif(vetor_linha[0] == "and"):
            saida[5] = 36 #36 decimal
        elif(vetor_linha[0] == "or"):
            saida[5] = 37 #37 decimal
        elif(vetor_linha[0] == "nor"):
            saida[5] = 39 #39 decimal

        # posição dos registradores $s
        # rd = $s, posição 1, registrador de destino
        if (vetor_linha[1] == '$s0'):
            saida[3] = 16
        if (vetor_linha[1] == '$s1'):
            saida[3] = 17
        if ((vetor_linha[1]) == '$s2'):
            saida[3] = 18
        if ((vetor_linha[1]) == '$s3'):
            saida[3] = 19
        if ((vetor_linha[1]) == '$s4'):
            saida[3] = 20
        if ((vetor_linha[1]) == '$s5'):
            saida[3] = 21
        if ((vetor_linha[1]) == '$s6'):
            saida[3] = 22
        if ((vetor_linha[1]) == '$s7'):
            saida[3] = 23

        # rs, $s, posição 2, registrador operando 1
        if ((vetor_linha[2]) == '$s0'):
            saida[1] = 16
        if ((vetor_linha[2]) == '$s1'):
            saida[1] = 17
        if ((vetor_linha[2]) == '$s2'):
            saida[1] = 18
        if ((vetor_linha[2]) == '$s3'):
            saida[1] = 19
        if ((vetor_linha[2]) == '$s4'):
            saida[1] = 20
        if ((vetor_linha[2]) == '$s5'):
            saida[1] = 21
        if ((vetor_linha[2]) == '$s6'):
            saida[1] = 22
        if ((vetor_linha[2]) == '$s7'):
            saida[1] = 23

        # rt, $s,  posição 3, registrador operando 2
        if ((vetor_linha[3]) == '$s0'):
            saida[2] = 16
        if ((vetor_linha[3]) == '$s1'):
            saida[2] = 17
        if ((vetor_linha[3]) == '$s2'):
            saida[2] = 18
        if ((vetor_linha[3]) == '$s3'):
            saida[2] = 19
        if ((vetor_linha[3]) == '$s4'):
            saida[2] = 20
        if ((vetor_linha[3]) == '$s5'):
            saida[2] = 21
        if ((vetor_linha[3]) == '$s6'):
            saida[2] = 22
        if ((vetor_linha[3]) == '$s7'):
            saida[2] = 23
        
        # posição dos registradores $t
        # rd, $t posicao 1, registrador destino
        if ((vetor_linha[1]) == '$t0'):
            saida[3] = 8
        if ((vetor_linha[1]) == '$t1'):
            saida[3] = 9
        if ((vetor_linha[1]) == '$t2'):
            saida[3] = 10
        if ((vetor_linha[1]) == '$t3'):
            saida[3] = 11
        if ((vetor_linha[1]) == '$t4'):
            saida[3] = 12
        if ((vetor_linha[1]) == '$t5'):
            saida[3] = 13
        if ((vetor_linha[1]) == '$t6'):
            saida[3] = 14
        if ((vetor_linha[1]) == '$t7'):
            saida[3] = 15

        # rs, $t, posicao 2, resgistrador operando 1
        if ((vetor_linha[2]) == '$t0'):
            saida[1] = 8
        if ((vetor_linha[2]) == '$t1'):
            saida[1] = 9
        if ((vetor_linha[2]) == '$t2'):
            saida[1] = 10
        if ((vetor_linha[2]) == '$t3'):
            saida[1] = 11
        if ((vetor_linha[2]) == '$t4'):
            saida[1] = 12
        if ((vetor_linha[2]) == '$t5'):
            saida[1] = 13
        if ((vetor_linha[2]) == '$t6'):
            saida[1] = 14
        if ((vetor_linha[2]) == '$t7'):
            saida[1] = 15

        # rt, $t posicao 3, registrador operando 2
        if ((vetor_linha[3]) == '$t0'):
            saida[2] = 8
        if ((vetor_linha[3]) == '$t1'):
            saida[2] = 9
        if ((vetor_linha[3]) == '$t2'):
            saida[2] = 10
        if ((vetor_linha[3]) == '$t3'):
            saida[2] = 11
        if ((vetor_linha[3]) == '$t4'):
            saida[2] = 12
        if ((vetor_linha[3]) == '$t5'):
            saida[2] = 13
        if ((vetor_linha[3]) == '$t6'):
            saida[2] = 14
        if ((vetor_linha[3]) == '$t7'):
            saida[2] = 15

    print(saida)


arq.close()
