#exemplo de leitura + divisão do vetor de forma correta

#contador de linhas do arquivo
arq = open('exemplo_entrada.asm', 'r')
cont = 0
arquivo = arq.readlines()
for line in arquivo:
    cont = cont + 1
print(cont)
#FOR PEGANDO LINHA POR LINHA
for line in arquivo:

    vetor_linha = line.split(" ")
    vetor_linha = line.replace("\n", " ")  # substitui o \n por um espaço
    vetor_linha = vetor_linha.replace(",", "")  #retira a(virgula)
    vetor_linha = vetor_linha.split(" ") # muda o vetor string de caracter por um vetor palavra

    print(vetor_linha)

arq.close()



#fim contador de linhas
#arq = open('exemplo_entrada.asm', 'r')
#entrada = arq.read()
#print (entrada)
#entrada = entrada.replace(",","")  #retira a(virgula)
#entrada = entrada.replace("\n"," ") #substitui o \n por um espaço
#entrada = entrada.split(" ")  #dividindo a string em posições do vetor
#print(entrada)
#arq.close()