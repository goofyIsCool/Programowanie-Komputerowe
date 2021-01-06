from math import ceil


def zadanie4(allTempS1):
    skokMax = 0
    for i in range(len(allTempS1)-1):
        for j in range(i+1, len(allTempS1)):
            skok = ceil(((allTempS1[i] - allTempS1[j])**2)/(j-i))
            if skok > skokMax:
                skokMax = skok

    return skokMax


def main():
    day1 = []
    day2 = []
    day3 = []

    temp1 = {}
    temp2 = {}
    temp3 = {}

    allTempS1 = []
    setOfDays = set()
    print("Zadainie 1:")
    for _ in range(1, 4):
        with open("dane_systemy{}.txt".format(_), "r") as f:

            min_temp = 100
            timeT = None
            counter = None
            day = 1

            for line in f:
                time = int(line.split(" ")[0], 2**_)

                if timeT is None:
                    timeT = time
                    counter = 0
                if time != timeT:
                    counter += 1
                    if _ == 1:
                        day1.append(day)
                    elif _ == 2:
                        day2.append(day)
                    else:
                        day3.append(day)

                timeT += 24
                temp = int(line.split(" ")[1], 2**_)

                if temp < min_temp:
                    min_temp = temp

                if _ == 1:
                    allTempS1.append(temp)
                    if len(temp1) >= 1:
                        if temp > max(temp1.values()):
                            temp1[day] = temp
                            setOfDays.add(day)
                    else:
                        temp1[day] = temp
                        setOfDays.add(day)

                if _ == 2:
                    if len(temp2) >= 1:
                        if temp > max(temp2.values()):
                            temp2[day] = temp
                            setOfDays.add(day)
                    else:
                        temp2[day] = temp
                        setOfDays.add(day)

                if _ == 3:
                    if len(temp3) >= 1:
                        if temp > max(temp3.values()):
                            temp3[day] = temp
                            setOfDays.add(day)
                    else:
                        temp3[day] = temp
                        setOfDays.add(day)

                day += 1

            min_temp = bin(min_temp)
            if min_temp[0] == '-':
                print("Min temperature in S{}: {}".format(_, min_temp[0]+min_temp[3:]))
            else:
                print("Min temperature in S{}: {}".format(_, min_temp[3:]))

    print("Zadainie 2:")
    counter = 0
    for i in range(len(day1)):
        if day1[i] in day2 and day1[i] in day3:
            counter += 1
    print(counter)

    # print(setOfDays)
    print("Zadainie 3:")
    print(len(setOfDays))

    print("Zadainie 4:")
    print(zadanie4(allTempS1))


main()
