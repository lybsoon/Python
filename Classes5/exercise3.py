################ Task 3
## Create function with multiple arguments (x1,x2,...,xn) that accepts a sequence of
## comma-separated numbers from console and returns:
## x1^x1  if number of input parameters equals 1 than y = x1^x1
## x1^x1, x2^x2 if number of input parameters equals 2
## x1^x1, x2^x2, x3^x3 if number of input parameters equals 3
## ....
## x1^x1, ... , x99^x99 if number of input parameters equals 99
## if number of input parameters equals greater than 100 will display an error message.
## Requirements:
## Name of input parameters:
## You should to document your code by using python docstrings (google)
###############

def Pow(*args):
    """
        Funkcja przyjmuje 1 element i poteguje przez jego wartość
    Args:
        *args: wiele argumentow

    Returns: zwraca liste z wynikami dla każdego argumentu

    """
    results = []
    if len(args) >100:
        print("Error")
    else:
        for i in args:
            powers = i ** i
            results.append(powers)

    return results


print(Pow(1,2,3,4,5,6,7,8,9,10))
print(Pow.__doc__)
