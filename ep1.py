# -*- coding: utf-8 -*-
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
    print("Level: {0}".format(Level))
    print("Vida: {0}".format(Vj))
    print("Damage: {0}".format(Dj))
    print("Armour: {0}".format(Ej))
    
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
                "andar professor": "Tomar o elevador para o andar do professor",
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
        cenario_atual = cenarios[nome_cenario_atual]
        k=0
        for nomes,c in cenario_atual.items():
            if nomes!="opcoes":
                print (c)
            if k==0:
                print ("-"*len(c))
                k+=1

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            if cenario_atual==cenarios ['biblioteca']:
                if j==0:
                    print ("Você estava andando na biblioteca e acabou achando"
                           " uma maçã para dar para seu professor quando for pedir o"
                           " adiamento do EP")
                    Inventario.append("Maçã")
                    print ("Maçã adicionada ao inventário")
                
            elif cenario_atual==cenarios['inicio']:
                if i==1:
                    print("Você voltou ao Saguão de entrada do Insper e"
                        " se deparou com a Next fazendo uma propaganda e dando"
                        " ingressos para o cinema")
                    ingresso=input("Deseja pegar um ingresso?(sim/não)")
                    if ingresso=="sim":
                        print("Um dos funcionários da Next chega em você e"
                              " pergunta:")
                        print("'Você conhece a Next?'")
                        print("Você com pressa responde que sim")
                        tempo(3)
                        print('\033[31m'+'COMO ASSIM VOCÊ JÁ CONHECE A NEXT?!?!?!'+'\033[0;0m')
                        tempo(2)
                        print("O funcionário vira um monstro")
                        print("Opções: Combater o monstro ou perder 15 de dano de ataque")
                        op=input('O que deseja fazer?(combate/fugir)')
                        if op=='combate':
                            print("Status do monstro")
                            Levelm=2
                            Vm=50
                            Dm=10
                            Em=0
                            print(printa_status(Vm,Dm,Em,Levelm))
                            batalha_next=batalha(Vj,Dj,Ej,Vm,Dm,Em)
                            print("Você subiu de nível!")
                            Level+=1
                            print(printa_status(batalha_next,Dj,Ej,Level))
                            print("O monstro ao morrer dropou um cartão débito da Next")
                            print("Há um saldo de 50 reais nele")
                        else:
                            print("Você perdeu 15 de dano de ataque")
                            Dj=Dj-15
                            print(printa_status(Vj,Dj,Ej,Level))
                i+=1
            elif cenario_atual==cenarios["andar professor"]:
                print("Ao chegar no andar do professor percebe que há"
                        "uma força estranha no ar...")
                print("Na entrada da sala do professor há uma espada "
                        "encravada numa pilha de provas")
                print("Ao chegar mais perto você observa e vê que são"
                        "provas de Python e observa que há uma frase escrita"
                        "na espada")
                print("O aluno que conseguir retirar a"
                        "espada encravada nesta pilha de provas será o capaz"
                        "de ser chamado de oráculo do Python")
                espada=input("Deseja tentar retirar a espada?(sim/não)")
                if espada=="sim":
                    print ("Você puxa com tanta força a espada que quando ela"
                           " sai da pilha de provas te corta no braço")
                    print("Ao analisar a espada você ganha +20"
                          " de dano de ataque")
                    Inventario.append("espada")
                    print("Espada adicionada ao inventário")
                else:
                    print("Então vá em frente e abra essa porta")
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
if __name__ == "__main__":
    main()