import random
from linecache import getline
import time
import hashlib

hash = '35a1dadffafe27481b8ffac2a473d942b08c28d4831686b2d7d958162f2b331e'
password = input("Podaj hasło: ")
if hashlib.sha256(password.encode()).hexdigest() == hash:
    pass
else:
    print("zle haslo")
    exit(2)

listaPL = []
listaDE = []
listaGEDE = []
listaPRDE = []
punktyde = 0
punktygede = 0
punktyprde = 0

timestart = 0
timeend = 0

def PL(linia):
    return getline("CzasownikiPL.txt", linia).strip()

def DE(linia):
    return getline("CzasownikiDE.txt", linia).strip()

def GEDE(linia):
    return getline("CzasownikiGEDE.txt", linia).strip()
def PRDE(linia):
    return getline("CzasownikiPRDE", linia).strip()

def clear():
    print('\n' * 100)

clear()
print("Hasło OK")


def ktoryTest():
    while True:
        clear()
        print('Który to test?')
        ktory = input('Podaj cyfre 1-4:')
        match ktory:
            case '1':
                losowe = random.sample(range(1, 11), 10)
                for losowa in losowe:
                    listaPL.append(PL(losowa))
                    listaDE.append(DE(losowa))
                    listaGEDE.append(GEDE(losowa))
                    listaPRDE.append(PRDE(losowa))
                break
            case '2':
                listaPL.clear()
                listaDE.clear()
                listaPRDE.clear()
                listaGEDE.clear()
                losowe = random.sample(range(11, 21), 10)
                for losowa in losowe:
                    listaPL.append(PL(losowa))
                    listaDE.append(DE(losowa))
                    listaGEDE.append(GEDE(losowa))
                    listaPRDE.append(PRDE(losowa))
                break
            case '3':
                listaPL.clear()
                listaDE.clear()
                listaPRDE.clear()
                listaGEDE.clear()
                losowe = random.sample(range(21, 31), 10)
                for losowa in losowe:
                    listaPL.append(PL(losowa))
                    listaDE.append(DE(losowa))
                    listaGEDE.append(GEDE(losowa))
                    listaPRDE.append(PRDE(losowa))
                break
            case '4':
                pass
                break
            case _:
                pass
                clear()
    clear()



while True:
    print('#' * 51)
    print('#' * 16, 'Nauczaniator 3000', '#' * 16)
    print('#' * 51)
    print('')
    print('')
    print('1. Practise Mode')
    print('2. Test Mode')
    mode = input()

    if mode == '1':
        ktoryTest()
        for i in range(0, 10):
            print(f"Słowo {listaPL[i]} jest po niemiecku {listaDE[i]}, w perfekt jest {listaGEDE[i]} i w prateritum {listaPRDE[i]}")
            input()
            clear()
    elif mode == '2':
        ktoryTest()
        timestart = int(time.time())
        for i in range(0, 10):
            print(f"Słowo: {listaPL[i]} po niemiecku to: ", end="")
            odp1 = input()
            print("W perfekt to: ", end="")
            odp2 = input()
            print("A w Prateritum to: ", end="")
            odp3 = input()
            print("")
            print("")
            if odp1 == listaDE[i]:
                print("Dobrze, +1 punkt")
                punktyde += 1
            else:
                print(f"Źle, {listaPL[i]} to {listaDE[i]}")

            if odp2 == listaGEDE[i]:
                print("Dobrze, +1 punkt")
                punktygede += 1
            else:
                print(f"Źle, w perfekt {listaDE[i]} to {listaGEDE[i]}")

            if odp3 == listaPRDE[i]:
                print("Dobrze, +1 punkt")
                punktyprde += 1
            else:
                print(f"Źle, w prateritum {listaDE[i]} to {listaPRDE[i]}")
            input()
            clear()
        timeend = int(time.time())
        print(f"{punktyde}/10 z niemieckiego")
        print(f"{punktygede}/10 z perfekt")
        print(f"{punktyprde}/10 z prateritum")
        srednia = (punktyde + punktygede + punktyprde) // 3
        print(f"Srednia to: {srednia}")
        czas = srednia / (timeend - timestart)
        print(f"punktow {czas}")
        punktyde = 0
        punktyprde = 0
        punktygede = 0

    elif mode == 'exit':
        exit()
    else:
        clear()