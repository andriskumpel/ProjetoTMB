# COMO CALCULAR A TAXA METABÓLICA BASAL DE ACORDO COM A EQUAÇÃO DE HERRIS BENEDICT (MAIS CONCEITUADA)
# TMB ( 10 x Peso em Kg) + (6.25 x Altura em Cm) - (5 x idade) + 5
# MULTIPLICAR PELO NÍVEL DE ATIVIDADE: SEDENTÁRIO (*1.2), LEVEMENTE ATIVO (1 A 3 DIAS POR SEMANA) (*1.375), MODERADAMENTE ATIVO (3 A 5 DIAS POR SEMANA) (*1.65) , MUITO ATIVO (5 A 7 DIAS POR SEMANA) (*1.725), EXTREMAMENTE ATIVO (*1.9)

print('Olá! Seja bem vindo(a) a calculadora da Taxa Metabólica Basal (TMB). O cálculo é baseado na equação de Herris Benedict (mais conceituada atualmente). Vamos iniciar!')
nome = str(input('Como você se chama? '))
print('Legal! {}, agora vamos calcular a sua TMB.'.format(nome))
print('O cálculo da TMB é realizado com as seguintes informações: peso, altura, idade e nível de atividade física.')
peso = float(input('Para iniciarmos, digite o seu peso atual (apenas números, exemplo: 80): '))
altura = int(input('Agora digite a sua altura aproximada em cm (apenas números, exemplo: 187): '))
idade = int(input(('Quantos anos você tem, {}? (apenas números, exemplo: 28): '.format(nome))))
print('E para finalizar, vamos calcular qual é o nível de atividade física que você pratica. ')
print('1 - SEDENTÁRIO: pouca ou quase nenhuma atividade física na semana')
print('2 - LEVEMENTE ATIVO: 1 a 3 dias por semana')
print('3 - MODERADAMENTE ATIVO: 3 a 5 dias por seamana')
print('4 - MUITO ATIVO: 5 a 7 dias por semana')
print('5 - EXTREMAMENTE ATIVO: 7 dias por semana e mais de uma vez ao dia')
ativ = int(input('Agora digite qual nível de atividade você considera que pratica durante a semana (digite apenas o número correspondente):  '))
print('Calculando...')
tmb = (10 * peso) + (6.25 * altura) - (5 * idade) + 5
if ativ == 1:
    print('Sua Taxa Metabólica Basal é de: {}'.format(tmb * 1.2))
elif ativ == 2:
    print('Sua Taxa Metabólica Basal é de: {}'.format(tmb * 1.375))
elif ativ == 3:
    print('Sua Taxa Metabólica Basal é de: {}'.format(tmb * 1.65))
elif ativ == 4:
    print('Sua Taxa Metabólica Basal é de: {}'.format(tmb * 1.725))
else:
    print('Sua Taxa Metabólica Basal é de: {}'.format(tmb * 1.9))
print('Agora bora viver, {}!'.format(nome))