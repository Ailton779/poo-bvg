
class Cliente:
    def __init__(self, nome, idade, saldo):
        # Atributos privados (encapsulamento)
        self.__nome = nome
        self.__idade = idade
        self.__saldo = saldo

    # Método para exibir as informações do cliente
    def mostrar_informacoes(self):
        print(f"Cliente: {self.__nome}, Idade: {self.__idade}, Saldo: {self.__saldo}")

    # Método para atualizar o saldo do cliente
    def atualizar_saldo(self, valor):
        self.__saldo += valor

    # Métodos para acessar os atributos (se necessário)
    def get_nome(self):
        return self.__nome

    def get_saldo(self):
        return self.__saldo



# Criando uma instância (objeto) da classe Cliente
cliente1 = Cliente("João Silva", 30, 1000.0)

# Exibindo informações do cliente
cliente1.mostrar_informacoes()

# Atualizando o saldo
cliente1.atualizar_saldo(500.0)

# Exibindo informações novamente
cliente1.mostrar_informacoes()
