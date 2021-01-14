def zadanie1(arr):
    min = 1000
    for ulamek in arr:
        ulamek = ulamek.split(" ")
        licznik = int(ulamek[0])
        mianownik = int(ulamek[1])

        if licznik / mianownik < min:
            min = licznik / mianownik
            tmp = [licznik, mianownik]

    return tmp


def dzielniki(n):
    arr = []
    for i in range(2, n):
        if n % i == 0:
            arr.append(i)

    return arr


def czySkracalny(a, b):
    if a == b and a != 1:
        return False

    arr = dzielniki(max(a, b))
    tmp = min(a, b)
    for czynnik in arr:
        if tmp % czynnik == 0:
            return False

    return True


def zadanie2(arr):
    counter = 0
    for ulamek in arr:
        ulamek = ulamek.split(" ")
        licznik = int(ulamek[0])
        mianownik = int(ulamek[1])
        if czySkracalny(licznik, mianownik):
            counter += 1

    return counter


def czynniki(n):
    arr = []
    for i in range(2, n):
        if n % i == 0:
            arr.append(i)
            n = n/i

    arr.append(int(n))
    arr.sort()
    return arr


def skrocUlamek(a, b):
    czynnikiA = czynniki(a)
    czynnikiB = czynniki(b)
    # print(czynnikiA)
    # print(czynnikiB)
    i = 0
    while i < (len(czynnikiA)):
        j = 0
        while j < (len(czynnikiB)):
            if czynnikiA[i] == czynnikiB[j]:
                czynnikiA.remove(czynnikiA[i])
                czynnikiB.remove(czynnikiB[j])
            j += 1
        i += 1
    a = 1
    b = 1
    for e in czynnikiA:
        a *= e

    for e in czynnikiB:
        b *= e

    return [a, b]


def nwd(n, m):
    if (n < m):
        return nwd(m, n)
    if (m == 0):
        return n

    return nwd(m, n % m)


def zadanie3(arr):
    sum = 0
    for ulamek in arr:
        ulamek = ulamek.split(" ")
        licznik = int(ulamek[0])
        mianownik = int(ulamek[1])
        d = nwd(licznik, mianownik)
        sum += licznik/d

    return int(sum)


def zadanie4(arr):

    licznikR = 0
    mianownikR = 2*3*5*7*13*2*3*5*7
    for ulamek in arr:
        ulamek = ulamek.split(" ")
        licznik = int(ulamek[0])
        mianownik = int(ulamek[1])

        licznikR += licznik*mianownikR/mianownik

    return int(licznikR)


if __name__ == '__main__':
    with open("dane_ulamki.txt", "r") as f:
        arr = []
        for line in f:
            arr.append(line)

    zadanie1odp = zadanie1(arr)
    zadanie2odp = zadanie2(arr)
    zadanie3odp = zadanie3(arr)
    zadanie4odp = zadanie4(arr)
    with open("wynik.txt", "w") as f:
        f.write("Zadanie 1. {}\n".format(zadanie1odp))
        f.write("Zadanie 2. {}\n".format(zadanie2odp))
        f.write("Zadanie 3. {}\n".format(zadanie3odp))
        f.write("Zadanie 4. {}\n".format(zadanie4odp))
