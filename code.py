print('-'*40)
print('Bem-vinde ao Triangulo Descobrinator! \nInforme três valores e eu direi se é um triângulo.')
print('-'*40)

while True:
    LadoA = int(input("Informe o valor do primeiro lado:"))
    LadoB = int(input("Informe o valor do segundo lado:"))
    LadoC = int(input("Informe o valor do terceiro lado:"))

    if LadoA < LadoB + LadoC and LadoC < LadoA + LadoB and LadoB < LadoC + LadoA:
        print(f'Os lados {LadoA},{LadoB},{LadoC} formam um triângulo!')
    else:
        print('Esses lados não formam um triângulo, pois um lado não é menor que a soma dos outros dois.')
    repeticao = input('Deseja informar novos valores? (Digite sim ou nao)')
    while repeticao != 'sim' and repeticao != 'nao':
        repeticao = input('Não entendi, digite apenas sim ou nao:')
    if repeticao == 'nao':
        print('Obrigade por usar o Triangulo Descobrinator! \nAté mais!')
        break
    
