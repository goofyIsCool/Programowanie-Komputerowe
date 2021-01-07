def czynniki(liczba):
    ile = 0
    czynnik = 3
    if liczba % 2 == 0:
        return False
    while liczba > 1:
        if liczba % czynnik == 0:
            ile += 1
        while liczba % czynnik == 0:
            liczba = liczba/czynnik

        czynnik = czynnik+2
        if ile > 3:
            return False

    if ile == 3:
        return True
    if ile < 3:
        return False


if __name__ == '__main__':

    liczby = []
    with open("liczby.txt", "r") as f:
        for line in f:
            liczby.append(int(line))

    counter = 0
    for liczba in liczby:
        print(czynniki(liczba))
        if czynniki(liczba):
            counter += 1

    print("Zadanie1. {}".format(counter))
