# -- coding: utf-8 --
"""
Created on Tue Apr 16 18:12:55 2019

@author: Pedro 
"""
# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Pedro Henrique Menezes de Oliveira, pedrohmo@al.insper.edu.br
# - aluno B: Eiki Luis Yamashiro Batista dos Santos, eikily@insper.edu.br

import time

def tempo(t):
    time.sleep(t)

def printa_status(Vj,Dj,Ej,Level):
    print('\033[4m'+'Status'+'\033[0;0m')
    tempo(2)
    print("Level: {0}".format(Level))
    print("Vida: {0}".format(Vj))
    print("Damage: {0}".format(Dj))
    print("Armour: {0}".format(Ej))
    return ''
    
def batalha(Vj,Dj,Ej,Vm,Dm,Em):
    while Vm>0 and Vj>0:
        Vm=Vm-(Dj-Em)
        Vj=Vj-(Dm-Ej)
    if Vj<=0:
        return "Você morreu"
    else:
        return Vj
    
def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "quarto andar": "Tomar elevador e ir para o quarto andar",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            }
        },
        "quarto andar": {
                "titulo": "Andar do cansaço",
                "descricao": "Você está no saguão do quarto andar",
                "opcoes":{
                        "inicio": "Voltar para o saguao de entrada",
                        "lab de info": "Ir para o laboratório de Informática",
                        "lab de quim": "Ir para o laboratório de Química",
                        "sala 405": "Ir para a sala 405",
                        "andar professor": "Tomar elevador para andar do professor"
            }
        },
        "lab de info": {
                "título": "Laboratório de Informática",
                "descricao": "Você está no lab de informática e percebe que o professor de "
                "design de software esqueceu um pen-drive... Com o Python 4.0!!!!",
                "opcoes":{
                         "Pegar o pen-drive": "Conseguir o uso exclusivo do Python 4.0 (+5 de armour)",
                         "quarto andar": "Voltar para o saguão do quarto andar"
            }
        },
        "lab de quim": {
                "título": "Laboratório de Química",
                "descricao": "Você está no lab de química",
                "opcoes": {
                        "quarto andar": "Voltar para o saguão do quarto andar"
            }
        },
        "sala 405": {
                "título": "Sala 405",
                "descricao": "Você está na sala da tortura",
                "opcoes": {
                        "quarto andar": "Voltar para o saguão do quarto andar"
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    tempo(5)
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    tempo(5)
    Vj=150
    Dj=20
    Ej=5
    Level=1
    print(printa_status(Vj,Dj,Ej,Level))
    cenarios, nome_cenario_atual = carregar_cenarios()
    i=0
    j=0
    Inventario=[]
    game_over = False
    while not game_over:
        escolha = cenarios[nome_cenario_atual]
        k=0
        for nomes,c in escolha.items():
            if nomes!="opcoes":
                print (c)
            if k==0:
                print ("-"*len(c))
                k+=1

        opcoes = escolha['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            if escolha==cenarios ['biblioteca']:
                if j==0:
                    print ("Você estava andando na biblioteca e acabou achando"
                           " uma maçã para dar para seu professor quando for pedir o"
                           " adiamento do EP")
                    tempo(2)
                    Inventario.append("Maçã")
                    print ('\033[35m'+'Maçã adicionada ao inventário'+'\033[0;0m')
                    tempo(2)
                
            elif escolha==cenarios['inicio']:
                if i==1:
                    print("Você voltou ao Saguão de entrada do Insper e"
                        " se deparou com a Next fazendo uma propaganda e dando"
                        " ingressos para o cinema")
                    tempo(4)
                    ingresso=input("Deseja pegar um ingresso?(sim/não)")
                    if ingresso=="sim":
                        print("Um dos funcionários da Next chega em você e"
                              " pergunta:")
                        tempo(2)
                        print("'Você conhece a Next?'")
                        tempo(1)
                        print("Você com pressa responde que sim")
                        tempo(3)
                        print('\033[32m'+'COMO ASSIM VOCÊ JÁ CONHECE A NEXT?!?!?!'+'\033[0;0m')
                        tempo(2)
                        print("O funcionário vira um monstro")
                        tempo(2)
                        print("Opções: Combater o monstro ou perder 15 de dano de ataque")
                        tempo(2)
                        op=input('O que deseja fazer?(combate/fugir)')
                        tempo(2)
                        if op=='combate':
                            print("Status do monstro")
                            Levelm=2
                            Vm=50
                            Dm=10
                            Em=0
                            print(printa_status(Vm,Dm,Em,Levelm))
                            tempo(3)
                            print("Você está batalhando contra o Monstro do Next")
                            tempo(1)
                            print('...')
                            tempo(1)
                            print('Você ganhou a batalha!')
                            batalha_next=batalha(Vj,Dj,Ej,Vm,Dm,Em)
                            tempo(1)
                            print('\033[33m'+'Você subiu de nível!'+'\033[0;0m')
                            Level+=1
                            tempo(1)
                            print(printa_status(batalha_next,Dj,Ej,Level))
                            tempo(2)
                            print("O monstro ao morrer dropou um cartão débito da Next")
                            tempo(2)
                            print("Há um saldo de 50 reais nele")
                        else:
                            print("'\033[31m'+'Você perdeu 15 de dano de ataque'+'\033[0;0m'")
                            Dj=Dj-15
                            print(printa_status(Vj,Dj,Ej,Level))
                i+=1
            elif escolha=="professor":
                print("Ao entrar na sala você se depara com o monstro"
                    " do Python")
                print("'Olá, caro aluno, o que deseja?'")
                decisao_final=input("O que deseja fazer?(Abrir inventário/Conversar/"
                                  "Sair no soco)")
                while decisao_final!="Sair no soco":
                    if decisao_final=="Abrir inventário":
                        print("Você olha no inventário e vê seus itens")
                        i=0
                        while i<len(Inventario):
                            print(Inventario[i])
                            i+=1
                            escolha=input("Deseja usar alguma coisa dessas?(digite um dos itens)")
                            if escolha in Inventario:
                                if escolha=="Maçã":
                                    print("Você deu a maçã para o professor")
                                    print("Ele, muito agradecido, nega sua oferta dizendo"
                                          " que não gosta de maçãs")
            elif escolha==cenarios["andar professor"]:
                tempo(5)
                print("Ao chegar no andar do professor percebe que há"
                        "uma força estranha no ar...")
                tempo(4)
                print("Na entrada da sala do professor há uma espada "
                        "encravada numa pilha de provas...")
                tempo(4)
                print("Ao chegar mais perto você observa e vê que são"
                        "provas de Python e observa que há uma frase escrita"
                        "na espada")
                tempo(4)
                print("O aluno que conseguir retirar a "
                        "espada encravada nesta pilha de provas será o capaz"
                        "de ser chamado de oráculo do Python")
                tempo(5)
                espada=input("Deseja tentar retirar a espada?(sim/não)")
                if espada=="sim":
                    print ("Você puxa com tanta força a espada que quando ela"
                           " sai da pilha de provas te corta no braço")
                    tempo(4)
                    print('\033[33m'+'Ao analisar a espada você ganha +20 de dano de ataque'+'\033[0;0m')
                    Inventario.append("espada")
                    tempo(3)
                    print('\033[35m'+'Espada adicionada ao inventário'+'\033[0;0m')
                else:
                    print("Então vá em frente e abra essa porta")
            elif escolha==cenarios["quarto andar"]:
                tempo(3)
                print("O quarto andar pode ser um ótimo lugar para aumentar seu inventário")
            elif escolha==cenarios["lab de info"]:
                tempo(3)
                print("")
                #for k,v in opcoes.items():
                    #del
            for k,v in opcoes.items():
                print(k+': '+v)
            escolha=input('Para onde deseja ir?')
            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")

# Programa principal.
_name_= "_main_"
if _name_ == "_main_":
    main()


