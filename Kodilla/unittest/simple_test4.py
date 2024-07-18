def wypisz(n):
    for i in range(n):
        print(i)

# Przykład użycia
#n = int(input("Podaj liczbę: "))
#wypisz(n)

def test_wypisz():
    assert wypisz(5) == range(5)

test_wypisz()
