from flask import render_template, Blueprint, request, redirect, url_for
from my_app.models.contas.tipos.conta_poupanca import ContaPoupanca
from my_app.models.cliente.cliente import Cliente
from my_app.db import get_connection

conta_bp = Blueprint('contas', __name__, url_prefix='/contas')

'''----------- CADASTRA CLIENTE -------------'''
'''EXIBE FOR CLIENTE'''
@conta_bp.route('/form/seja-cliente')
def formulario_cliente():
    return render_template('form-cliente.html')

'''CADASTRA CLIENTE'''
@conta_bp.route('/form/cadastro-cliente', methods=['POST'])
def cria_cliente():

    nome = request.form.get('nome')
    sobrenome = request.form.get('sobrenome')
    cpf = request.form.get('cpf')

    cliente = Cliente(nome, sobrenome, cpf)

    connection = get_connection()

    sql = 'insert into contas (titular, cpf) values (%s, %s)'
    valores = (cliente.get_titular, cliente.get_cpf)

    cursor = connection.cursor()
    cursor.execute(sql, valores)

    connection.commit()
    connection.close()

    return redirect(url_for('contas.get_cliente',
                            id=cliente.get_id,
                            titular=cliente.get_titular,
                            cpf=cliente.get_cpf))

'''-------------- CRIA CONTA ----------------'''
'''PEGA CLIENTE NO BD'''
@conta_bp.route('/form/<int:id>/escolha-sua-conta', methods=['GET'])
def get_cliente(id):

    update = True

    connection = get_connection()

    sql = 'select * from contas where id={}'.format(int(id))

    cursor = connection.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()

    id = resultado[0][0]
    titular = resultado[0][2]
    cpf = resultado[0][3]

    connection.close()

    return render_template('form-conta.html',
                           id=id,
                           titular=titular,
                           cpf=cpf,
                           update=update)

'''CRIA CONTA'''
@conta_bp.route('/<int:id>/create', methods=['POST'])
def create_account(id):

    connection = get_connection()

    numero = request.form.get('numero')
    senha = request.form.get('senha')
    limite = float(request.form.get('limite'))

    conta = ContaPoupanca(numero, senha, limite)

    sql = 'update contas set numero=%s, senha=%s, saldo=%s, limite=%s where id=%s;'
    valores = (numero, senha, conta.get_saldo, limite, int(id))

    cursor = connection.cursor()
    cursor.execute(sql, valores)

    connection.commit()
    connection.close()

    return '<h1>O seu cartão chegará em 7 dias uteis!!! :D</h1>'

''' ------------ LOGIN CLIENTE ------------- '''
@conta_bp.route('/signin')
def login():
    return render_template('login.html')

@conta_bp.route('/login', methods=['POST'])
def validation():

    input_cpf = request.form.get('cpf')
    input_senha = request.form.get('senha')

    connection = get_connection()

    sql = 'select id, senha from contas where cpf={}'.format(input_cpf)

    cursor = connection.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()

    # Se o cpf nao existir no sistema, o retorno da query é -> []
    if resultado == []:
        connection.close()
        print('Connection closed')
        return render_template('login.html', failed_login=True)

    id_output = resultado[0][0]
    senha_output = resultado[0][1]

    connection.close()

    if input_senha == senha_output:
        return '<h1>Entrou</h1>'
    else:
        return render_template('login.html', failed_login=True)

''' ------- HOME PRINCIPAL SEM LOGIN -------- '''
@conta_bp.route('/home')
def home():
    return render_template('main.html')