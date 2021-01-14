def zadanie1(arr):
    max = 0
    min = 1000000
    for e in arr:
        if e > max:
            max = e
        elif e < min:
            min = e

    return [oct(min)[2:], oct(max)[2:]]


def zadanie2(arr):
    pierwszy = 0
    maxLength = 0
    length = 1

    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            length = 1
            pierwszy = arr[i]
        else:
            length += 1

        if length > maxLength:
            maxLength = length
            maxPierwszy = pierwszy

    return [maxPierwszy, maxLength]


def zadanie3(arr1, arr2):
    LicznikA = 0
    LicznikB = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            LicznikA += 1
        if arr1[i] >= arr2[i]:
            LicznikB += 1

    return [LicznikA, LicznikB]


def zadanie4_(number):
    counter = 0
    for c in number:
        if c == '6':
            counter += 1

    return counter


def zadanie4(arr):
    counter = 0
    counter2 = 0
    for e in arr:
        tmp = str(e)
        tmp2 = str(oct(e))
        if '6' in tmp:
            counter += zadanie4_(tmp)
        if '6' in tmp2:
            counter2 += zadanie4_(tmp2)

    return [counter, counter2]


if __name__ == '__main__':
    with open("liczby1.txt", "r") as f:
        arr1 = []
        for line in f:
            arr1.append(int(line, 8))

    zadanie1odp = zadanie1(arr1)

    with open("liczby2.txt", "r") as f:
        arr2 = []
        for line in f:
            arr2.append(int(line))

    zadanie2odp = zadanie2(arr2)
    zadanie3odp = zadanie3(arr1, arr2)
    zadanie4odp = zadanie4(arr2)

    with open("wynik.txt", "w") as f:
        f.write("Zadanie 1. min:{} max:{}\n".format(zadanie1odp[0], zadanie1odp[1]))
        f.write("Zadanie 2. pierwszy element:{} dlugosc:{}\n".format(
            zadanie2odp[0], zadanie2odp[1]))
        f.write("Zadanie 3. a){} b){}\n".format(zadanie3odp[0], zadanie3odp[1]))
        f.write("Zadanie 4. base10:{} base8:{}\n".format(zadanie4odp[0], zadanie4odp[1]))

    # print(arr)
