import math


def test_get_longest_all_even():
    assert get_longest_all_even([1, 1, 1, 1]) == []
    assert get_longest_all_even([2, 2, 2, 2]) == [2, 2, 2, 2]
    assert get_longest_all_even([1, 2, 3, 2, 2, 3, 6, 6, 6, 5]) == [6, 6, 6]
    assert get_longest_all_even([1, 2, 2, 2, 2, 3, 4, 4, 6, 7]) == [2, 2, 2, 2]


def all_even(l):
    for x in l:
        if x % 2 == 1:
            return False
    return True


def get_longest_all_even(l):
    '''
    Cea mai lunga secventa de nr pare
    :param l:lista de nr intregi
    :return:o lista
    '''
    SubsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if all_even(l[i:j + 1]) == True and len(l[i:j + 1]) > len(SubsecventaMax):
                SubsecventaMax = l[i:j + 1]
    return SubsecventaMax


def test_get_longest_all_primes():
    assert get_longest_all_primes([5, 5, 5]) == [5, 5, 5]
    assert get_longest_all_primes([1]) == []
    assert get_longest_all_primes([8]) == []
    assert get_longest_all_primes([6, 6, 6, 3, 3, 6, 3, 3, 3, 6]) == [3, 3, 3]


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True


def all_primes(l):
    for x in l:
        if is_prime(x) == False:
            return False
    return True


def get_longest_all_primes(l):
    '''
    Afiseaza cea mai lunga secventa de nr prime
    :param l:lista de nr intregi
    :return:o lista ce contine cea mai lunga secventa de nr prime
    '''
    SubsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if all_primes(l[i:j + 1]) and len(l[i:j + 1]) > len(SubsecventaMax):
                SubsecventaMax = l[i:j + 1]
    return SubsecventaMax


def test_all_perfect_squares():
    assert get_longest_all_perfect_squares([1, 2, 3, 4, 4, 2]) == [4, 4]
    assert get_longest_all_perfect_squares([5, 5, 5, 5, 5]) == []
    assert get_longest_all_perfect_squares([1, 2, 3, 4, 5, 144, 144, 9, 4, 5, 5, 9, 9, 9]) == [144,144,9,4]


def all_perfect_squares(l):
    '''
    Verifica daca toate elementele dintr o lista sunt patrate perfecte
    :param l: lista cu elemente intregi
    :return: True sau False
    '''
    for x in l:
        if math.sqrt(x) != int(math.sqrt(x)):
            return False
    return True


def get_longest_all_perfect_squares(l):
    SubsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if all_perfect_squares(l[i:j + 1]) == True and len(l[i:j + 1]) > len(SubsecventaMax):
                SubsecventaMax = l[i:j + 1]
    return SubsecventaMax


def meniu():
    print("1.Citire date:")
    print("2.Determinare cea mai lunga subsecventa de patrate perfecte")
    print("3.Determinare cea mai lunga subsecventa de nr pare")
    print("4.Determinare cea mai lung subsecvanta de nr prime")
    print("5.Stop")


def citeste_lista():
    l = []
    givenString = input("dati elemente lista separate prin virgula:")
    numberAssString = givenString.split(",")
    for x in numberAssString:
        l.append(int(x))
    return l


def main():
    test_get_longest_all_even()
    test_get_longest_all_primes()
    test_all_perfect_squares()
    l = []
    while True:
        meniu()
        optiune = input("Alege optiune:")
        if optiune == "1":
            l = citeste_lista()
        elif optiune == "2":
            print(get_longest_all_perfect_squares(l))
        elif optiune == "3":
            print(get_longest_all_even(l))
        elif optiune == "4":
            print(get_longest_all_primes(l))
        elif optiune == "5":
            break


main()
