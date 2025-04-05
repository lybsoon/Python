########################## Task 5 ########################
## The first step,
## generate test data: create folder. Create 5 text files to this folder,
## each file contains more than 5 sentences.
## Filenames: Text1ID_ABC, Text2ID_405.txt, Text3ID_607.txt, Text4ID_ABC5.txt, Text5ID_DEF.txt
##
## Create function with multiple arguments that:
## a) print all file from folder
## b) if the file name contains 'ABC', count how many words in the text of file
## contain words with more than 3 letters
## Wykonaj na Lab6:  Next step, decorate this function, add the following functionality:
## a) the function will check how many files have 0 in the filename
## b) if the file has 0 in the filename then the function counts words in the text of the file
## c) if the filename contains 'EF.txt', then the function copy this file to
## 'DocumentLab5copy' directory


import os
import shutil

def decorator(fun):
    """
    Funkcja sprawdza ile plikow ma "0" w nazwie pliku i sprawdza ile ma słów,
    a jezeli zawiera "EF.txt" to kopije plik do Classes5

    Args:
        fun: Odniesienie do głównej funkcji
    Returns:

    """
    def functions(folderPath):
        wordsCounter = 0
        counter = 0
        folder = os.path.dirname(folderPath)

        for file in os.listdir(folderPath):
            if "0" in file:
                counter += 1
                filePath = os.path.join(folderPath, file)
                with open(filePath, "r") as f:
                    words = f.read().split()
                    for word in words:
                      wordsCounter += 1

        for file in os.listdir(folderPath):
            if "EF.txt" in file:
                source_file = os.path.join(folderPath,file)
                toFile = os.path.join(folder,file)
                shutil.copy(source_file, toFile)
                print(f"Plik {file} został skopiowany do folderu {folder}")



        print(f"liczba plikow zawierająca w nazwie '0' wynosi: {counter}")
        print(f"liczba słów w plikach zawierających '0' wynosi: {wordsCounter}\n")
        return fun(folderPath)
    return functions



@decorator
def folderFiles(folderPath):
    """
    Funkcja która wypisuje pliki z folderu, a dla tych ktore zawierają w nazwie "ABC"
    liczy ile słow ma wiecej niz 3 litery

    Args:
        folderPath (str): Ścieżka prowadząca do folderu gdzie znajdują sie pliki.

    Returns:
        Zwraca pliki które posiadają 'ABC' w nazwie i zlicza słowa dłuższe od 3 liter
    """

    files = os.listdir(folderPath)
    print("pliki:")
    for file in files:
        print(file)
    print("")

    print("Foldery które zawieraja 'ABC':")
    for file in files:
        if 'ABC' in file:
            filePath = os.path.join(folderPath,file)
            with open(filePath,"r") as f:
                words = f.read().split()
                counter = 0
                for word in words:
                    if len(word) >3:
                        counter +=1

                print(f"{file}: {counter} jest słów które zawierają wiecęj niż 3 litery")




folderPath = "directory"
print(folderFiles.__doc__)
folderFiles(folderPath)