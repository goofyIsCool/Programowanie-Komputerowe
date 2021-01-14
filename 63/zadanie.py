from math import sqrt


def zadanie1_(ciag):
    if len(ciag) % 2 == 1:
        return False

    for i in range(int(len(ciag)/2)):
        if ciag[i] != ciag[int(len(ciag)/2)+i]:
            return False

    return True


def zadanie1(arr):
    result = []
    for ciag in arr:
        if zadanie1_(ciag):
            result.append(ciag)

    return result


def zadanie2_(ciag):
    for i in range(len(ciag)-1):
        if ciag[i] == '1' and ciag[i+1] == '1':
            return False

    return True


def zadanie2(arr):
    counter = 0
    for ciag in arr:
        if zadanie2_(ciag):
            counter += 1

    return counter


def czyPierwsza(n):
    if n == 1 or (n % 2 == 0 and n != 2):
        return False
    if n == 2:
        return True

    for i in range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return False

    return True


def zadanie3_(ciag):
    for i in range(1, ciag):
        if (ciag % i == 0 and czyPierwsza(i) and czyPierwsza(ciag/i)):
            # print("[", i, " ", int(ciag/i), "]", " ", int(ciag/i)*i)
            return True

    return False


def zadanie3(arr):
    counter = 0
    max = -1
    min = 100000
    for ciag in arr:
        tmp = int(ciag, 2)
        if zadanie3_(tmp):
            # print(tmp, zadanie3_(tmp))
            counter += 1
            if tmp > max:
                max = tmp
            elif tmp < min:
                min = tmp

    return [counter, min, max]


if __name__ == '__main__':
    with open("ciagi.txt", "r") as f:
        arr = []
        for line in f:
            tmp = int(line)
            arr.append(str(tmp))

    zadanie1odp = zadanie1(arr)
    zadanie2odp = zadanie2(arr)
    zadanie3odp = zadanie3(arr)
    with open("wynik.txt", "w") as f:
        f.write("Zadanie 1. \n")
        for n in zadanie1odp:
            f.write(str(n) + "\n")
        f.write("Zadanie 2. {}".format(zadanie2odp))
        f.write("Zadanie 3. \n")
        f.write("licznik {}\n".format(zadanie3odp[0]))
        f.write("min: {}\n".format(zadanie3odp[1]))
        f.write("max: {}\n".format(zadanie3odp[2]))
