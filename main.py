automato = open("automato.txt", "r")

estados = automato.readline().split()

alfabeto = automato.readline().split()

estadoInicial = automato.readline().split()

estadosFinais = automato.readline().split()

matriz = []
linha = automato.readline().split()
while len(linha) > 0:
  matriz.append(linha)
  linha = automato.readline().split()
print("Matriz")
for i in matriz:
  print(i)

#ENTRADAS
entrada = open("entrada.txt", "r")

entradas = []
linha = entrada.readline().rstrip()
while len(linha) > 0:
  entradas.append(linha)
  linha = entrada.readline().rstrip()
print("Entradas:")
for i in entradas:
  print(i)

saida = open("saida.txt", "x")

for i in entradas:
  atual = estadoInicial[0]
  for y in i:
    
    #estado
    for x in range(len(estados)):
      if atual == str(estados[x]):
        linha = x
    
    #alfabeto           
    for x in range(len(alfabeto)):
      if y == alfabeto[x]:
        coluna = x
    
    atual = matriz[coluna][linha]
      
  contem = False
  for i in estadosFinais:
     if i == atual:
       contem = True
       saida.write("ACEITO\n")
  if contem == False:
    saida.write("NEGADO\n")

automato.close()
entrada.close()
saida.close()


