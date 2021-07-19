import requests
import os
import time

def clear():
    os.system(["clear", "cls"][os.name == "nt"])

def art():
    print(fCiano + f"""
                    /i
                    //,
                   ///i
                 ,/ ).'i
                  |   )-i
                  |   )i
    {fReset}b3lial{fCiano}        '   )i
                 /    |-
            _.-./-.  /z_
             `-. >._\ _ );i.
              / `-'/`k-'`u)-'`
             /    )-
      ,.----'   ) '
      /      )1`
     ///v`-v\\v
    /v  BP{fReset}""")

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
    url = input(f"\nSite {fCiano}‒ {fReset}")
    question = input(f"Deseja personalizar a wordlist? s/N ").lower()
    if question == "s":
        wordlist = input(f"Local da wordlist {fCiano}‒ {fReset}")
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
    url = f"{url}{path[0]}"
    print()
    res = requests.get(url)
    if res.status_code == 200:
        print(f"{url} {fVerde}Diretório existente{fReset}")
        file = open("200.txt", "w")
        file.write(f"{url}\n")
    elif res.status_code == 404:
        print(f"{url} {fVermelho}Diretório inexistente{fReset}")
    else:
        print(f"{url} {fAmarelo}Requisição bloqueada. Tente usar proxychains - VPN.{fReset}")

    for a in range(0, linhas):
        url = url.replace(path[a], "")
        url = f"{url}{path[a+1]}"
        res = requests.get(url)
        if res.status_code == 200:
            print(f"{url} {fVerde}Diretório existente{fReset}")
            file.write(f"{url}\n")
        elif res.status_code == 404:
            print(f"{url} {fVermelho}Diretório inexistente{fReset}")
        else:
            print(f"{url} {fAmarelo}Requisição bloqueada. Tente usar proxychains - VPN.{fReset}")

except KeyboardInterrupt:
    print(f"\nVolte sempre.")

except IndexError:
    exit()

except requests.exceptions.MissingSchema:
    print(f"Seu baiano desgraçado, cê não viu que o formato certo é http://www.example.com/? >:(")

except requests.exceptions.ConnectionError:
    print(f"Seu baiano arrombado, cê não viu que o formato certo é http://www.example.com/? >:(")
