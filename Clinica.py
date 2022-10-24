import os
from sistema import Sistema

class Clinica(Sistema):
    def __init__(self):
        self.dados = {}
        self.agenda = {}

    def login(self):
        login0 = "admin"
        senha = "12345"
        teste = 0

        while(teste == 0):
            print("            Clinica")
            print("--------------------------------\n")
            login1 = input("LOGIN: ")
            if(login0 == login1):
                teste = 1
                senha1 = input("SENHA: ")
                if(senha == senha1):
                    os.system("cls")
                    print("\nLOGADO\n\n\a")
                else:
                    teste = 0
                    print("\nSenha incorreta\n\n\a")
                    os.system("pause")
                    os.system("cls")
            else:
                teste = 0
                print("\nLogin incorreto\n\n\a")
                os.system("pause")
                os.system("cls")
            os.system("cls")

    def menu_principal(self):
        print("                  MENU PRINCIPAL")
        print("--------------------------------------------------\n")
        print("[1] - CADASTRAMENTO")
        print("[2] - AGENDAMENTO")
        print("[3] - CANCELAMENTO")
        print("[4] - LISTAR CONSULTAS")
        print("[5] - LISTAR PACIENTES")
        print("[0] - SAIR")
        try:
            op_menu_principal = int(input("Escolha uma opção: "))
            os.system("cls")
            if op_menu_principal == 1:
                self.cadastrar()
            elif op_menu_principal == 2:
                self.agendar()
            elif op_menu_principal == 3:
                self.deletar()
            elif op_menu_principal == 4:
                self.listar()
            elif op_menu_principal == 5:
                self.listar_pac()
            elif op_menu_principal == 0:
                os.system("cls")
                print("Até logo !\n\n")
                os.system("pause")
            else:
                os.system("cls")
                print("Escolha uma opção válida !!\n\n")
                os.system("pause")
            return op_menu_principal
        except ValueError:
            os.system("cls")
            print("Digite apenas numeros!\n")
            os.system("pause")

    def cadastrar(self):
        print("Cadastro de pacientes\n")
        print("\n-------------------------------------\n")
        nome = input("\nInforme o nome do paciente: ")
        dataNasc = input("\nInforme a data de nascimento do paciente: ")
        while True:
            teste = 0
            cpf = input("\nInforme o CPF do paciente: ")
            for i in self.dados.keys():
                if i == cpf:
                    teste = 1
                    break
            if teste == 0:
                break
            else:
                os.system("cls")
                print("Já existe um paciente com esse cpf!\n")
        self.dados[cpf] = [nome, dataNasc]

        os.system("cls")
        print("Cadastro realizado com sucesso!\n\n")
        os.system("pause")
        os.system("cls")

    def agendar(self):
        os.system("cls")
        achou = 0
        while (achou != 1):
            
            aux = not self.dados
            if (aux):
                op = int(input("Nenhum paciente cadastrado, digite 1 para cadastrar! "))
                if(op == 1):
                    os.system("cls")
                    self.cadastrar()
                else:
                    break
            else:
                print("      Agendamento de pacientes")
                print("------------------------------------\n")
                cpf = input("Informe o cpf do paciente: ")
                os.system("cls")
                for i in self.dados.keys():
                    if (i == cpf):
                        achou = 1
                        print("Paciente:", self.dados[cpf][0])
                        print("\n")
                        os.system("pause")
                        os.system("cls")
                        break
                    
                if achou == 0:
                    if cpf == '-1':
                        break
                    else:
                        os.system("cls")
                        print("Paciente não encontrado, tente novamente! ou digite -1 para sair\n\n")
                        os.system("pause")
                        os.system("cls")

            os.system("cls")
            if(achou == 1):
                teste = 0
                for i in self.agenda.keys():
                    if i == cpf:
                        teste = 1
                        break
                if teste == 0:
                    data = input("Digite uma data: ")
                    hora = input("\nDigite um horario: ")
                    self.agenda[cpf] = [data, hora]
                    os.system("cls")
                    print("AGENDAMENTO REALIZADO COM SUCESSO!")
                    print("\nDia:", data)
                    print("Hora:", hora)
                    os.system("pause")
                else:
                    print("O Paciente", self.dados[cpf][0], "já tem uma consulta agendada!\n")
                    os.system("pause")
                os.system("cls")

    def listar(self):
        aux = not self.agenda
        if (aux):
            print("Nenhuma consulta marcada!\n")
            os.system("pause")
        else:
            os.system("cls")
            print("     Consultas marcadas")
            print("----------------------------")
            for i, j in self.agenda.items():
                print(f"Paciente: {self.dados[i][0]}")
                print(f"CPF: {i}")
                print(f"Data: {j[0]}")
                print(f"Hora: {j[1]}")
                print()
            os.system("pause")

    def listar_pac(self):
        aux = not self.dados
        if (aux):
            print("Nenhum paciente cadastrado!\n")
            os.system("pause")
        else:
            os.system("cls")
            print("     Pacientes cadastrados")
            print("-------------------------------")
            for i, j in self.dados.items():
                print(f"Paciente: {self.dados[i][0]}")
                print(f"Data de Nascimento: {j[1]}")
                print(f"CPF: {i}")
                print()
            os.system("pause")

    def deletar(self):
        aux = not self.agenda
        if(aux):
            os.system("cls")
            print("Nenhuma consulta marcada!\n")
            os.system("pause")
        else:
            teste = 0
            cpf = input("Informe o cpf do paciente: ")
            for i in self.agenda.keys():
                if i == cpf:
                    teste = 1
                    break
            if teste == 1:
                os.system("cls")
                del self.agenda[cpf]
                print("Colsulta cancelada com sucesso!\n")
                os.system("pause")
            else:
                os.system("cls")
                print("Nenhuma consulta encontrada para esse cpf!\n")
                os.system("pause")
