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


if __name__ == '__main__':

    liczby = []
    with open("liczby.txt", "r") as f:
        for line in f:
            liczby.append(int(line))

    counter1 = 0
    counter2 = 0
    for liczba in liczby:
        # print(palindromSum(liczba))
        # if czynniki(liczba):
        #     counter1 += 1
        if palindromSum(liczba):
            counter2 += 1

    # print("Zadanie1. {}".format(counter))
    # 114
    print("Zadnaie2. {}".format(counter2))
    # 181
