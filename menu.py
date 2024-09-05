import os, funcoes

os.system("clear")
altura = float(input("Digite sua altura: "))
pes = float(input("Digite seu peso: "))
IMC = pes / altura ** 2

print("Seu IMC é {:.2f}".format(IMC))

if IMC < 18.5:
    print("MAGREZA, IMC {:.2f}".format(IMC))
    tabela("DE ACORDO COM SEU IMC, O IDEAL É QUE AUMENTE O GANHO DE PESO!")
    dieta()
    input("\nTecle ENTER para continuar...")
    os.system("clear")
    exercicio()
elif IMC <= 24.9:
    print("NORMAL, IMC {:.2f}".format(IMC))
    tabela("DE ACORDO COM SEU IMC, VOCÊ PODE OPTAR ENTRE AS OPÇÕES DA TABELA!")
    dieta()
    input("\nTecle ENTER para continuar...")
    os.system("clear")
    exercicio()
elif IMC <= 29.9:
    print("SOBREPESO, IMC {:.2f}".format(IMC))
    tabela("DE ACORDO COM SEU IMC, O IDEAL É QUE VOCÊ EMAGREÇA, POIS ESTA PERTO DA OBESIDADE!")
    dieta()
    input("\nTecle ENTER para continuar...")
    os.system("clear")
    exercicio()
elif IMC <= 39.9:
    print("OBESIDADE, IMC {:.2f}".format(IMC))
    tabela("DE ACORDO COM SEU IMC, O IDEAL É QUE VOCÊ EMAGREÇA, POIS ESTA PERTO DA OBESIDADE GRAVE!")
    dieta()
    input("\nTecle ENTER para continuar...")
    os.system("clear")
    exercicio()
else:
    print("OBESIDADE GRAVE, IMC {:.2f}".format(IMC))
    tabela("DE ACORDO COM SEU IMC, O IDEAL É QUE VOCÊ EMAGREÇA URGENTEMENETE, POIS CORRE RISCO DE VIDA!")
    dieta()
    input("\nTecle ENTER para continuar...")
    os.system("clear")
    exercicio()
