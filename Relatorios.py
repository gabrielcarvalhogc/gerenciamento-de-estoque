
#Funções para gerar relatórios e consultar o histórico de movimentações.
def gerar_relatorio_estoque(produtos):
    print("Relatório de estoque: ")
    for produto in produtos:
        print(f"ID: {produto.id}, nome: {produto.nome}, 
        Quantidade: {produto.quantidade}, Preço: {produto.preco:.2f}")
        
def consultar_movimentacoes(movimentacoes, produto_id):
    print(f"Movimentações do produto ID {produto_id}: ")
    for movimentacao in movimentacoes:
        if movimentacao.produto.id == produto_id:
            print(f"ID: {movimentacao.id}, Quantidade: {movimentacao.quantidade}, 
            Tipo: {movimentacao.tipo_movimentacao}, Data: {movimentacao.data}")