from Movimentacao import registrar_movimentacao
from Produto import cadastrar_produtos, consultar_produto_id
from Relatorios import consultar_movimentacoes, gerar_relatorio_estoque

def menu():
  import os
  import time
  
  produtos = []
  movimentacoes = []
  contador_produtos = 0
  contador_movimentacoes = 0

  while True:
    print("Estamos iniciando...")
    time.sleep(2)
    os.system('clear') or None
    print("#### Seja bem vindo ao SISCONF ####\n")
    escolha = int(input("Escolha uma ação:\n1 - Cadastrar novo produto\n2 - Consultar produto\n3 - Movimentações\n4 - Consulta movimentos\n5 - Gerar Relatório\n6 - Sair:\n"))
    if escolha == 1:
      while True:
        contador_produtos = cadastrar_produtos(produtos, contador_produtos)
        retornar = int(input("Escolha uma ação:\n1 - Cadastrar novo produto\n2 - Retornar ao menu: "))
        if retornar == 2:
          os.system('clear') or None
          break
    elif escolha == 2:
      while True:
        point = int(input("Qual o id do produto deseja consultar: "))
        consultar_produto_id(produtos, point)
        retornar = int(input("Escolha uma ação:\n1 - Consultar novo produto\n2 - Retornar ao menu: "))
        if retornar == 2:
          os.system('clear') or None
          break
    elif escolha == 3:
      contador_movimentacoes = registrar_movimentacao(movimentacoes, contador_movimentacoes, produtos)
      retornar = input('Deseja retornar ao menu: S - Sim N - Não: ').upper()
      if retornar == "S":
        os.system('clear') or None
    elif escolha == 4:
      point_mov = int(input("Qual o ID do produto que deseja consultar: "))
      consultar_movimentacoes(movimentacoes, point_mov)
    elif escolha == 5:
      gerar_relatorio_estoque(produtos)
      retornar = input('Deseja retornar ao menu: S - Sim N - Não: ').upper()
      if retornar == "S":
        os.system('clear') or None
    else:
      break

menu()