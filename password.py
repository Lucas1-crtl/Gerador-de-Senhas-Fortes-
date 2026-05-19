import random
import string
import time

def sair():
    cont = 0
    
    while cont <1:
        time.sleep(1)
        print("SAINDO DO SISTEMA") 
        cont+=1
        
          
        
        
def acessar():
    a = input("USUÁRIO:")
    b = input("SENHA: ")
    ipc = 0
    
    if a == "admin" and b == "senha":
        while ipc <10:
            
            print("ACESSO GARANTIDO\n ")
            caracteres = string.ascii_letters + string.digits
            string_final= "".join(random.choices(caracteres, k=12))
            time.sleep(2)
            print("SENHA CRIADA: ",string_final)
            ipc+=1
           
        return True
        menu()    
        
            

    else:
        print("Acesso Negado!")
        return False

    
    
def menu():
    while True:
        print("--- SISTEMA ---")
        print("1 - Acessar Sistema")
        print("2 - Sair")
    
    
        opc = (input("Digite uma opção: "))

        match opc:    
            case "1":
                if acessar():
                    menu()
                    break
     
            case "2":
                sair()
                break
            case _:
                print("Invádido")        
        
        
menu()        
        
        
