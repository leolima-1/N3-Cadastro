# N3-Cadastro
Alunos: Leonard Yamamoto Lima, João Victor Teixeira / 1 Semestre
# Atividade N3: criação de cadastro

Aula de estrutura de dados 

Tema:

# Cadastro de RPG de mesa:

O programa funciona como um pequeno cadastro de classes de RPG, guardadas no arquivo classes.json. Cada classe é representada por um objeto com três campos: nome, dano base e tipo dano. Por exemplo:

{
 
  "nome": "guerreiro",
  "dano_base": 15,
  "tipo_dano": "fisico"
  
}

Ao iniciar, carregar lê o JSON e transforma seu conteúdo em uma lista Python. O programa então entra em um ciclo que exibe o menu e espera uma opção. Esse ciclo continua até a pessoa escolher 0. Quando há uma alteração, ele salvar e grava a lista atualizada no arquivo, com indentação para melhorar a leitura.

# As principais funções são:

• incluir(lista): pede os dados de uma nova classe. Se já existir uma classe com o mesmo nome, encaminha para alteração. ler_numero() valida o dano base, aceitando apenas números inteiros não negativos.

• alterar(lista, nome=None): procura a classe pelo nome e permite mudar o dano ou o tipo de dano. Campos deixados em branco mantêm o valor atual.

• excluir(lista): pede o nome, mostra os dados encontrados e só remove a classe se a confirmação for s(sim).

• pesquisar(lista): permite procurar por nome ou tipo de dano. A pesquisa encontra correspondências parciais e não diferencia maiúsculas de minúsculas.

• ordenar(lista, campo) e listar(lista): organizam e exibem as classes por nome ou por dano base. A ordenação é feita sobre uma cópia da lista, sem mudar a ordem original dos dados.

#Nota

Caso o número do dano não seja do tipo Int:inteiro, o programa irá ignora-lo e continua para a finalização/alteração do cadastro
