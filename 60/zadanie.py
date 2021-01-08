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

            numbers.append(liczba)

    print("Zadanie 1.")
    print("W pliku liczby.txt znajduje sie {} liczb mniejszych od 1000".format(counter))
    print("Ostatnia: {} \nPrzedostatnia: {}".format(last, secondLast))

    najwiekszaPierwsza = 0
    for i in range(len(numbers)):
        ok = True
        for j in range(len(numbers)):
            if i != j and nwd(numbers[i], numbers[j]) > 1:
                ok = False

        if ok and numbers[i] > najwiekszaPierwsza:
            najwiekszaPierwsza = numbers[i]

    print("Najwieksza wzglednie pierwsza: {}".format(najwiekszaPierwsza))
