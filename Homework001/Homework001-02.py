
def TruthTable():
    '''программа для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.'''

    a = (False, True)
    print('X \t\tY \t\tZ \t\tftt')

    for X in a:
        for Y in a:
            for Z in a:
                ftt = not (X or Y or Z) == (not X) and (not Y) and (not Z)
                #print(X, '\t', Y, '\t', Z, '\t', ftt)
                print(int(X), '\t\t', int(Y), '\t\t', int(Z), '\t\t', ftt)

TruthTable()