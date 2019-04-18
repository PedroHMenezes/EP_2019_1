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

def printa_status(Vj,Dj,Ej,Level,nome):
    print('\033[4m'+'Status {0}'.format(nome)+'\033[0;0m')
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
                        "quarto andar": "Voltar para o saguão do quarto andar"
            }
        },
        "lab de quim": {
                "título": "Laboratório de Química",
                "descricao": "Algo de errado não está certo...",
                "opcoes": {
                        "quarto andar": "Voltar para o saguão do quarto andar"
            }
        },
        "sala 405": {
                "título": "Sala 405",
                "descricao": "Você está na sala da tortura",
                "opcoes": {
                        "inicio": "Voltar para o saguao de entrada",
                        "lab de info": "Ir para o laboratório de Informática",
                        "lab de quim": "Ir para o laboratório de Química",
                        "andar professor": "Tomar elevador para andar do professor",
                        "quarto andar": "Voltar para o saguão do quarto andar",
                        "biblioteca": "Ir para a biblioteca",
                        "sala comp": "Ir para a sala com computadores super caros (Predio Novo)",
                        "fablab": "Ir para o famoso fablab do Insper (Predio Novo)",
                        "saguao": "Ir para o saguão do prédio novo (Predio Novo)"
            }
        },
        "saguao": {
                "titulo": "Predio Novo",
                "descricao": "Você está no prédio de engenharia!",
                "opcoes": {
                        "sala comp": "Ir para a sala com muitos equipamentos eletrônicos",
                        "fablab": "Ir para o famoso fablab do Insper",
                        "Sala 405": "Ir para a sala 405 (Predio Velho)"
            }
        },
        "sala comp": {
                "titulo": "Sala do Milhão",
                "descricao": "Você está na sala do computador da NASA do Insper",
                "opcoes": {
                        "saguao": "Ir para o saguão do predio novo",
            }
        },
        "fablab": {
                "titulo": "Sala da Criação",
                "descricao": "Você está no famoso fablab do Insper",
                "opcoes": {
                        "saguao": "Ir para o saguão do predio novo"
            }
        },
        "banheiro": {
                "titulo": "Banheiro",
                "descricao": "Você está no banheirinho",
                "opcoes": {
                        "sala 405": "Ir para a sala 405"
            }
        },
    }
                        
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa ideia: vou só jogar um pouquinho/assistir Netflix/"
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
    print(printa_status(Vj,Dj,Ej,Level,''))
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
                    tempo(4)
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
                        print('\033[32m'+'O FUNCIONÁRIO VIRA UM MONSTRO'+'\033[0;0m')
                        tempo(2)
                        print("Opções: Combater o monstro ou perder 15 de dano de ataque")
                        tempo(2)
                        op=input('O que deseja fazer?(combate/fugir)')
                        tempo(2)
                        if op=='combate':                      
                            Levelm=2
                            Vm=50
                            Dm=10
                            Em=0
                            print(printa_status(Vm,Dm,Em,Levelm,"Monstro"))
                            tempo(3)
                            print("Você está batalhando contra o Monstro do Next")
                            tempo(2)
                            print('...')
                            tempo(2)
                            print("Grrrr...")
                            tempo(3)
                            print("...")
                            tempo(3)
                            print('\033[34m'+'Você ganhou a batalha!'+'\033[0;0m')
                            batalha_next=batalha(Vj,Dj,Ej,Vm,Dm,Em)
                            tempo(4)
                            print('\033[33m'+'Você subiu de nível!'+'\033[0;0m')
                            Level+=1
                            tempo(3)
                            print(printa_status(batalha_next,Dj,Ej,Level,''))
                            tempo(4)
                            print("O monstro ao morrer dropou um cartão débito da Next")
                            tempo(4)
                            print("Há um saldo de 50 reais nele")
                            Inventario.append("Cartão de débito")
                            tempo(4)
                            print('\033[35m'+'Cartão adicionado ao inventário'+'\033[0;0m')
                            tempo(4)
                        else:
                            print("'\033[31m'+'Você perdeu 15 de dano de ataque'+'\033[0;0m'")
                            Dj=Dj-15
                            print(printa_status(Vj,Dj,Ej,Level))
                i+=1
            elif escolha=="professor":
                print("Ao entrar na sala você se depara com o monstro"
                    " do Python")
                print("'Olá, caro aluno, o que deseja?'")
                decisao_final=input("O que deseja fazer?(Abrir inventário/Conversar)")
                while decisao_final!="Sair no soco":
                    if decisao_final=="abrir inventário":
                        print("Você olha no inventário e vê seus itens")
                        i=0
                        while i<len(Inventario):
                            print(Inventario[i])
                            i+=1
                        escolha=input("Deseja usar alguma coisa dessas?(digite um dos itens)")
                        if escolha in Inventario:
                            if escolha=="Maçã":
                                print("Você deu a maçã para o professor")
                                tempo(2)
                                print("Ele, muito agradecido, nega sua oferta dizendo"
                                      " que não gosta de maçãs")
                                tempo(3)
                                print("Maçã retorna ao seu inventário")
                                tempo(1)
                            elif escolha=="Cartão de débito":
                                print("Olha professor... Eu tenho esse cartão"
                                      " que você pode usar para pagar um almoção"
                                      " lá no Laranjinha. O que acha?")
                                tempo(3)
                                print(" 'Hmmm... Eu gosto do chef de lá... O que"
                                      " você quer em troca?")
                                tempo(2)
                                print("Você entrega o cartão para o professor")
                                tempo(1)
                                del Inventario["Cartão de débito"]
                                print("Então... Eu preciso de um adiamento do EP...")
                                tempo(2)
                                print(" 'Bom... Posso adiar para amanhã. O que acha?")
                                tempo(2)
                                print("Mas para amanhã é pouco tempo professor!!!")
                                tempo(1)
                                print("'Isso já é suficiente!' ")
                                tempo(1)
                                print("Você, sem expectativa de conseguir mais algum"
                                    " dia, começa a sair da sala")
                                tempo(2)
                                print(" 'Espere um pouco... Eu precisava que você guardasse"
                                    " segredo disso...' ")
                                tempo(2)
                                print("Você vendo uma oportunidade de adiamento do EP diz que "
                                    "irá falar pra todo mundo se o professor não adiar para um"
                                    " um maior prazo o EP")
                                tempo(4)
                                print(" 'Nesse caso... Não terei outra escolha' ")
                                tempo(1)
                                print("O professor vira o monstro do Python")
                                tempo(1)
                                
                            elif escolha=="pen drive":
                                print(" 'O que é isso? Um pen drive? O que tem ai dentro?")
                                tempo(2)
                                print("O Python 4.0...")
                                tempo(1)
                                print("O professor olha fixamente nos seus olhos e"
                                    " ao perceber a gravidade de um aluno possuir tais"
                                    " arquivos tão poderosos, vira o monstro do Python"
                                    " para proteger a mais nova edição do Python...")
                                tempo(6)
                                decisao_final="Sair no soco"
                            elif escolha=="espada":
                                print("Acho que não seria uma boa coisa oferecer"
                                    " essa espada a ele...")
                                tempo(2)
                                confirmacao=input("Quer mesmo oferecer isso a ele?(sim/não")
                                if confirmacao=="sim":
                                    print("Você mostra a espada para ele")
                                    tempo(2)
                                    print(" ' Uau... Você, então, conseguiu retirar a"
                                        " espada daquela pilha de provas...")
                                    tempo(2)
                                    print(" O professor sussura baixo, quase que de"
                                        " forma incompreensível:")
                                    tempo(2)
                                    print(" 'Sempre esperei por esse momento...' ")
                                    tempo(1)
                                    print("O professor vira o monstro do Python")
                                    tempo(1)
                                    decisao_final=="Sair no soco"
                                else:
                                    print("Acho melhor viu...")
                                    tempo(1)
                            elif escolha=="Alienware":
                                print("Ao mostrar o Alienware para o professor ele"
                                    " pergunta:")
                                tempo(2)
                                print(" 'Pra que isso?' ")
                                tempo(1)
                                print("Você gosta dessa linha de computadores da Dell?")
                                tempo(2)
                                print(" 'É, eles são de fato muito bons... Mas o que você"
                                    " quer com eles?")
                                tempo(3)
                                print("Poderia adiar o EP em troca de um desses...")
                                tempo(2)
                                print("O professor começa a rir com uma risada maligna, "
                                    "como se fosse um monstro...")
                                tempo(3)
                                brincadeira=input("Você está brincando comigo, certo?(sim/não)")
                                if brincadeira=="sim":
                                    print("De maneira muito séria, o professor diz:")
                                    tempo(2)
                                    print(" 'Pois não teve graça alguma' ")
                                    tempo(1)
                                    print("Ele vira o monstro do Python")
                                    tempo(1)
                                    decisao_final="Sair no soco"
                                else:
                                    print(" 'Como você consegue tentar me chantagear com isso?' ")
                                    tempo(2)
                                    print("Ele fica irado")
                                    tempo(1)
                                    print("O professor vira o monstro do Python")
                                    tempo(1)
                                    decisao_final="Sair no soco"
                            elif escolha=="banana dourada" or escolha=="barril explosivo" or escolha=="tronco atirador":
                                print("Não pode oferecer isso ao professor")
                        else:
                            print("Você está tentando usar um item que não"
                                    " está em seu inventário")
                    elif decisao_final=="Conversar":
                        print(" 'Certo... Sobre o que quer conversar?' ")
                        print("Preciso de um adiamento do EP...")
                        print(" 'O que você fez nesse tempo que tinha?' ")
                        print("Ahhh... eu decidi dar um descanso pra mim mesmo...")
                        print(" 'Acredito que isso não seja uma boa desculpa' ")
                        print("MAS EU PRECISO DE UM ADIAMENTO DO EP!!!!")
                        print(" 'VOCÊ NÃO TERÁ ADIAMENTO DO EP!' ")
                        print("O professor vira um monstro")
                        decisao_final="Sair no soco"
                if decisao_final=="Sair no soco":
                    
                
                
            elif escolha==cenarios["quarto andar"]:
                tempo(3)
                print("O quarto andar pode ser um ótimo lugar para aumentar seu inventário")
            elif escolha==cenarios["lab de info"]:
                tempo(3)
                print("Você olha para o pen-drive")
                tempo(3)
                print("...")
                tempo(3)
                print("O pen-drive olha para você")
                tempo(3)
                print("...")
                tempo(3)
                print('\033[33m'+'Você rouba o pen-drive'+'\033[0;0m')
                Inventario.append("pen-drive")
                tempo(2)
                print('\033[35m'+'Pen-drive adcionado ao inventário'+'\033[0;0m')
                tempo(2)
                print('\033[36m'+'+5 pontos de Armour'+'\033[0;0m')
                Ej+=5
            elif escolha==cenarios["lab de quim"]:
                tempo(3)
                print("Você está no laboratório de química e encontra um colega")
                tempo(2)
                print("Mas há algo de diferente nele")
                tempo(3)
                print('\033[32m'+'ELE ESTÁ INFECTADO COM UM VÍRUS!!!'+'\033[0;0m')
                Levelm=3
                Vm=60
                Dm=8
                Em=2
                tempo(3)
                print('\033[31m'+'ELE COMEÇA A TE ATACAR!'+'\033[0;0m')
                tempo(1)
                print('\033[31m'+'-1 ponto de vida'+'\033[0;0m')
                tempo(1)
                print('\033[31m'+'-1 ponto de vida'+'\033[0;0m')
                tempo(1)
                print('\033[31m'+'-1 ponto de vida'+'\033[0;0m')
                tempo(1)
                print('\033[31m'+'-1 ponto de vida'+'\033[0;0m')
                tempo(1)
                print('\033[31m'+'-1 ponto de vida'+'\033[0;0m')
                Vj=Vj-5
                op=input("O que deseja fazer?(combate/fugir)")
                if op=="combate":
                    a=batalha(Vj,Dj,Ej,Vm,Dm,Em)
                    print("A batalha começou!")
                    tempo(3)
                    print("...")
                    tempo(3)
                    print("Grr...")
                    tempo(3)
                    print('...')
                    tempo(4)
                    print('\033[34m'+'Você ganhou a batalha!'+'\033[0;0m')
                    tempo(1)
                    print("Pontos de vida após a batalha: {0}".format(a))
                    tempo(4)
                    print('\033[36m'+'Você subiu de nível!'+'\033[0;0m')
                    tempo(4)
                    Level+=1
                    print(printa_status(Vj,Dj,Ej,Level,''))
                    tempo(4)
                else:
                    print("Você fugiu")
            elif escolha==cenarios["sala 405"]:
                tempo(3)
                print("Você tenta abrir a porta da sala 405, mas ela não abre...")
                tempo(1)
                print("Então você faz mais força, e ela abre")
                tempo(2)
                print("Dentro da sala você percebe que há uma máquina de teleporte!")
                tempo(2)
                tel=input("Deseja entrar na máquina de teleporte?(sim/nao)")
                if tel=="sim":
                        print('\033[36m'+'Você está na máquina de teleporte'+'\033[0;0m')
                        tempo(3)
                elif tel=="nintendo":
                    print("Parece que você encontrou um easter egg...")
                    tempo(2)
                    print("Você decidiu ligar o nintendo da sala 405 e se deparou"
                        " com um novo jogo")
                    print("Esse é o Donkey Kong... Surpreso, quer jogar só uma partidinha")
                    tempo(3)
                    print("Ao vencer a fase, você desbloqueia um item...")
                    tempo(2)
                    print("Você pode escolher entre a banana dourada, barril explosivo e"
                        " tronco atirador")
                    tempo(3)
                    arma=input("Qual você escolhe?")
                    if arma=="banana dourada":
                        print("Ao analisar a banana dourada você percebe que ela é capaz"
                            " de recuperar sua vida completamente instantâneamente")
                        tempo(4)
                        Inventario.append("banana dourada")
                        print('\033[35m'+'Banana dourada adcionado ao inventário'+'\033[0;0m')
                        tempo(2)
                    elif arma=="barril explosivo":
                        print("Analisando o barril, percebe que ele é capaz de causar 250"
                            " de dano de ataque ao inimigo")
                        tempo(4)
                        Inventario.append("barril explosivo")
                        print('\033[35m'+'Barril explosivo adcionado ao inventário'+'\033[0;0m')
                        tempo(2)
                    else:
                        print("Ao analisar o tronco atirador você foi capaz de perceber que"
                            " ele pode atirar nozes(ilimitadas!) de longe")
                        tempo(4)
                        Inventario.append("tronco atirador")
                        print('\033[35m'+'Tronco atirador adcionado ao inventário'+'\033[0;0m')
                        tempo(2)
                else:
                    print("Você sai da sala 405")
                    tempo(2)
            elif escolha==cenarios["andar professor"]:
                tempo(5)
                print("Ao chegar no andar do professor percebe que há"
                        " uma força estranha no ar...")
                tempo(4)
                print("Na entrada da sala do professor há uma espada "
                        " encravada numa pilha de provas...")
                tempo(4)
                print("Ao chegar mais perto você observa e vê que são"
                        " provas de Python e observa que há uma frase escrita"
                        " na espada")
                tempo(4)
                print("O aluno que conseguir retirar a "
                        " espada encravada nesta pilha de provas será o capaz"
                        " de ser chamado de oráculo do Python")
                tempo(5)
                espada=input("Deseja tentar retirar a espada?(sim/não)")
                if espada=="sim":
                    print ("Você puxa com tanta força a espada que quando ela"
                           " sai da pilha de provas te corta no braço")
                    tempo(1)
                    print('\033[31m'+'-1 ponto de vida'+'\033[0;0m')
                    tempo(3)
                    print('\033[33m'+'Ao analisar a espada você ganha +20 de dano de ataque'+'\033[0;0m')
                    Inventario.append("espada")
                    tempo(3)
                    print('\033[35m'+'Espada adicionada ao inventário'+'\033[0;0m')
                    tempo(3)
                else:
                    print("Então vá em frente e abra essa porta")
            elif escolha==cenarios["quarto andar"]:
                tempo(3)
                print("O quarto andar pode ser um ótimo lugar para aumentar seu inventário")
            elif escolha==cenarios["sala comp"]:
                tempo(3)
                print("Você encontra vários Alienwares...")
                tempo(3)
                pro=input("Deseja roubar um Alienware?(sim/nao)")
                if pro=="sim":
                    Inventario.append("Alienware")
                    print('\033[35m'+'Alienware adicionado ao inventário'+'\033[0;0m')
                    tempo(3)
                    print('\033[36m'+'+20 pontos de Armour'+'\033[0;0m')
                    tempo(3)
                else:
                    print("Você saiu da sala comp")
                    tempo(3)
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

print('oi')