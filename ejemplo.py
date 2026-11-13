print("lectura de credenciales a partir de entrada")
with open("entrada.txt","r") as txt:
    for l in txt:
        print(*l.split())