def iloraz(a,b,c) : return a/b/c if all(x%2 == 0 for x in (a,b,c)) else "liczby musza byc parzyste"

print(iloraz(8,4,2))