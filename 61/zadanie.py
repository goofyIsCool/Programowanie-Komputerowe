def zadanie1(seq, size):
    diff = int(seq[1]) - int(seq[0])
    for _ in range(size-1):
        r = int(seq[_ + 1]) - int(seq[_])
        if r != diff:
            return [False, r]

    return [True, r]


def is_perfect_cube(x):
    x = abs(x)
    return int(round(x ** (1. / 3))) ** 3 == x


def zadanie2(seq, size):
    max = 0
    seq.reverse()
    for i in range(size):
        if is_perfect_cube(int(seq[i])) and int(seq[i]) > max:
            max = int(seq[i])

    if max == 0:
        return False
    return max


def zadanie3(seq, size):
    arr = []
    seq[0] = int(seq[0])
    for i in range(1, size):
        seq[i] = int(seq[i])
        arr.append(seq[i]-seq[i-1])

    if arr[0] != arr[1] and arr[1] == arr[2]:
        return seq[0]

    if arr[0] != arr[2] and arr[1] != arr[2] and arr[3] == arr[2]:
        return seq[1]

    for i in range(len(arr)):
        if arr[i] != arr[0]:
            return seq[i+1]


if __name__ == "__main__":
    arr = []
    with open("ciagi.txt", "r")as f:
        for line in f:
            arr.append(line)

    counter = 0
    max = 0
    arrZadanie2 = []
    for i in range(0, len(arr), 2):
        size = int(arr[i])
        seq = arr[i+1].split(" ")
        tmp = zadanie1(seq, size)
        if tmp[0]:
            counter += 1
            if tmp[1] > max:
                max = tmp[1]

        tmp2 = zadanie2(seq, size)
        if tmp2 is not False:
            arrZadanie2.append(tmp2)

    arr = []
    with open("bledne.txt", "r")as f:
        for line in f:
            arr.append(line)

    arrZadanie3 = []
    for i in range(0, len(arr), 2):
        size = int(arr[i])
        seq = arr[i+1].split(" ")
        arrZadanie3.append(zadanie3(seq, size))

    with open("wynik1.txt", "w") as f:
        f.write("Ciagow arytmetycznych: {}\n".format(counter))
        f.write("Najwieksza roznica: {}\n".format(max))

    with open("wynik2.txt", "w") as f:
        for seq in arrZadanie2:
            f.write(str(seq) + "\n")

    with open("wynik3.txt", "w") as f:
        for seq in arrZadanie3:
            f.write(str(seq) + "\n")
