#print("Hello, World!")

print('Olá! \nHoje vou te ajudar a calcular seu peso ideal através do seu Índice de Massa Corporal.\n(Use . para casas decimais)')
peso = float(input('Qual seu peso em kg? '))
altura = float(input('Qual sua altura em m? '))

imc = round(peso / (altura ** 2),2)

if imc < 18.5:
    print('Abaixo do Peso\nConsulte um médico e um nutricionista!')
elif 18.5 <= imc < 24.9:
    print('Peso ideal')
elif 25 <= imc < 29.9:
    print('Acima do Peso\nConsulte um médico e um nutricionista!')
elif 30 <= imc < 34.9:
    print('Obesidade Grau I\nConsulte um médico e um nutricionista!')
elif 35 <= imc < 39.9:
    print('Obesidade Grau II\nConsulte um médico e um nutricionista!')
else:
    print('Obesidade Grau III\nConsulte um médico e um nutricionista!')