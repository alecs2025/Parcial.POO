class ItemBiblioteca:
    def __init__(self, titulo, ano_publicacao):
        self._titulo = titulo
        self.ano_publicacao = ano_publicacao

        def titulo(self):
        return self._titulo


    def titulo(self, valor):
        self._titulo = valor

        def ano_publicacao(self):
        return self._ano_publicacao

    
    def ano_publicacao(self, valor):
        if valor > 0:
            self._ano_publicacao = valor
        else:
            print("Erro: Ano de publicação deve ser positivo.")

    def apresentar_detalhes(self):
        return f"Título: {self._titulo} | Ano: {self._ano_publicacao}"


class Livro(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, autor, num_paginas):
        super().__init__(titulo, ano_publicificacao)
        self._autor = autor
        self.num_paginas = num_paginas

    
    def num_paginas(self):
        return self._num_paginas

    
    def num_paginas(self, valor):
        if valor > 50:
            self._num_paginas = valor
        else:
            print("Erro: Um livro deve ter mais de 50 páginas.")

    def apresentar_detalhes(self):
        return (
            f"[LIVRO] Título: {self._titulo} | Ano: {self._ano_publicacao} | "
            f"Autor: {self._autor} | Páginas: {self._num_paginas}"
        )


class Revista(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, edicao, volume):
        super().__init__(titulo, ano_publicificacao)
        self._edicao = edicao
        self._volume = volume

    def apresentar_detalhes(self):
        return (
            f"[REVISTA] Título: {self._titulo} | Ano: {self._ano_publicacao} | "
            f"Edição: {self._edicao} | Volume: {self._volume}"
        )


acervo = []


def cadastrar_livro():
    titulo = input("Título do livro: ")
    ano = int(input("Ano de publicação: "))
    autor = input("Autor: ")
    paginas = int(input("Número de páginas: "))

    livro = Livro(titulo, ano, autor, paginas)
    acervo.append(livro)
    print("Livro cadastrado com sucesso!\n")


def cadastrar_revista():
    titulo = input("Título da revista: ")
    ano = int(input("Ano de publicação: "))
    edicao = int(input("Edição: "))
    volume = int(input("Volume: "))

    revista = Revista(titulo, ano, edicao, volume)
    acervo.append(revista)
    print("Revista cadastrada com sucesso!\n")


def listar_acervo():
    if not acervo:
        print("Acervo vazio.\n")
        return
    for item in acervo:
        print(item.apresentar_detalhes())
    print()


while True:
    print("--- Sistema de Biblioteca ---")
    print("1. Cadastrar Livro")
    print("2. Cadastrar Revista")
    print("3. Listar Acervo")
    print("4. Sair")
    opc = input("Escolha uma opção: ")

    if opc == "1":
        cadastrar_livro()
    elif opc == "2":
        cadastrar_revista()
    elif opc == "3":
        listar_acervo()
    elif opc == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida!\n")

