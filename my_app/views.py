from flask import render_template, Blueprint, request, redirect, url_for

'''from my_app.models.contas.tipos.conta_poupanca import ContaPoupanca'''
from my_app.models.contas.tipos.conta_corrente import ContaCorrente
from my_app.models.cliente.cliente import Cliente
from my_app.db import get_connection

conta_bp = Blueprint('bb', __name__, url_prefix='/bb')


@conta_bp.route('/seja-cliente')
def formulario_cliente():
    return render_template('cadastro_cliente.html')


'''CADASTRA CLIENTE'''


@conta_bp.route('/registrar-cliente', methods=['POST'])
def cria_cliente():
    nome = request.form.get('nome')
    sobrenome = request.form.get('sobrenome')

    cpf = request.form.get('cpf')
    email = request.form.get('email')
    telefone = request.form.get('telefone')
    celular = request.form.get('celular')
    endereco = request.form.get('endereco')
    complemento = request.form.get('complemento')
    numero_residencial = request.form.get('numero_residencial')
    pais = request.form.get('pais')
    estado = request.form.get('estado')
    cep = request.form.get('cep')

    cliente = Cliente(nome,
                      sobrenome,
                      cpf,
                      email,
                      telefone,
                      celular,
                      endereco,
                      complemento,
                      numero_residencial,
                      pais,
                      estado,
                      cep)

    connection = get_connection()

    sql = 'insert into contas (titular, cpf, email, telefone, celular, endereco, complemento, numero_residencial, pais, estado, cep) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    valores = (cliente.get_titular,
               cliente.get_cpf,
               cliente.get_email,
               cliente.get_telefone,
               cliente.get_celular,
               cliente.get_endereco,
               cliente.get_complemento,
               cliente.get_numero_residencial,
               cliente.get_pais,
               cliente.get_estado,
               cliente.get_cep)

    cursor = connection.cursor()
    cursor.execute(sql, valores)

    connection.commit()
    connection.close()

    return redirect(url_for('bb.get_cliente', id=cliente.get_id))


'''-------------- CRIA CONTA ----------------'''
'''PEGA CLIENTE NO BD'''


@conta_bp.route('/<int:id>/escolha-sua-conta', methods=['GET'])
def get_cliente(id):
    update = True

    connection = get_connection()

    sql = 'select * from contas where id={}'.format(int(id))

    cursor = connection.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()

    id = resultado[0][0]
    titular = resultado[0][1]

    connection.commit()
    connection.close()

    return render_template('escolha_conta.html',
                           id=id,
                           titular=titular,
                           update=update)


'''CRIA CONTA (   QUANDO DER SUBMIT NO FORM   )'''


@conta_bp.route('/<int:id>/corrente', methods=['POST'])
def create_account(id):
    connection = get_connection()

    sql_busca = 'select titular from contas where id={}'.format(int(id))

    cursor = connection.cursor()
    cursor.execute(sql_busca)
    resultado = cursor.fetchall()

    titular = resultado[0][0]

    conta = ContaCorrente(titular)

    sql = 'update contas set tipo_conta=%s, numero=%s, senha=%s, saldo=%s, limite=%s where id=%s;'
    valores = (conta.get_tipo_conta, conta.get_numero, conta.get_senha, conta.get_saldo, conta.get_limite, int(id))

    cursor = connection.cursor()
    cursor.execute(sql, valores)

    connection.commit()
    connection.close()

    return render_template('envio_email.html')


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
        return redirect(url_for('bb.dashboard'))
    else:
        return render_template('login.html', failed_login=True, id=id_output)


''' ------- HOME PRINCIPAL SEM LOGIN -------- '''


@conta_bp.route('/home')
def home():
    return render_template('main.html')


''' ------- DASHBOARD -------- '''


@conta_bp.route('/<int:id>/dashboard')
def dashboard(id):
    connection = get_connection()

    sql = 'select saldo from contas where id={}'.format(id)

    cursor = connection.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()

    saldo = resultado[0][0]

    connection.close()

    return render_template('dashboard.html', saldo=saldo)
