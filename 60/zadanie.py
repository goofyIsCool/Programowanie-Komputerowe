from math import sqrt


def dzielniki(liczba):
    tmp = [1, liczba]
    for i in range(2, liczba):
        if liczba % i == 0:
            tmp.append(i)
        if len(tmp) > 18:
            return False

    if len(tmp) < 18:
        return False
    return sorted(tmp)


if __name__ == '__main__':
    counter = 0
    last = 0
    secondLast = 0
    print("Zadanie 2.")
    with open("liczby.txt", "r") as f:
        for line in f:
            liczba = int(line)
            if liczba < 1000:
                counter += 1
                secondLast = last
                last = liczba

            tmp = dzielniki(liczba)
            if tmp is not False:
                print(liczba, tmp)

    print("Zadanie 1.")
    print("W pliku liczby.txt znajduje sie {} liczb mniejszych od 1000".format(counter))
    print("Ostatnia: {} \nPrzedostatnia: {}".format(last, secondLast))
