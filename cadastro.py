import json

ARQUIVO = "classes.json"


def carregar():
    arquivo = open(ARQUIVO, "r", encoding="utf-8")
    lista = json.load(arquivo)
    arquivo.close()
    return lista

def salvar(lista):
    arquivo = open(ARQUIVO, "w", encoding="utf-8")
    json.dump(lista, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()

def buscar_por_nome(lista, nome):
    for classe in lista:
        if classe["nome"].lower() == nome.lower():
            return classe
    return None

def ler_numero(mensagem):
    while True:
        texto = input(mensagem)
        if texto.isdigit():
            return int(texto)
        print("Digite apenas números")

def mostrar_classe(classe):
    print(f"{classe['nome']} | Dano base: {classe['dano_base']} | "
          f"Tipo de dano: {classe['tipo_dano']}")

def incluir(lista):
    print("\n- INCLUIR CLASSE")
    nome = input("Nome da classe: ")

    existente = buscar_por_nome(lista, nome)
    if existente is not None:
        print("Classe já existente, mudando para alteração")
        alterar(lista, existente["nome"])
        return

    dano_base = ler_numero("Dano base: ")
    tipo_dano = input("Tipo de dano: ")

    classe = {
        "nome": nome,
        "dano_base": dano_base,
        "tipo_dano": tipo_dano
    }
    lista.append(classe)
    salvar(lista)
    print("Classe cadastrada")

def alterar(lista, nome=None):
    print("\n- ALTERAR CLASSE")
    if nome is None:
        nome = input("Nome da classe: ")

    classe = buscar_por_nome(lista, nome)
    if classe is None:
        print("Classe não encontrada")
        return

    print("Dados atuais")
    mostrar_classe(classe)
    print("(Deixe em branco para manter o valor atual)")

    dano_base = input("Novo dano base: ")
    if dano_base.isdigit():
        classe["dano_base"] = int(dano_base)

    tipo_dano = input("Novo tipo de dano: ")
    if tipo_dano != "":
        classe["tipo_dano"] = tipo_dano

    salvar(lista)
    print("Classe alterada")

def excluir(lista):
    print("\n- EXCLUIR CLASSE")
    nome = input("Nome da classe: ")

    classe = buscar_por_nome(lista, nome)
    if classe is None:
        print("Classe não encontrada")
        return

    mostrar_classe(classe)
    confirma = input("Deseja realmente excluir (s/n): ")
    if confirma.lower() == "s":
        lista.remove(classe)
        salvar(lista)
        print("Classe excluída")
    else:
        print("Exclusão cancelada")

def pesquisar(lista):
    print("\n- PESQUISAR (Selecione a ordem)")
    print("1 - Por nome")
    print("2 - Por tipo de dano")
    opcao = input("Escolha: ")

    if opcao == "1":
        campo = "nome"
    elif opcao == "2":
        campo = "tipo_dano"
    else:
        print("Opção inválida")
        return

    termo = input("Digite o texto a procurar: ").lower()
    encontrou = False

    for classe in lista:
        if termo in classe[campo].lower():
            mostrar_classe(classe)
            encontrou = True

    if not encontrou:
        print("Nenhuma classe encontrada")

def ordenar(lista, campo):
    copia = lista[:]
    if campo == "nome":
        copia.sort(key=lambda classe: classe["nome"].lower())
    else:
        copia.sort(key=lambda classe: classe["dano_base"])
    return copia

def listar(lista):
    print("\n- LISTAR CLASSES (Selecione a ordem)")
    print("1 - Nome")
    print("2 - Dano base")
    opcao = input("Escolha: ")

    if opcao == "1":
        ordenada = ordenar(lista, "nome")
    elif opcao == "2":
        ordenada = ordenar(lista, "dano_base")
    else:
        print("Opção inválida")
        return

    if len(ordenada) == 0:
        print("Nenhuma classe cadastrada")
        return

    print()
    for classe in ordenada:
        mostrar_classe(classe)

classes = carregar()

while True:
    print("\n- CADASTRO DE CLASSES DE RPG")
    print("1 - Incluir")
    print("2 - Alterar")
    print("3 - Excluir")
    print("4 - Pesquisar")
    print("5 - Listar")
    print("0 - Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        incluir(classes)
    elif escolha == "2":
        alterar(classes)
    elif escolha == "3":
        excluir(classes)
    elif escolha == "4":
        pesquisar(classes)
    elif escolha == "5":
        listar(classes)
    elif escolha == "0":
        print("Encerrando processo")
        break
    else:
        print("Opção inválida")

    input("Aperte ENTER para continuar")