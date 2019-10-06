from flask import render_template, Blueprint, request, redirect, url_for
from my_app.models.contas.tipos.conta_poupanca import ContaPoupanca
from my_app.models.cliente.cliente import Cliente
from my_app.db import get_connection

conta_bp = Blueprint('contas', __name__, url_prefix='/contas')


@conta_bp.route('/form/seja-cliente')
def formulario_cliente():
    return render_template('form-cliente.html')

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
    limite = float(request.form.get('limite'))

    conta = ContaPoupanca(numero, limite)

    sql = 'update contas set numero=%s, saldo=%s, limite=%s where id=%s;'
    valores = (numero, conta.get_saldo, limite, int(id))

    cursor = connection.cursor()
    cursor.execute(sql, valores)

    connection.commit()
    connection.close()

    return '<h1>O seu cartão chegará em 7 dias uteis!!! :D</h1>'







































'''LISTA CONTAS'''
@conta_bp.route('/lista')
def lista_contas():
    connection = get_connection()

    sql = 'select * from contas'

    cursor = connection.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()

    contas = []
    for registro in resultado:
        conta = Conta(registro[1], registro[2], registro[3], registro[4], registro[0])
        contas.append(conta)

    connection.close()

    return render_template('lista.html', contas=contas)

'''FORM CONTAS'''
@conta_bp.route('/form/escolha-sua-conta')
def formulario_conta():
    return render_template('form-conta.html')

'''CRIA CONTAS'''
@conta_bp.route('/cria-conta', methods=['POST'])
def cria_conta():

    numero = request.form.get('numero')
    saldo = 0.0
    limite = float(request.form.get('limite'))

    conta = Conta(numero, titular, saldo, limite)

    connection = get_connection()

    sql = 'insert into contas (numero, titular, saldo, limite) values (%s, %s, %s, %s)'
    valores = (conta.numero, conta.titular, conta.saldo, conta.limite)

    cursor = connection.cursor()
    cursor.execute(sql, valores)

    connection.commit()
    connection.close()

    return redirect(url_for('contas.lista_contas'))

'''PEGA CONTA NO BD'''
@conta_bp.route('/form/<int:id>/edit', methods=['GET'])
def get_update(id):

    update = True

    connection = get_connection()

    sql = 'select * from contas where id={}'.format(int(id))

    cursor = connection.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()

    id = resultado[0][0]
    numero = resultado[0][1]
    titular = resultado[0][2]
    saldo = resultado[0][3]
    limite = resultado[0][4]

    connection.close()

    return render_template('form-conta.html',
                           id=id,
                           numero=numero,
                           titular=titular,
                           saldo=saldo,
                           limite=limite,
                           update=update)

'''ATUALIZACAO DA CONTA'''
@conta_bp.route('/<int:id>/edit', methods=['POST'])
def update(id):

    connection = get_connection()

    numero = request.form.get('numero')
    titular = request.form.get('titular')
    saldo = float(request.form.get('saldo'))
    limite = float(request.form.get('limite'))

    sql = 'update contas set numero=%s, titular=%s, saldo=%s, limite=%s where id=%s;'
    valores = (numero, titular, saldo, limite, int(id))

    cursor = connection.cursor()
    cursor.execute(sql, valores)

    connection.commit()
    connection.close()

    return redirect(url_for('contas.lista_contas'))

'''DELETA CONTA'''
@conta_bp.route('/<int:id>/remove')
def remove(id):

    connection = get_connection()

    sql = 'delete from contas where id={}'.format(int(id))

    cursor = connection.cursor()
    cursor.execute(sql)

    connection.commit()
    connection.close()

    return redirect(url_for('contas.lista_contas'))