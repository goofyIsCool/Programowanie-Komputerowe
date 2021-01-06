if __name__ == '__main__':

    liczby = []
    with open("liczby.txt", "r") as f:
        for line in f:
            liczby.append(int(line))

    print(liczby)
