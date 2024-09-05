import os, funcoes

def tabela(msg):
    tam = len(msg) + 4
    print("-" * tam)
    print(f"  {msg}")
    print("-" * tam)
    print("|  1.Ganho de peso..............|")
    print("|  1.Perca de peso rapidamente..|")
    print("|  2.Emagrecer..................|")
    print("|  3.Manter o peso..............|")
    print("-" * tam)


def dieta():
    p = int(input("Qual seu objetivo de acordo com a tabela ? "))
    if p == 1:
        print("""\nDieta para GANHO DE PESO:

Aqui está um plano de refeições de aproximadamente 2500 calorias, dividido em 5 refeições diárias:
 
Café da Manhã--6:30--
- 2 fatias de pão integral (140 calorias)
- 2 ovos mexidos (140 calorias)
- 1/2 abacate (120 calorias)
- 1 xícara de morangos (50 calorias)
- 1 xícara de café preto (sem calorias) ou chá verde (sem calorias)

*Total: 450 calorias*

Lanche da Manhã--10:00--
- 1 maçã média (95 calorias)
- 1 iogurte grego natural (200g) (120 calorias)
- 1 colher de sopa de mel (60 calorias)

*Total: 275 calorias*

Almoço--12:30--
- 150g de peito de frango grelhado (165 calorias)
- 1 xícara de arroz integral cozido (215 calorias)
- 1 xícara de brócolis no vapor (55 calorias)
- 1 colher de sopa de azeite de oliva (40 calorias) - para temperar
- 1/2 xícara de feijão preto cozido (100 calorias)

*Total: 575 calorias*

Lanche da Tarde--16:00--
- 1 punhado de nozes (30g) (200 calorias)
- 1 banana média (105 calorias)
- 1 colher de sopa de manteiga de amendoim (90 calorias)

*Total: 395 calorias*

Jantar--20:00--
- 200g de salmão grelhado (400 calorias)
- 1 xícara de quinoa cozida (220 calorias)
- 1 xícara de espinafre refogado (40 calorias)
- 1 batata-doce média assada (120 calorias)

*Total: 780 calorias*

Ceia--22:00--
- 1 porção de queijo cottage (200g) (200 calorias)
- 1 punhado de frutas vermelhas (50 calorias)
- 1 colher de chá de sementes de chia (30 calorias)

*Total: 280 calorias*

### Calorias Totais
- Café da Manhã: 450 calorias
- Lanche da Manhã: 275 calorias
- Almoço: 575 calorias
- Lanche da Tarde: 395 calorias
- Jantar: 780 calorias
- Ceia: 280 calorias
- Total do dia: 2755 calorias""")
    elif p == 2:
        print("""\nDieta para PERCA DE PESO RAPIDAMENTE 

Aqui está um exemplo de plano alimentar de 1500 calorias para um dia. Lembre-se de que é importante ajustar as porções e os alimentos às suas necessidades nutricionais e preferências pessoais.

# Café da Manhã--6:30--
- 1 fatia de pão integral (70 calorias)
- 1 ovo cozido (70 calorias)
- 1 maçã média (95 calorias)
- 1 xícara de café preto (0 calorias)

*Total:* 235 calorias

# Lanche da Manhã--10:00--
- 1 iogurte grego desnatado (150g) (100 calorias)
- 1 colher de chá de mel (21 calorias)

*Total:* 121 calorias

# Almoço--12:30--
- Salada verde com tomate e pepino (2 xícaras) (50 calorias)
- 1 peito de frango grelhado (150g) (250 calorias)
- 1/2 xícara de arroz integral cozido (110 calorias)
- 1/2 xícara de brócolis cozidos (25 calorias)

*Total:* 535 calorias

# Lanche da Tarde--16:00--
- 1 punhado de nozes (30g) (180 calorias)
- 1 laranja média (62 calorias)

*Total:* 242 calorias

# Jantar--20:00--
- 1 filé de peixe assado (150g) (200 calorias)
- 1/2 xícara de quinoa cozida (110 calorias)
- 1 xícara de espinafre refogado com alho (60 calorias)

*Total:* 370 calorias

# Ceia--22:00--
- 1 fatia de melancia (200g) (60 calorias)

*Total:* 60 calorias

### Calorias Totais
- Café da Manhã: 235 calorias
- Lanche da Manhã: 121 calorias
- Almoço: 535 calorias
- Lanche da Tarde: 242 calorias
- Jantar: 370 calorias
- Ceia: 60 calorias
- Total do Dia: 1.563 calorias
""")
    elif p == 3:
        print("""\nDieta para EMAGRECER: 

Aqui está um plano de refeições de aproximadamente 1800 calorias, dividido em 5 refeições diárias:

# Café da Manhã--6:30--
- 1 fatia de pão integral (70 calorias)
- 1 ovo cozido (70 calorias)
- 1/2 abacate (120 calorias)
- 1 xícara de morangos (50 calorias)

*Total: 310 calorias*

# Lanche da Manhã--10:00--
- 1 maçã média (95 calorias)
- 1 iogurte grego natural (150g) (90 calorias)
- 1 colher de sopa de mel (60 calorias)

*Total: 245 calorias*

# Almoço--12:30--
- 120g de peito de frango grelhado (140 calorias)
- 3/4 xícara de arroz integral cozido (160 calorias)
- 1 xícara de brócolis no vapor (55 calorias)
- 1/4 xícara de feijão preto cozido (50 calorias)

*Total: 445 calorias*

# Lanche da Tarde--16:00--
- 1 punhado de amêndoas (15g) (105 calorias)
- 1 banana média (105 calorias)

*Total: 210 calorias*

# Jantar--20:00--
- 150g de peito de frango grelhado (165 calorias)
- 3/4 xícara de quinoa cozida (165 calorias)
- 1 xícara de espinafre refogado (40 calorias)

*Total: 370 calorias*

# Ceia--22:00--
- 1 porção de ricota (100g) (150 calorias)
- 1 maçã pequena (77 calorias)

*Total: 227 calorias*
              
### Totais do Dia
- Café da Manhã: 310 calorias
- Lanche da Manhã: 245 calorias
- Almoço: 445 calorias
- Lanche da Tarde: 210 calorias
- Jantar: 370 calorias
- Ceia: 227 calorias
- Total do dia: 1.807 calorias
""")
    elif p == 4:
        print("""\nDieta para MANTER O PESO: 

# Café da Manhã--6:30--
- 1 fatia de pão integral (70 calorias)
- 1 ovo mexido (70 calorias)
- 1/2 abacate (120 calorias)
- 1 xícara de morangos (50 calorias)
- 1 xícara de café preto (sem calorias) ou chá verde (sem calorias)

*Total: 310 calorias*

# Lanche da Manhã--10:00--
- 1 maçã média (95 calorias)
- 1 iogurte grego natural (150g) (90 calorias)
- 1 colher de sopa de mel (60 calorias)

*Total: 245 calorias*

# Almoço--12:30--
- 150g de peito de frango grelhado (165 calorias)
- 1 xícara de arroz cozido (215 calorias)
- 1 xícara de brócolis no vapor (55 calorias)
- 1/2 xícara de feijão preto cozido (100 calorias)

*Total: 575 calorias*

# Lanche da Tarde--16:00--
- 1 punhado de nozes (30g) (200 calorias)
- 2 banana média (210 calorias)

*Total: 410 calorias*

# Jantar--20:00--
- 150g de peito de frango grelhado (165 calorias)
- 10 colheres de baião (350 calorias)
- 1 xícara de espinafre refogado (40 calorias)

*Total: 660 calorias*

# Ceia--22:00--
- 1 porção de queijo cottage (150g) (150 calorias)
- 1 punhado de frutas vermelhas (50 calorias)

*Total: 200 calorias*

### Totais do Dia
- Café da Manhã: 310 calorias
- Lanche da Manhã: 245 calorias
- Almoço: 575 calorias
- Lanche da Tarde: 410 calorias
- Jantar: 660 calorias
- Ceia: 200 calorias
- Total do dia: 2.400 calorias

Aqui estão algumas opções de substituição para cada refeição, mantendo o total próximo de 2000 calorias:

Café da Manhã
~~Substituições~~
- 1 fatia de pão integral (70 calorias)
- 1/2 xícara de aveia cozida (150 calorias)
- 1 ovo mexido (70 calorias)
- 1 clara de ovo cozida (17 calorias) + 1 fatia de queijo magro (50 calorias)
- 1/2 abacate (120 calorias) 
- 1/2 banana média (60 calorias) + 1 colher de sopa de manteiga de amendoim (90 calorias)
- 1 xícara de morangos (50 calorias) 
- 1/2 xícara de framboesas (30 calorias)

~~Exemplo de substituição~~
- 1/2 xícara de aveia cozida (150 calorias)
- 1 clara de ovo cozida (17 calorias) + 1 fatia de queijo magro (50 calorias)
- 1/2 banana média (60 calorias) + 1 colher de sopa de manteiga de amendoim (90 calorias)
- 1/2 xícara de framboesas (30 calorias)

*Total: 397 calorias*

Lanche da Manhã
~~Substituições~~
- 1 maçã média (95 calorias) 
- 1 pera média (100 calorias)
- 1 iogurte grego natural (150g) (90 calorias) 
- 1 iogurte natural desnatado (200g) (100 calorias)
- 1 colher de sopa de mel (60 calorias) 
- 1 colher de sopa de xarope de agave (60 calorias)

~~Exemplo de substituição~~
- 1 pera média (100 calorias)
- 1 iogurte natural desnatado (200g) (100 calorias)
- 1 colher de sopa de xarope de agave (60 calorias)

*Total: 260 calorias*

Almoço
~~Substituições~~
- 150g de peito de frango grelhado (165 calorias) 
- 150g de tofu grelhado (130 calorias)
- 1 xícara de arroz integral cozido (215 calorias)
- 1 xícara de cuscuz (176 calorias)
- 1 xícara de brócolis no vapor (55 calorias) 
- 1 xícara de couve-flor cozida (25 calorias)
- 1 colher de chá de azeite de oliva (40 calorias) 
- 1 colher de sopa de vinagre balsâmico (14 calorias)

~~Exemplo de substituição~~
- 150g de tofu grelhado (130 calorias)
- 1 xícara de cuscuz (176 calorias)
- 1 xícara de couve-flor cozida (25 calorias)
- 1 colher de sopa de vinagre balsâmico (14 calorias)

*Total: 345 calorias*

Lanche da Tarde
~~Substituições~~
- 1 punhado de nozes (30g) (200 calorias) 
- 1 porção de amêndoas (30g) (160 calorias) 
- 1 iogurte grego (150g) (90 calorias)
- 1 banana média (105 calorias) 
- 1 maçã pequena (77 calorias) 
- 1 pera pequena (80 calorias)

~~Exemplo de substituição~~
- 1 porção de amêndoas (30g) (160 calorias)
- 1 maçã pequena (77 calorias)

*Total: 237 calorias*

Jantar
~~Substituições~~
- 150g de salmão gr""")
    else:
        print("OPÇÃO NÃO ENCONTRADA NA TABELA!")


def exercicio():
    pergunta = input("\nVocê quer uma lista de exercícios ? (S/N): ").upper()
    if pergunta == "S":
        exercicios = ["Agachamento", "Flexão", "Corrida", "Abdominal", "Pular corda", "Prancha"]
        horas = float(input("Quantas horas você pode dedicar aos exercícios (SÓ O NÚMERO DE HORAS, SEM LETRAS) ? "))
        min_totais = horas * 60
        tempo_por_exercicio = min_totais / len(exercicios)
        
        print("Programação de exercícios:")
        for x, exercicio in enumerate(exercicios, 1):
            print(f"{x}. {exercicio}: {tempo_por_exercicio:.2f} minutos")
    elif pergunta == "N":
        print("Programa encerrado...")
    else:
        print("Escolha não aceita!")


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
