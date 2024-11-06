#Sistema de gerenciamento de estoque
class Produto:
    def __init__(self, id, nome, categoria_id, quantidade, preco, setor):
        self.id = id
        self.nome = nome
        self.categoria_id = categoria_id
        self.quantidade = quantidade
        self.preco = preco
        self.setor = setor
        
class Categoria:
    def __init__(self,id,nome):
        self.id = id
        self.nome = nome

#Funções para cadastrar e consultar dados no sistema.         
def cadastrar_produtos(produtos, contador_produtos):
    id = contador_produtos + 1
    nome = input("Nome do produto: ")
    categoria_id = int(input("Id da categoria: "))
    quantidade = int(input("Insira a quantidade: "))
    preco = float(input("Insira o preço: "))
    setor = input("Digite o setor onde o produto estará localizado: ")
    produtos.append(Produto(id, nome, categoria_id, quantidade, preco, setor))
    print("Produto cadastrado com sucesso!")
    return contador_produtos + 1

def consultar_produto_id(produtos, id):
    for produto in produtos:
        if produto.id == id:
            print(f'ID: {produto.id}, Nome: {produto.nome}, Categoria: {produto.categoria_id}, 
            Quantidade: {produto.quantidade}, Preço: {produto.preco}')
