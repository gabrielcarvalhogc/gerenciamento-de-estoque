class Movimentação:
    def __init__(self, id, produto_id, quantidade, tipo_movimentacao, data):
        self.id = id
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.tipo_movimentacao = tipo_movimentacao
        self.data = data
        
#Algoritmos de Movimentação: Funções para registrar entradas e saídas de produtos e atualizar o estoque.
def registrar_movimentacao(movimentos, contador_movimentos, produtos):
    id = contador_movimentos
    produto_id = int(input("ID do produto: "))
    quantidade = int(input("Quantidade: "))
    tipo_movimentacao = input("Tipo de movimentação: \nE - Entrada\n S - Saída: ").strip().upper()
    data = input("Data (DD/MM/AAAA): ")
    
    produto_encontrado = next((p for p in produtos if p.id == produto_id), None)
    if produto_encontrado:
        if tipo_movimentacao == "E":
            produto_encontrado.quantidade += quantidade
        elif tipo_movimentacao == "S":
            if produto_encontrado.quantidade >= quantidade:
                produto_encontrado.quantidade -= quantidade
            else:
                print("Quantidade insuficiente no estoque!")
                return contador_movimentos 
        movimentos.append(Movimentação(id, produto_id, quantidade, tipo_movimentacao, data))
        print("Movimentação registrada com sucesso!")
        return contador_movimentos + 1
    else:
        print("Produto não encontrado!")
        return contador_movimentos