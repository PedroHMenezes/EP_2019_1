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
cont1=0
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
            "descricao": "Sala do professor",
            "opcoes": {
                    "andar professor": "Voltar para andar professor"
            }
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
                        "sala 405": "Ir para a sala 405 (Predio Velho)"
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
    cont=0
    Inventario=[]
    game_over = False
    vitoria=False
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
                    print('')
                    tempo(2)
                    j+=1
                else:
                    print("Não há nada que possa lhe ajudar aqui na biblioteca...")
                    print('')
                    tempo(2)
                
            elif escolha==cenarios['inicio']:
                if i==1:
                    print("Você voltou ao Saguão de entrada do Insper e"
                        " se deparou com a Next fazendo uma propaganda e dando"
                        " ingressos para o cinema")
                    tempo(4)
                    ingresso=input("Deseja pegar um ingresso?(sim/nao)")
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
                        print("Opções: Combater o monstro ou fugir perder 15 de dano de ataque")
                        tempo(2)
                        op=input('O que deseja fazer?(combater/fugir)')
                        tempo(2)
                        if op=='combater':                      
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
                            tempo(2)
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
                            print('')
                            tempo(4)
                        else:
                            Dj=Dj-15
                            print('\033[31m'+'Você perdeu 15 de dano de ataque'+'\033[0;0m')
                            print('')
                            tempo(3)
                            print(printa_status(Vj,Dj,Ej,Level,''))
                i+=1
            elif escolha==cenarios["professor"]:
                print("Ao entrar na sala você se depara com o monstro"
                    " do Python")
                print("'Olá, caro aluno, o que deseja?'")
                decisao_final=input("O que deseja fazer?(abrir inventario/Conversar)")
                while decisao_final!="Sair no soco":
                    if decisao_final=="abrir inventario":
                        print("Você olha no inventário e vê seus itens:")
                        for e in Inventario:
                            print(e)
                        escolha=input("Deseja usar alguma coisa dessas?(digite um dos itens)")
                        if escolha in Inventario:
                            if escolha=="Maçã":
                                print("'Como que você pode me oferecer isso?'")
                                tempo(2)
                                print("Pensei que fosse gostar...")
                                tempo(1)
                                print("'Achou errado, otário'")
                                tempo(1)
                                print("Professor vira o monstro do Python")
                                tempo(1)
                            elif escolha=="Cartão de débito":
                                print("Olha professor... Eu tenho esse cartão"
                                      " que você pode usar para pagar um almoção"
                                      " lá no Laranjinha. O que acha?")
                                tempo(3)
                                print(" 'Hmmm... Eu gosto do chef de lá... O que"
                                      " você quer em troca?' ")
                                tempo(2)
                                print("Você entrega o cartão para o professor")
                                tempo(1)
                                i=0
                                indice=0
                                while i<len(Inventario):
                                    if Inventario[i]=="Cartão de débito":
                                        indice=i
                                    i+=1
                                del (Inventario[indice])
                                print("Então... Eu preciso de um adiamento do EP...")
                                tempo(2)
                                print(" 'Bom... Posso adiar para amanhã. O que acha?' ")
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
                                decisao_final="Sair no soco"
                                
                            elif escolha=="pen drive":
                                print(" 'O que é isso? Um pen drive? O que tem ai dentro?' fugir")
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
                                confirmacao=input("Quer mesmo oferecer isso a ele?(sim/não)")
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
                                    print('')
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
                                    " quer com eles?' ")
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
                            tempo(2)
                            print(" 'Certo... Sobre o que quer conversar?' ")
                            tempo(2)
                            print("Preciso de um adiamento do EP...")
                            tempo(2)
                            print(" 'O que você fez nesse tempo que tinha?' ")
                            tempo(2)
                            print("Ahhh... eu decidi dar um descanso pra mim mesmo...")
                            tempo(2)
                            print(" 'Acredito que isso não seja uma boa desculpa' ")
                            tempo(2)
                            print("MAS EU PRECISO DE UM ADIAMENTO DO EP!!!!")
                            tempo(2)
                            print(" 'VOCÊ NÃO TERÁ ADIAMENTO DO EP!' ")
                            tempo(2)
                            print("O professor vira um monstro")
                            tempo(2)
                            decisao_final="Sair no soco"
                del opcoes['andar professor']
                tempo(2)
                print ("O professor em forma de monstro, começa a destruir a sala"
                          " por conta do seu tamanho")
                tempo(2)
                print("Ele agarra você e joga longe, direto para a Hélio Peregrino")
                tempo(2)
                print("Você, atordoado pela queda, pensa em 2 opções:")
                tempo(2)
                print("Pegar um patinete elétrico e fugir ou lutar")
                tempo(2)
                Helio_escolha=input("Qual você escolhe?(fugir/lutar)")
                if Helio_escolha=="lutar":
                    print("Você se prepara para o combate!")
                    tempo(2)
                    print("O professor pula do prédio do Insper direto para a"
                          " Hélio Peregrino")
                    tempo(2)
                    print("Ele estremece o chão ao cair. E você, quase caindo, dá um"
                          " mortal para trás e olha fixo para o monstro")
                    tempo(2)
                    Vp=400
                    Dp=100
                    Ep=100
                    Levelp=100
                    print(printa_status(Vp,Dp,Ep,Levelp,"Professor"))
                    tempo(2)
                    print("Chute do dragão - 10 de dano")
                    tempo(2)
                    print("Jogar uma bike do itau - 8 de dano")
                    tempo(2)
                    print("Programar uma função sem return - 10 de dano")
                    tempo(2)
                    ataque1=input("Qual será seu ataque?(dragão/itau/funcao)")
                    tempo(2)
                    if ataque1=="dragão":
                        print("O professor consegue se programar para virar o "
                              "Jackie Chan e vocês começam uma luta")
                        tempo(2)
                        print("Você vai em direção a ele com o chute do dragão")
                        tempo(2)
                        print("Ele para seu pé com uma das mãos e com a outra segura sua"
                              " perna")
                        tempo(2)
                        print("Você rapidamente pensa em possibilidades: pode chutar ele com"
                              " a outra perna ou tirar a mão dele da sua perna")
                        tempo(2)
                        reacao1=input("Qual sua decisão?(chutar/tirar)")
                        if reacao1=="chutar":
                            print("Você chuta o professor do lado esquerdo do corpo dele,"
                                  " fazendo ele largar seu pé e dar um passo atrás")
                            tempo(2)
                            print("Vocês continuam lutando bravamente!!!")
                            tempo(2)
                            print("Ele então prepara um código especial e atira em você!")
                            tempo(2)
                            print(" ' DICIONÁRIOS ANINHADOS!' ")
                            tempo(2)
                            print("Você toma um golpe muito forte, cai no chão" 
                                  "e começa a se sentir fraco...")
                            tempo(2)
                            print("Ele chega perto de você e diz:" )
                            tempo(2)
                            print(" ' Você lutou muito bem, mas não há adiamento de EP's' ")
                            tempo(2)
                            game_over=True
                        else:
                            print("Você soca o braço dele e ao fazer isso ele te segura"
                                  " no braço")
                            tempo(2)
                            print("Com poucas opções, você tenta se soltar, mas o Jackie "
                                  "Chan do Python acaba percebendo isso e está transformando"
                                  " você em código")
                            tempo(3)
                            print("Você pode fazer duas movimentações:")
                            tempo(2)
                            print("Pedir socorro")
                            tempo(2)
                            print("Gritar bem alto while sem i+=1")
                            tempo(2)
                            reacao2=input("Como última chance, o que deseja fazer?(socorro/while)")
                            if reacao2=="socorro":
                                print("Você pede socorro, mas ninguém sequer te ouve...")
                                game_over=True
                            else:
                                print("O professor sente uma dor muito forte e te larga")
                                tempo(2)
                                print("Ele começa a andar para trás...")
                                tempo(2)
                                print("Então ele trava (assim como o while...)")
                                tempo(2)
                                print('...')
                                vitoria=True
                                game_over=True
                    elif ataque1=="itau":
                        print("Você joga a bike do Itau e professor desvia rapidamente")
                        tempo(2)
                        print("Você então começa a procurar por uma saída e pensa em como"
                              " derrotá-lo")
                        tempo(2)
                        print("Enquanto isso o professor prepara um código e joga em você!")
                        tempo(2)
                        print("EXERCÍCIOS DE PROVAS PASSADAS")
                        tempo(2)
                        print("Você tenta desviar mas acaba sendo atingido")
                        tempo(2)
                        print("Machucado, então você pensa em duas possibilidades:")
                        tempo(2)
                        print("Pegar o patinete e fugir")
                        tempo(2)
                        print("Olhar inventário")
                        tempo(2)
                        decisao_itau=input("O que deseja fazer?(patinete/inventario)")
                        if decisao_itau=="patinete":
                            print("O professor vê você tentando fugir no patinete e dá"
                                  " risada")
                            tempo(2)
                            print("Ele então programa um patinete mais veloz e vai atrás"
                                  " de você")
                            tempo(2)
                            print("Ele te alcança e transforma você em código")
                            game_over=True
                        elif decisao_itau=="inventario":
                            i=0
                            while i<len(Inventario):
                                print (Inventario[i])
                                i+=1
                            item=input("Qual item deseja utilizar?")
                            if "banana dourada" and "tronco atirador" and "barril explosivo" not in Inventario:
                                print("Nada aqui pode te ajudar muito...")
                                tempo(2)
                                print("O professor percebendo uma brecha arremessa um"
                                      " código em você e te acerta")
                                tempo(3)
                                print(" 'Você bem que tentou, mas com grandes poderes"
                                      " vem grandes responsabilidades' ")
                                game_over=True
                            else:
                                if item in Inventario:
                                    if item=="pen drive" or item=="Maçã" or item=="espada" or item=="Alienware" or item=="cartão de débito":
                                        print("Nada disso pode te ajudar muito...")
                                        tempo(2)
                                    else:
                                        print("Você tira {0} do Inventário".format(item))
                                        tempo(2)
                                        print(" ' ONDE VOCÊ CONSEGUIU ISSO?' ")
                                        tempo(2)
                                        print("O professor surpreso, começa a processar código demais"
                                              " e trava seu kernel")
                                        tempo(2)
                                        game_over=True
                                        vitoria=True
                    elif ataque1=='funcao':
                        print("Você define uma função!")
                        tempo(3)
                        print("...")
                        tempo(3)
                        print("Mas...")
                        tempo(3)
                        print("Você não coloca o return!")
                        tempo(3)
                        print("O professor então diz:")
                        tempo(3)
                        print("...")
                        tempo(3)
                        print("'None'")
                        tempo(3)
                        print("Então ele olha fixamente para você...")
                        tempo(3)
                        print("E grita:")
                        tempo(2)
                        print('\033[31m'+'VOCÊ ESTÁ DE DP!!!!'+'\033[0;0m')
                        tempo(3)
                        game_over=True
                else:
                    print("Você pega um patinete elétrico e começa a fugir")
                    tempo(3)
                    print("...")
                    tempo(3)
                    print("Você chega à 25km/h com seu patinete")
                    tempo(3)
                    print("...")
                    tempo(3)
                    print("Mas passa em cima de uma pedra e sai voando!!!")
                    tempo(3)
                    print('\033[31m'+'Ai! Você caiu feio!'+'\033[0;0m')
                    tempo(3)
                    game_over=True
            elif escolha==cenarios["quarto andar"]:
                tempo(3)
                print("O quarto andar pode ser um ótimo lugar para aumentar seu inventário")
                print('')
                tempo(2)
            elif escolha==cenarios["lab de info"]:
                tempo(4)
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
                    printa_status(Vm,Dm,Em,Levelm, "Colega Infectado")
                    tempo(3)
                    print("...")
                    tempo(3)
                    print("Grr...")
                    tempo(3)
                    print('...')
                    tempo(4)
                    print('\033[34m'+'Você ganhou a batalha!'+'\033[0;0m')
                    tempo(3)
                    print('\033[36m'+'Você subiu de nível!'+'\033[0;0m')
                    tempo(4)
                    Level+=1
                    print(printa_status(a,Dj,Ej,Level,''))
                    tempo(4)
                else:
                    print("Você fugiu")
            elif escolha==cenarios["sala 405"]:
                if cont==0:
                    tempo(3)
                    print("Você tenta abrir a porta da sala 405, mas ela não abre...")
                    tempo(3)
                    print("Então você faz mais força, e ela abre")
                    tempo(3)
                    print("Dentro da sala você percebe que há uma máquina de teleporte!")
                    tempo(3)
                    tel=input("Deseja entrar na máquina de teleporte?(sim/nao)")
                    cont+=1
                elif cont>0:
                    tel=input("Deseja entrar na máquina de teleporte?(sim/nao)")
                if tel=="sim":
                            print('\033[36m'+'Você está na máquina de teleporte:'+'\033[0;0m')
                            print('')
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
                        print('')
                        tempo(2)
                    elif arma=="barril explosivo":
                        print("Analisando o barril, percebe que ele é capaz de causar 250"
                            " de dano de ataque ao inimigo")
                        tempo(4)
                        Inventario.append("barril explosivo")
                        print('\033[35m'+'Barril explosivo adcionado ao inventário'+'\033[0;0m')
                        print('')
                        tempo(2)
                    else:
                        print("Ao analisar o tronco atirador você foi capaz de perceber que"
                            " ele pode atirar nozes(ilimitadas!) de longe")
                        tempo(4)
                        Inventario.append("tronco atirador")
                        print('\033[35m'+'Tronco atirador adcionado ao inventário'+'\033[0;0m')
                        print('')
                        tempo(2)
                else:
                    print("Você sai da sala 405")
                    print('')
                    tempo(2)
            elif escolha==cenarios["andar professor"]:
                tempo(5)
                print("Ao chegar no andar do professor, você percebe que há"
                        " uma força estranha no ar...")
                tempo(4)
                print("Na entrada da sala do professor há uma espada "
                        " encravada numa pilha de provas...")
                tempo(4)
                print("Ao chegar mais perto você observa que são"
                        " provas de Python e que há uma frase escrita"
                        " nela")
                tempo(4)
                print("O aluno que conseguir retirar a "
                        " espada encravada nesta pilha de provas será capaz"
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
                    print('')
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
                    Ej+=20
                    print('\033[36m'+'+20 pontos de Armour'+'\033[0;0m')
                    tempo(3)
                else:
                    print("Você saiu da sala comp")
                    tempo(3)
            elif escolha==cenarios["banheiro"]:
                print("Tirando a água do joelho...")
                #for k,v in opcoes.items():
                    #del
            if game_over==False:
                for k,v in opcoes.items():
                    print(k+': '+v)
                escolha=input('Para onde deseja ir?')
                if escolha in opcoes:
                    nome_cenario_atual = escolha
                else:
                    print("Sua indecisão foi sua ruína!")
                    game_over = True
    if vitoria==False:    
        print("Você morreu!")
    else:
        print("Parabéns! Você conseguiu adiar o EP")
# Programa principal.
_name_= "_main_"
if _name_ == "_main_":
    main()
