################ Task 4
## Create function with multiple arguments (x1,x2,...,xn) that accepts a sequence of
## comma-separated numbers from console and returns:
## x1^x1  if number of input parameters equals 1 than y = x1^x1
## x1^x1, x2^x2 if number of input parameters equals 2
## x1^x1, x2^x2, x3^x3 if number of input parameters equals 3
## ....
## x1^x1, ... , x99^x99 if number of input parameters equals 99
## if number of input parameters equals greater than 100 will display an error message.
## Requirements:
## Use: dynamic variable name (exec() or globals() or locals())
## Name of input parameters: x1, x2, ..., xn
## You should to document your code by using python docstrings (google)
## Wykonaj na Lab6:  Don't forget to handle exceptions (obsłudze wyjątków)
###############
from traceback import print_tb


def Pow(**kwargs):
    """
        Funkcja przyjmuje 1 element i poteguje przez jego wartość
    Args:
        **kwargs: wiele argumentow z przypisanym kluczem

    Returns: zwraca liste z wynikami dla każdego argumentu

    """
    results = []
    if len(kwargs) >100:
        raise Exception("podano za duzo argumentow")

    for i, (key,value) in enumerate(kwargs.items(),1):
        globals()[f"x{i}"] = value
        results.append(globals()[f"x{i}"] ** globals()[f"x{i}"])

    return results

kwargs= {}

for i in range(1,102):
    kwargs[f"x{i}"] = i

print(Pow.__doc__)
# print(Pow(x1=1,x2=2,x3=3,x4=4))
# print(Pow(**kwargs))