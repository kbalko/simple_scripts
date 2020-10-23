

def start():
    print("Witaj w programie Fibonacci.")
    while True:
        print(input_n())
        line = input("\nChcesz kontynuować wciśnij enter, by wyjść z programu wpisz 'koniec': ")
        if line.lower() == "koniec":
            break
    print("Zakończyłeś prace z programem.")

def input_n():
    start = input("\nWprowadź liczbę całkowitą: ")
    try:
        n = int(start)
        if n >= 0:
            output = "{} liczba ciągu Fibonnaciego to {}. " \
                    "\nW przedziale od 0 do {} jest {} liczb ciągu Fibonacciego. ".format(n, fib2(n), n, fib(n))
            return output
        else:
            return "Tylko liczy dodatnie!"
    except:
        n = start
        output_wrong = 'Niestety "{}" to nie jest prawidłowa wartość.'.format(n)
        return output_wrong


def fib(n):
    a, b = 0, 1
    numb = 0
    while a <= n:
        a, b = b, a + b
        numb += 1
    return numb


def fib2(n):
    a, b = 0, 1
    for i in range(1,n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    print(start())


