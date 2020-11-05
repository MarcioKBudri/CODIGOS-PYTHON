entrada= input()
busca= input()
soma=0
for i in (entrada):
  if i ==busca:
    soma+=1
if soma !=0:
  print ('O caractere buscado ocorre {} vezes na sequencia'.format(soma))
else:
  print ('Caractere nao encontrado.')
