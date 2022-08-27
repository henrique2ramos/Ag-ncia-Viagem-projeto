#integrantes do grupo
#José Henrique Sinésio Ramos
#Victor Gustavo Cavalcanti da Silva
#Leonardo Silva de Oliveira
#João Karllus Monteiro Paiva

import sys
import os
import random
import math

arquivosAgencia = []
pacotes = [{'tipo': 'viagem', 'destino': 'Dubai', 'data':10, 'valor': 3000, 'codigo': 3000}]
clientes = []
pedidos = []
faturamento = 0000
# dataAtualList = " ".join(str(datetime.datetime.now()).split("-")[0:3]).split(" ")[0:3] # gambiarra
#dataAtual = datetime.date(int(dataAtualList[0]),int(dataAtualList[1]),int(dataAtualList[2]))
digitos = 40

def Clear():
  if sys.platform[:3] == "win":
    os.system("cls")
  else:
    os.system("clear")

def CadastraPacotes():
  while True:
    tipoPacote = input("Qual é o tipo do Pacote: [Viagem, Combo] ").lower().strip()
    if tipoPacote == "viagem" or tipoPacote == "combo":
      break
    continue
      
  destino = input("Qual é o destino do pacote: ")
  while True:
    data = int(input("Digite a data: "))
    if data > 31:
      print("Não é possivel cadastra um Pacote para a data informada.")
      continue
    break

  while True:
    try: 
      transporte = input("Digite o nome do transporte: [oni ou avi]").lower().strip()[0]
      if (transporte == "a"):
        transporte = "Avião"
        break
      elif transporte == "o":
        transporte = "Ônibus"
        break
      else:
        continue
    except:
      continue

  while True:
    try: 
      diarias = int(input("Digite o número de diarias: "))
      break
    except:
      continue
  valor = int(input("Valor do Pacote: R$ "))
  codigo = random.randint(0000,9999)
  print('Código do pacote:',codigo)
  
  pacotes.append({
    "tipo":tipoPacote,
    "transporte":transporte,
    "destino":destino,
    "data":data,
    "valor":valor,
    "codigo":codigo
  })

def CadastroClientes():
  nome = input('Digite seu nome completo: ')  
  cpf = input('Digite seu cpf: ')
  endereco = input('Digite seu endereço: ')
  contato = input('Digite seu contato: ')

  clientes.append({
    'nome':nome,
    'cpf':cpf,
    'endereço':endereco,
    'contato':contato

  })

def ListarPacotes():
  global faturamento

  print("="*digitos)
  print("Viagens".center(digitos))
  print("="*digitos)
  
  if (len(pacotes) == 0):
    print("Nenhuma Viagem Cadastrada!")
    return

  for p in pacotes:
    print("Tipo da Viagem:",p["tipo"])
    print("Destino da Viagem:",p["destino"])
    print("Data da Viagem:",p["data"])
    print("Valor da Viagem: R$"+str(p["valor"]))
    print("Codigo do pacote:",p["codigo"])
    print("\n"+("-"*digitos)+"\n")

 
def CompraPacotes(codigoPacote=None):
  global faturamento

  codigoPacote = None
  pacoteInfos = {}
  oCodigoFoiEncontrado = False
  if codigoPacote == None:
    while True:
      try:
        codigoPacote = int(input("Qual é o Codigo do Pacote: "))
        for p in pacotes:
          if p["codigo"] ==  codigoPacote:
            print("O Codigo está correto!")
            oCodigoFoiEncontrado = True
            pacoteInfos = p
            break
      except:continue
      if oCodigoFoiEncontrado == True:
        break
      else:
        print("O Codigo informado não existe!")
  else:
    oCodigoFoiEncontrado = True

  while True:
    oCpfFoiEncontrado = False
    nomeDoCliente = ""
    try:
      cpf = input("Qual é o Cpf do Comprado já Cadastrado: ")
      for c in clientes:
        if c["cpf"] == cpf:
          print("O Cpf está correto!")
          oCpfFoiEncontrado = True
          nomeDoCliente = c["nome"]
          break
    except:continue
    if oCpfFoiEncontrado == True:
      break
    else:
      print("O Cpf informado não está cadastrado")

  while True:
    data = int(input("Digite a data: "))
    if data > 31:
      print("Não é possivel cadastra um Pacote para a data informada.")
      continue
    break

  quant = 0
  while True:
    try:
      quant = int(input("Digite a Quantidade de Pacotes: "))
      break
    except:continue

  print("Preço: R$"+str(quant * pacoteInfos["valor"]))

  def Comfirma(): 
    global faturamento

    codigo = random.randint(0000,9999)
    print(codigo)
    pedidos.append({
      "cpf":cpf,
      "nome":nomeDoCliente,
      "codigo":codigo,
      "data":data,
      "quant":quant,
      "valor":str(quant * pacoteInfos["valor"]),
      "infos":pacoteInfos
    })


    faturamento =  + (quant * pacoteInfos["valor"])

    print(f"Compra realizada com Suceso.\nNúmero do pedido: {codigo}")

  while True:
    comfirm = input("Deseja realmente Compra: [S,N...] ").lower().strip()[0]
    if (comfirm == "s"):
      Comfirma()
      break
    else:
      print("Compra encerrada!")
      break

def CancelarPacote():
  global faturamento

  pedido = None
  count = None
  while True:
    encontrou = False
    cp = int(input("Qual é o número do pedido: "))
    for c,p in enumerate(pedidos):
      if cp == p["codigo"]:
        pedido = p
        encontrou = True
        count = c
        break
    if (encontrou):
      break

  while True:
    dataCancelou = int(input("Digite a data: "))
    if dataCancelou > 31:
      print("Não é possivel cadastra um Pacote para a data informada.")
      continue
    break

  dataComprou =  pedido["data"]  

  def Multa():
    return (int(pedido["valor"]) * 2)
    
  if dataCancelou < dataComprou:
    print("Você foi multado em R$",Multa())
  else:
    sobra = abs(dataComprou - dataCancelou)
    if (sobra > 7):
      print("Você foi multado em R$",Multa())
    else:
      print("Cancelamento feito com sucesso.\nVocê não foi multado.")

  while True:
    a = input("Deseja realmente cancelar: [S, N] ").lower().strip()[0]
    if (a == "s"):
      print("Compra cancelada.")
      del pedidos[count]
      faturamento += Multa()
      break
    else:
      print("A Compra não foi cancelada.")
      break

def ListarPedidos():
  print("="*digitos)
  print("Pedidos".center(digitos))
  print("="*digitos)

  for e in pedidos:
    print("CPF do Comprador:",e["cpf"])
    print("Destino:",e["infos"]["destino"])
    print("Quantidade:",e["quant"])
    print("Valor Total: R$"+str(e["valor"]))
    print("Número do pedido:",e["codigo"])
    print("\n"+("-"*digitos)+"\n")

  print("Faturamento total: ",faturamento)

def ListarCompradores():
  codigo = None
  while True:
    try:
      codigo = int(input("Digite o Codigo do pacote: "))
      break
    except:
      continue

  compradores = []
  for p in pedidos:
    if p["infos"]["codigo"] == codigo:
      compradores.append([p["nome"],p["quant"]])
  
  print("="*digitos)
  print("Compradores".center(digitos))
  print("="*digitos)
  print("\n")
  if (len(compradores) > 0):
    for c in compradores:
      print(f"Nome: {c[0]}\nQuantidade: {c[1]}\n")
  else:
    print("Pedidos não encontrados")
    
def BuscarPacotes():
  codigo = None
  while True:
    try:
      codigo = int(input("Digite o Codigo do pacote: "))
      break
    except:
      continue

  p = {}
  encontrado = False
  for p_ in pacotes:
    if p_["codigo"] == codigo:
      p = p_
      encontrado = True
      break

  if encontrado:
    print("\nTipo da Viagem:",p["tipo"])
    print("Destino da Viagem:",p["destino"])
    print("Data da Viagem:",p["data"])
    print("Valor da Viagem: R$"+str(p["valor"]))
    print("Codigo da Viagem:",p["codigo"])
    print("\n"+("-"*digitos)+"\n")

  deseja = input('Deseja comprar pacote: [N, S]').strip().upper()[0]
  if deseja == 'S':
    CompraPacotes(codigo)

def ExcluirPacotes():
  codigo = None
  while True:
    try:
      codigo = int(input("Digite o Codigo do pacote: "))
      break
    except:
      continue

  isDeletado = False
  for c_,p_ in enumerate(pacotes):
    if p_["codigo"] == codigo:
      del pacotes[c_]
      isDeletado = True
      break

  if isDeletado:
    print("Deletado com Sucesso.")
  else:
    print("Não foi possivel deletar")


def Menu():
  while True:
    print("="*digitos)
    print("Agência de Viagem".center(digitos))
    print("="*digitos)
    opcoes = [
  "Cadastra Pacotes", "Cadastra Clientes",
  "Listar Pacotes", "Comprar Pacotes", 
  "Cancelar Pacotes", "Listar Pedidos",
  "Lista Compradores", "Buscar Pacote",
  "Excluir Pacote", "Sair do Sistema"
  ]

    for n,c in enumerate(opcoes):
      print(f"[{n}] - {c}")
    print("="*digitos)

    opcao = int(input("Sua opção: "))
    if (opcao > 9 or opcao < 0):
      Clear()
      continue

    if opcao == 0:
      CadastraPacotes()
    elif opcao == 1:
      CadastroClientes()
    elif opcao == 2:
      ListarPacotes()
    elif opcao == 3:
      CompraPacotes()
    elif opcao == 4:
      CancelarPacote()
    elif opcao == 5:
      ListarPedidos()
    elif opcao == 6:
      ListarCompradores()
    elif opcao == 7:
      BuscarPacotes()
    elif opcao == 8:
      ExcluirPacotes()
    elif opcao == 9:
      print("O Programa foi encerrado!")
      sys.exit()
Menu()