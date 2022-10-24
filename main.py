import os
from clinica import Clinica

def main():
    c = Clinica()
    c.login()
    op_menu_principal = 1
    while(op_menu_principal != 0):
        os.system("cls")
        op_menu_principal = c.menu_principal()
    os.system("cls")

if __name__=="__main__":
    dados = {}
    agenda = {}
    main()