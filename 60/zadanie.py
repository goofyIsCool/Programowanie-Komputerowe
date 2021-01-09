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


def nwd(a, b):
    if a < b:
        return nwd(b, a)
    if b == 0:
        return a

    return nwd(b, a % b)


if __name__ == '__main__':
    counter = 0
    last = 0
    secondLast = 0
    numbers = []
    box = []
    with open("liczby.txt", "r") as f:
        for line in f:
            liczba = int(line)
            if liczba < 1000:
                counter += 1
                secondLast = last
                last = liczba

            tmp = dzielniki(liczba)
            if tmp is not False:
                box.append([liczba, tmp])

            numbers.append(liczba)

    najwiekszaPierwsza = 0
    for i in range(len(numbers)):
        ok = True
        for j in range(len(numbers)):
            if i != j and nwd(numbers[i], numbers[j]) > 1:
                ok = False

        if ok and numbers[i] > najwiekszaPierwsza:
            najwiekszaPierwsza = numbers[i]

    with open("wynik.txt", "w") as f:
        f.write("Zadanie 1.\n")
        f.write("W pliku liczby.txt znajduje sie {} liczb mniejszych od 1000\n".format(counter))
        f.write("Ostatnia: {} \nPrzedostatnia: {}\n".format(last, secondLast))
        f.write("Zadanie 2.\n")
        for _ in box:
            f.write(str(_[0]) + " " + str(_[1]) + "\n")
        f.write("Zadanie 3.\n")
        f.write("Najwieksza wzglednie pierwsza: {}".format(najwiekszaPierwsza))
