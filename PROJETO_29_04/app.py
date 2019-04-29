from flask import Flask, url_for, request, json, jsonify, abort
from json import dumps
from dbUtils import DbUtils

app = Flask(__name__)
myUser = []

@app.route('/')
def api_root():
    return 'Bem-vindo!!!'

#  -------------------------------  METODOS POST ------------------------------------

@app.route('/addvendedor', methods = ['POST'])
def Insert_vendedor():

    if not request.json:
        abort(400)
    req_data = request.get_json()
    cpf = req_data['cpf']
    nome = req_data['nome']
    carteira_trabalho = req_data['carteiraTrabalho']
    telefone = req_data['telefone']
    data = req_data['dataAdmissao']
    fg_ativo = req_data['fg_ativo']
    dbutils = DbUtils()
    if(dbutils.Insere_Vendedor(cpf, nome, carteira_trabalho,telefone,data,fg_ativo)):
        result = {"result": "Vendedor inserido"}
    else:
        result = {"result": "ERRO"}
    return jsonify(result)

@app.route('/addproduto', methods = ['POST'])
def Insert_produto():
    
    if not request.json:
        abort(400)
    req_data = request.get_json()
    id_fornecedor = req_data['id_fornecedor']
    id_categoria = req_data['id_categoria']
    nome = req_data['nomeProduto']
    descricao = req_data['descricaoProduto']
    valor = req_data['valorUnitario']
    quantidade = req_data['quantidade']
    quantidade_minima = req_data['quantidadeMinima']
    fg_ativo = req_data['fg_ativo']
    dbutils = DbUtils()
    if(dbutils.Insert_Prod(id_fornecedor,id_categoria,nome,descricao,valor,quantidade,quantidade_minima, fg_ativo)):
        result = {"result": "Produto inserido"}
    else:
        result = {"result": "ERRO"}
    return jsonify(result)

@app.route('/addcategoria', methods = ['POST'])
def Insert_categoria():
    
    if not request.json:
        abort(400)
    req_data = request.get_json()
    titulo = req_data['tituloCategoria']
    descricao = req_data['descricaoCategoria']
    fg_ativo = req_data['fg_ativo']
    dbutils = DbUtils()
    if(dbutils.Insert_Cat( titulo_categoria,descricao_categoria, fg_ativo)):
        result = {"result": "Categoria inserida"}
    else:
        result = {"result": "ERRO"}
    return jsonify(result)
    
@app.route('/addcompra', methods = ['POST'])
def Insert_compra():
    
    if not request.json:
        abort(400)
    req_data = request.get_json()
    id_fornecedor = req_data['id_fornecedor']
    id_produto = req_data['id_produto']
    id_categoria = req_data['id_categoria']
    data = req_data['dataCompra']
    valor = req_data['valorTotal']
    quantidade = req_data['quantidade']
    fg_ativo = req_data['fg_ativo']
    dbutils = DbUtils()

    if(dbutils.Insert_Compra(id_fornecedor,id_produto,id_categoria,data,valor,quantidade, fg_ativo)):
        result = {"result": "Compra inserida"}
    else:
        result = {"result": "ERRO"}
    return jsonify(result)

@app.route('/addvenda', methods = ['POST'])
def Insert_venda():
    
    if not request.json:
        abort(400)
    req_data = request.get_json()
    id_vendedor = req_data['id_vendedor']    
    id_categoria = req_data['id_categoria']
    id_produto = req_data['id_produto']
    data = req_data['dataVenda']
    valor = req_data['valorTotal']
    quantidade = req_data['quantidade']
    fg_ativo = req_data['fg_ativo']
    dbutils = DbUtils()
    if(dbutils.Insert_Venda(id_vendedor,id_categoria,id_produto,data,valor,quantidade, fg_ativo)):
        result = {"result": "Venda inserida"}
    else:
        result = {"result": "ERRO"}
    return jsonify(result)

@app.route('/addfornecedor', methods = ['POST'])
def Insert_fornecedor():
    
    if not request.json:
        abort(400)
    req_data = request.get_json()
    cnpj = req_data['cnpj']
    razao = req_data['razaoSocial']
    telefone = req_data['telefone']
    endereco = req_data['endereco']
    contato = req_data['contato']
    fg_ativo = req_data['fg_ativo']
    dbutils = DbUtils()
    razao = req_data['razaoSocial']
    if(dbutils.Insert_Fornec(cnpj,razao,telefone,endereco,contato, fg_ativo)):
        result = {"result": "Fornecedor inserida"}
    else:
        result = {"result": "ERRO"}
    return jsonify(result)

#  -------------------------------  METODOS GET  ------------------------------------

@app.route('/getvendedores')
def GET_vendedor():
    Sellers = []
    dbUtils = DbUtils()
    DB_VECTOR = dbUtils.getVendedores()
    for data in DB_VECTOR:
        item = {"id": data[0], "cpf": data[1], "nome": data[2], "carteira_de_trabalho": data[3],
        "telefone": data[4], "data_de_admissao": data[5], "fg_ativo": data[6]}
    Sellers.append(item)
    return jsonify(Sellers)

@app.route('/getprodutos')
def GET_produto():
    Prodc = []
    dbUtils = DbUtils()
    DB_VECTOR = dbUtils.getProdutos()
    for data in DB_VECTOR:
        item = {"id_produto": data[0], "id_fornecedor": data[1], "id_categoria": data[2], "nomeproduto":data[3],
        "descricaoproduto":data[4],"valor_unitario":str(data[5]), "quantidade":data[6], "quantidademinima":data[7], "fg_ativo":data[8]}
    Prodc.append(item)
    return jsonify(Prodc)

@app.route('/getcategorias')
def GET_categoria():
    Cat = []
    dbUtils = DbUtils()
    DB_VECTOR = dbUtils.getCategorias()
    for data in DB_VECTOR:
        item = {"id": data[0], "titulo_da_categoria": data[1], "descricao_da_categoria": data[2],"fg_ativo": data[3]}
    Cat.append(item)
    return jsonify(Cat)

@app.route('/getfornecedores')
def GET_fornecedor():
    Forn = []
    dbUtils = DbUtils()
    DB_VECTOR = dbUtils.getFornecedores()
    for data in DB_VECTOR:
        item = {"id": data[0], "cnpj": data[1], "razaosocial": data[2], "telefone":data[3],"endereco":data[4], 
        "contato":data[5], "fg_ativo":data[6]}
    Forn.append(item)
    return jsonify(Forn)

@app.route('/getcompras')
def GET_compra():
    Shop = []
    dbUtils = DbUtils()
    DB_VECTOR = dbUtils.getCompras()
    for data in DB_VECTOR:
        item = {"id_compra":data[0],"id_fornecedor":data[1], "id_produto": data[2], "id_categoria": data[3], 
        "datacompra":data[4],"valortotal":str(data[5]), "quantidade":data[6], "fg_ativo":data[7]}
    Shop.append(item)
    return jsonify(Shop)

@app.route('/getvendas')
def GET_venda():
    Sales = []
    dbUtils = DbUtils()
    DB_VECTOR = dbUtils.getVendas()
    for data in DB_VECTOR:
        item = {"id_venda":data[0],"id_vendedor":data[1], "id_categoria": data[2],"id_produto": data[3], "datavenda":data[4],
        "valortotal":str(data[5]), "quantidade":data[6], "fg_ativo":data[7]}
    Sales.append(item)
    return jsonify(Sales)




    



