import os
import time




#\033[1;30m Branco
#\033[1;31m Vermelho
#\033[1;32m Verde
#\033[1;33m Amarelo
#\033[1;34m Azul
#\033[1;35m Roxo
#\033[1;36m Ciano
#\033[1;37m Cinza Claro


os.system("clear")
os.system("pkg install figlet")
os.system("clear")
print("\033[1;36m")
os.system("figlet Cracker")
print("""\033[1;35m
=-=-=-=-=-=-=-=-=-=-=-=-=
l     HackScriptv2      l
=-=-=-=-=-=-=-=-=-=-=-=-=
l    [1]Install Update  l
l    [2]Install upgrade l
l    [3]Install git     l
l    [4]Install wget    l
l    [5]Install python  l
l    [6]Install python2 l
l    [7]Install python3 l
l    [8]Install openssh l
l    [9]Install php     l
l    [10]Install Ruby   l
l    [11]Install clang  l
l    [12]Install Tor    l
l    [13]Install figlet l
l    [14]Install cmatrixl
l    [15]Install sl     l
l    [16]Install Perl   l
l    [17]Install Curl   l
l    [18]Sair/Exit      l
[i]Digite o nome        l
ou o numero da opção!   l
l-=-=-=-=-=-=-=-=-=-=-=-l
""")
op = input(">>> ")

if op == "1":
    os.system("clear")
    os.system("pkg update")
    os.system("python3 cacker.py")
elif op == "2":
    os.system("clear")
    os.system("pkg install upgrade")
    os.system("python3 cracker.py")
elif op == "3":
    os.system("clear")
    os.system("pkg install git")
    os.system("python3 cracker.py")
elif op == "4":
    os.system("clear")
    os.system("pkg install wget")
    os.system("python3 cracker.py")
elif op == "5":
    os.system("clear")
    os.system("pkg install python")
    os.system("python3 cracker.py")
elif op == "6":
    os.system("clear")
    os.system("pkg install python2")
    os.system("python3 cracker.py")
elif op == "7":
    os.system("clear")
    os.system("pkg unstall python3")
    os.system("python3 cracker.py")
elif op == "8":
    os.system("clear")
    os.system("pkg install ssh")
    os.system("python3 cracker.py")
elif op == "9":
    os.syatem("clear")
    os.system("pkg install php")
    os.system("python3 cracker.py")
elif op == "10":
    os.system("clear")
    os.system("pkg install ruby")
    os.system("python3 cracker.py")
elif op == "11":
    os.system("clear")
    os.system("pkg install clang")
    os.system("python3 cracker.py")
elif op == "12":
    os.system("clear")
    os.system("pkg install Tor")
    os.system("python3 cracker.py")
elif op == "13":
    os.system("clear")
    os.system("pkg install figlet")
    os.system("python3 cracker.py")
elif op == "14":
    os.system("clear")
    os.system("pjg install cmatrix")
    os.system("python3 cracker.py")
elif op == "15":
    os.system("clear")
    os.system("pkg install sl")
    os.system("python3 cracker.py")
elif op == "16":
    os.system("clear")
    os.system("pkg install perl")
    os.system("python3 cracker.py")
elif op == "17":
    os.system("clear")
    os.system("pkg install curl")
    os.system("python3 cracker.py")
elif op == "18":
    print("Vc quer sair deste programa?")
    print("""
    1 Sim 
    2 não
    """)
    op = input("_")
    if op == "1":
        print("Ok, Estou Saindo por vc!!")
        time.sleep(6)
        os.system("clear")
        exit()
    if op == "2":
        os.system("python3 cracker.py")
else:
    os.system("python3 cracker.py")