# # ################################ Task 1
## A website requires the users to input username and password to register.
## Create function to check the validity of password input by users.
## Using continue() or break().
## Following are the criteria for checking the password:
## 1. At least 1 letter between [a-z]
## 2. At least 1 number between [0-9]
## 3. At least 1 letter between [A-Z]
## 4. Minimum length of transaction password: 4
## 5. Maximum length of transaction password: 8
## You should to document your code by using python docstrings (google)
## Save result to *.txt file



def checkCorrectPassword(password:str):
    """
        Funkcja Sprawdzająca poprawność hasła podanego przez użytkownika

    Args:
        password(str): haslo które podał użytkownik

    Returns:
        Zwraca zależnie od podanego hasła:
        -błąd
        -zapisywanie do pliku wyniku

    """
    with open("test.txt", "w") as file:

        if len(password)< 4 or len(password)>8:
            print("Haslo musi byc od 4 do 8 znakow!!!")

        hasLower = False
        hasUpper = False
        hasDigit = False

        for char in password:
            if char.islower():
                hasLower = True
            if char.isupper():
                hasUpper = True
            if char.isdigit():
                hasDigit = True

            if hasLower and hasUpper and hasDigit:
                break

        if not (hasLower and hasUpper and hasDigit):
            print("Nie poprawne haslo")
            return False
        else:
            file.write("Haslo Poprawne")
            print("Poprawne haslo :)")
            return True


login = str(input("Podaj nazwe uzytkownika: "))
password = str(input("Podaj haslo: "))

print(checkCorrectPassword.__doc__)

print(checkCorrectPassword(password))