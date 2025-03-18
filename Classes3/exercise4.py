logins = []
passwords = []

while True:
    login = input("Podaj login ('STOP' by zakończyć): ")
    if login == "STOP":
        break

    if login == " ":
        print("Pusty login")
        continue

    password = input("Podaj haslo: ")

    if password =="":
        print("haslo puste")
        continue

    logins.append(login)
    passwords.append(password)

data = {login: password for login, password in zip(logins,passwords)}

for i,(login,password) in enumerate(data.items(),start=1):
    print(str(i)+"."+login+" "+password)
