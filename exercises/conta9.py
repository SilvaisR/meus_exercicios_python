'''
Este exercício é o que estou tentando fazer em Java, vamos lá. Aqui eu preciso criar um programa que
leia dois valores, um será até aonde ele vai contar, o outro valor é o valor que vamos contar quantas vezes
apareceu durante toda a contagem. Por exemplo, quantos números 9 temos dentro de uma contagem de 0 até 100.
'''
print('Vamos começar, aqui você precisa digitar primeiro até onde você quer que o programa conte, \n'
      'em seguida você digita o número que você quer ir contando durante este percurso.')
print()
num1 = int(input('Digite o primeiro número que vai ser usado até onde iremos contar: '))
num2 = int(input('Digite o segundo número que vai ser o qual iremos ir contando quando aparecer: '))

lista = []
for i in range(0, num1 + 1):
    lista.append(str(i))

lista_nova = ''.join(lista)
contador = lista_nova.count(str(num2))

print(f'O número {num2}, apareceu {contador} vezes durante a contagem')
