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


def palindrom(liczba):
    s = str(liczba)

    for i in range(len(s)):
        if (s[i] != s[len(s)-1-i]):
            return False

    return True


def palindromSum(liczba):
    tmp = str(liczba)
    liczbaReversed = int(tmp[::-1])

    sum = liczba + liczbaReversed
    if palindrom(sum):
        return True
    else:
        return False


def moc_liczby(liczba, moc):
    tmp = str(liczba)
    iloczyn = 1
    for cyfra in tmp:
        iloczyn *= int(cyfra)

    if iloczyn >= 10:
        return moc_liczby(iloczyn, moc + 1)
    else:
        return moc


if __name__ == '__main__':

    liczby = []
    with open("liczby.txt", "r") as f:
        for line in f:
            liczby.append(int(line))

    counter1 = 0
    counter2 = 0
    counters = [0 for i in range(8)]
    min = 999999999
    max = 0
    for liczba in liczby:
        print(palindromSum(liczba))
        if czynniki(liczba):
            counter1 += 1
        if palindromSum(liczba):
            counter2 += 1

        tmp = moc_liczby(liczba, 1)
        counters[tmp-1] += 1

        if tmp == 1:
            if liczba > max:
                max = liczba
            elif liczba < min:
                min = liczba

    with open("wynik.txt", "w") as f:
        f.write("Zadanie 1. {}\n".format(counter1))
        f.write("Zadnaie 2. {}\n".format(counter2))
        f.write("Zadanie 3.\n")
        for _ in range(len(counters)):
            f.write("Moc {}: {}\n".format(_+1, counters[_]))
        f.write("Minimalna liczba o mocy jeden jest rowna: {}\n".format(min))
        f.write("Maksymalna liczba o mocy jeden jest rowna: {}".format(max))
