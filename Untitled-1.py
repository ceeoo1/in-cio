import os

mensagens = [] #type: ignore

nome = input("nome: ")

# limpando terminal do windows (cls)

while True: 
    os.system('cls')
    
    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("________")

    # obter texto do chat

    texto = input("mensagem: ")
    if texto == "fim":
        break
    
    # adicionando mensagens na lista

    mensagens.append ({
        "nome": nome,
        "texto": texto
    })
    
   
        
