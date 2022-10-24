import os

def login():
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

def menu_principal():
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
            cadastrar()
        elif op_menu_principal == 2:
            agendar()
        elif op_menu_principal == 3:
            deletar()
        elif op_menu_principal == 4:
            listar()
        elif op_menu_principal == 5:
            listar_pac()
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

def cadastrar():
    print("Cadastro de pacientes\n")
    print("\n-------------------------------------\n")
    nome = input("\nInforme o nome do paciente: ")
    dataNasc = input("\nInforme a data de nascimento do paciente: ")
    while True:
        teste = 0
        cpf = input("\nInforme o CPF do paciente: ")
        for i in dados.keys():
            if i == cpf:
                teste = 1
                break
        if teste == 0:
            break
        else:
            os.system("cls")
            print("Já existe um paciente com esse cpf!\n")
    dados[cpf] = [nome, dataNasc]

    os.system("cls")
    print("Cadastro realizado com sucesso!\n\n")
    os.system("pause")
    os.system("cls")

def agendar():
    os.system("cls")
    achou = 0
    while (achou != 1):
        aux = not dados
        if (aux):
            op = int(input("Nenhum paciente cadastrado, digite 1 para cadastrar! "))
            if(op == 1):
                os.system("cls")
                cadastrar()
            else:
                break
        else:
            print("      Agendamento de pacientes")
            print("------------------------------------\n")
            cpf = input("Informe o cpf do paciente: ")
            os.system("cls")
            for i in dados.keys():
                if (i == cpf):
                    achou = 1
                    print("Paciente:",dados[cpf][0])
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
            for i in agenda.keys():
                if i == cpf:
                    teste = 1
                    break
            if teste == 0:
                data = input("Digite uma data: ")
                hora = input("\nDigite um horario: ")
                agenda[cpf] = [data, hora]
                os.system("cls")
                print("AGENDAMENTO REALIZADO COM SUCESSO!")
                print("\nDia:", data)
                print("Hora:", hora)
                os.system("pause")
            else:
                print("O Paciente", dados[cpf][0], "já tem uma consulta agendada!\n")
                os.system("pause")
            os.system("cls")

def listar():
    aux = not agenda
    if (aux):
        print("Nenhuma consulta marcada!\n")
        os.system("pause")
    else:
        os.system("cls")
        print("     Consultas marcadas")
        print("----------------------------")
        for i, j in agenda.items():
            print(f"Paciente: {dados[i][0]}")
            print(f"CPF: {i}")
            print(f"Data: {j[0]}")
            print(f"Hora: {j[1]}")
            print()
        os.system("pause")

def listar_pac():
    aux = not dados
    if (aux):
        print("Nenhum paciente cadastrado!\n")
        os.system("pause")
    else:
        os.system("cls")
        print("     Pacientes cadastrados")
        print("-------------------------------")
        for i, j in dados.items():
            print(f"Paciente: {dados[i][0]}")
            print(f"Data de Nascimento: {j[1]}")
            print(f"CPF: {i}")
            print()
        os.system("pause")

def deletar():
    aux = not agenda
    if(aux):
        os.system("cls")
        print("Nenhuma consulta marcada!\n")
        os.system("pause")
    else:
        teste = 0
        cpf = input("Informe o cpf do paciente: ")
        for i in agenda.keys():
            if i == cpf:
                teste = 1
                break
        if teste == 1:
            os.system("cls")
            del agenda[cpf]
            print("Colsulta cancelada com sucesso!\n")
            os.system("pause")
        else:
            os.system("cls")
            print("Nenhuma consulta encontrada para esse cpf!\n")
            os.system("pause")

def main():
    login()
    op_menu_principal = 1
    while(op_menu_principal != 0):
        os.system("cls")
        op_menu_principal = menu_principal()
    os.system("cls")

if __name__=="__main__":
    dados = {}
    agenda = {}
    main()
