import requests
import os
import time

def clear():
    os.system(["clear", "cls"][os.name == "nt"])

def art():
    print(fCiano + """
                    /i
                    //,
                   ///i
                 ,/ ).'i
                  |   )-i
                  |   )i
    {}b3lial{}        '   )i
                 /    |-
            _.-./-.  /z_
             `-. >._\ _ );i.
              / `-'/`k-'`u)-'`
             /    )-
      ,.----'   ) '
      /      )1`
     ///v`-v\\v
    /v  BP{}""".format(fReset, fCiano, fReset))

fPreto = '\033[2;30m'
fBranco = '\033[1;97m'
fVermelho = '\033[1;91m'
fAzul = '\033[1;34m'
fAmarelo = '\033[1;33m'
fVerde = '\033[1;92m'
fCiano = '\033[1;36m'
fReset = '\033[m'

try:
    clear()
    time.sleep(1)
    art()
    url = input("\nSite {}‒ {}".format(fCiano, fReset))
    question = input("Deseja personalizar a wordlist? s/N ").lower()
    if question == "s":
        wordlist = input("Local da wordlist {}‒ {}".format(fCiano, fReset))
        f = open(wordlist, "r")
        path = f.readlines()
        path = list(map(lambda a: a.strip(), path))
        f = open(wordlist)
        linhas = 0
        for item in f:
            linhas = linhas + 1
    else:
        f = open("path.txt", "r")
        path = f.readlines()
        path = list(map(lambda a: a.strip(), path))
        f = open("path.txt")
        linhas = 0
        for item in f:
            linhas = linhas + 1
    url = "{}{}".format(url, path[0])
    print()
    res = requests.get(url)
    if res.status_code == 200:
        print("{} {}Diretório existente{}".format(url, fVerde, fReset))
    elif res.status_code == 404:
        print("{} {}Diretório inexistente{}".format(url, fVermelho, fReset))
    else:
        print("{} {}Requisição bloqueada. Use proxychains seu filho da puta{}".format(url, fAmarelo, fReset))

    for a in range(0, linhas):
        url = url.replace(path[a], "")
        url = "{}{}".format(url, path[a+1])
        res = requests.get(url)
        if res.status_code == 200:
            print("{} {}Diretório existente{}".format(url, fVerde, fReset))
        elif res.status_code == 404:
            print("{} {}Diretório inexistente{}".format(url, fVermelho, fReset))
        else:
            print("{} {}Requisição bloqueada. Use proxychains seu filho da puta{}".format(url, fAmarelo, fReset))

except KeyboardInterrupt:
    print("\nVolte sempre.")

except IndexError:
    exit()

except requests.exceptions.MissingSchema:
    print("Seu baiano desgraçado, cê não viu que o formato certo é http://www.example.com/? >:(")

except requests.exceptions.ConnectionError:
    print("Seu baiano arrombado, cê não viu que o formato certo é http://www.example.com/? >:(")
