import psycopg2
from sqlalchemy import create_engine
from psycopg2 import Error

class DbUtils:
    db_string = "postgresql+psycopg2://postgres:5780@localhost/ASA"
    db_query = " "
    
#  -------------------------------  INSERTS ------------------------------------

    def Insere_Vendedor(self, cpf, nome, carteira_trabalho, telefone, data, fg_ativo):
        db = create_engine(self.db_string)
        self.db_query = "INSERT INTO new_db.tb_vendedores (cpf, nome, carteiraTrabalho, telefone, dataAdmissao,fg_ativo) VALUES (%s, %s, %s, %s, %s, %s);" 
        values = (cpf, nome, carteira_trabalho, telefone, data, fg_ativo)
        try:
            db.execute(self.db_query,values)
            res = True

        except (Exception, psycopg2.Error) as error :
            print(error)
            print("ERRO")
            res = False
        return res

    def Insert_Fornec(self, cnpj,razao,telefone,endereco,contato,fg_ativo):
        db = create_engine(self.db_string)
        self.db_query = "INSERT INTO new_db.tb_fornecedores (cnpj, razaoSocial, telefone, endereco, contato, fg_ativo) VALUES (%s,%s,%s, %s, %s,%s);" 
        values = (cnpj, razao, telefone, endereco, contato, fg_ativo)
        try:
            db.execute(self.db_query,values)
            res = True

        except (Exception, psycopg2.Error) as error :
            print(error)
            print("ERRO")
            res = False
        return res

    def Insert_Cat(self, titulo, descricao, fg_ativo):
        db = create_engine(self.db_string)
        self.db_query = "INSERT INTO new_db.tb_categorias (tituloCategoria, descricaoCategoria, fg_ativo) VALUES (%s, %s, %s);" 
        values = (titulo,descricao, fg_ativo)
        try:
            db.execute(self.db_query,values)
            res = True

        except (Exception, psycopg2.Error) as error :
            print(error)
            print("ERRO")
            res = False
        return res

    def Insert_Prod(self, id_fornecedor, id_categoria, nome, descricao, valor, quantidade, quantidade_minima,fg_ativo):
        db = create_engine(self.db_string)
        self.db_query = "INSERT INTO new_db.tb_produtos (id_fornecedor, id_categoria, nomeProduto, descricaoProduto, valorUnitario, quantidade, quantidademinima,fg_ativo) VALUES (%s,%s,%s, %s, %s,%s,%s,%s);" 
        values = (id_fornecedor, id_categoria, nome, descricao, valor, quantidade, quantidade_minima,fg_ativo)
        try:
            db.execute(self.db_query,values)
            res = True

        except (Exception, psycopg2.Error) as error :
            print(error)
            print("ERRO")
            res = False
        return res

    def Insert_Venda(self, id_vendedor,id_categoria,id_produto,data,valor,quantidade, fg_ativo):
        db = create_engine(self.db_string)
        self.db_query = "INSERT INTO new_db.tb_vendas (id_vendedor,id_categoria,id_produto,dataVenda,valorTotal,quantidade, fg_ativo) VALUES (%s,%s,%s, %s, %s,%s,%s);" 
        values = (id_vendedor,id_categoria,id_produto,data,valor,quantidade, fg_ativo)
        try:
            db.execute(self.db_query,values)
            res = True

        except (Exception, psycopg2.Error) as error :
            print(error)
            print("ERRO")
            res = False
        return res

    def Insert_Compra(self, id_fornecedor,id_produto,id_categoria,data,valor,quantidade, fg_ativo):
        db = create_engine(self.db_string)
        self.db_query = "INSERT INTO new_db.tb_compras (id_fornecedor,id_produto,id_categoria,dataCompra,valorTotal,quantidade, fg_ativo) VALUES (%s,%s,%s, %s, %s,%s,%s);" 
        values = (id_fornecedor,id_produto,id_categoria,data,valor,quantidade, fg_ativo)
        try:
            db.execute(self.db_query,values)
            res = True

        except (Exception, psycopg2.Error) as error :
            print(error)
            print("ERRO")
            res = False
        return res

#  -------------------------------  SELECTS ------------------------------------

    def getVendedores(self):
        db = create_engine(self.db_string)
        self.select_query = "select * from new_db.tb_vendedores"
        vendedores = db.execute(self.select_query)
        return vendedores

    def getCategorias(self):
        db = create_engine(self.db_string)
        self.select_query = "select * from new_db.tb_categorias"
        categorias = db.execute(self.select_query)
        return categorias

    def getFornecedores(self):
        db = create_engine(self.db_string)
        self.select_query = "select * from new_db.tb_fornecedores"
        fornecedores = db.execute(self.select_query)
        return fornecedores

    def getProdutos(self):
        db = create_engine(self.db_string)
        self.select_query = "select * from new_db.tb_produtos"
        produtos = db.execute(self.select_query)
        return produtos

    def getCompras(self):
        db = create_engine(self.db_string)
        self.select_query = "select * from new_db.tb_compras"
        compras = db.execute(self.select_query)
        return compras

    def getVendas(self):
        db = create_engine(self.db_string)
        self.select_query = "select * from new_db.tb_vendas"
        vendas = db.execute(self.select_query)
        return vendas