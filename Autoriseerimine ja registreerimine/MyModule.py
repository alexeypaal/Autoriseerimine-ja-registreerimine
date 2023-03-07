import string
from random import choice

# luua tühjad nimekirjad login ja paroolid
# Создаю пустые списки логинов и паролей
logins = []
passwords = []

# funktsioon juhusliku parooli genereerimiseks
# функция случайного пароля
def salasona(k: int):
  sala=""
  for i in range(k):
   t=choice(string.ascii_letters) #Aa...Zz
   num=choice([1,2,3,4,5,6,7,8,9,0])
   t_num=[t,str(num)]
   sala+=choice(t_num)
  return sala

# funktsioon kasutaja registreerimiseks
# функция регистрации пользователя
def register():
    login = input("Sisesta oma login: ")
    if login in logins:
        print("See login on juba votud.")
        return
    salasõna_valik = input("Kas sa tahad juhuslik salasõne? (Y/N): ")
    if salasõna_valik.lower() == 'y':
        password = salasõna(8)
        print(f"Sinu salasõna: {password}")
    else:
        while True:
            password = input("Sisesta salasona: ")
            if any(char.isdigit() for char in password) and any(char.islower() for char in password) and any(char.isupper() for char in password) and any(char in string.punctuation for char in password):
                break
            else:
                print("Teie parool peab sisaldama vähemalt ühte numbrit, ühte väiketähte, ühte suurtähte ja ühte erilist sümbolit.")
    logins.append(login)
    passwords.append(password)
    print("Registreerimine õnnetus!")

# funktsioon kasutaja autoriseerimiseks
# функция авторизации пользователя
def authorize():
    login = input("Sisesta oma login: ")
    if login not in logins:
        print("See logini pole registreeritud.")
        return
    password = input("Sisesta oma salasõna: ")
    if password != passwords[logins.index(login)]:
        print("Vale salasõna.")
        return
    print("Login õnnetus!")

# funktsioon nime või parooli muutmiseks
# функция смены имени или пароля
def change():
    login = input("Sisesta oma login: ")
    if login not in logins:
        print("See nimi ei ole registreeritud.")
        return
    valik = input("Kas soovite muuta oma nime või parooli? (login/password): ")
    if valik.lower() == 'login':
        new_login = input("Sisesta uue login: ")
        if new_login in logins:
            print("See login on juba võtud.")
            return
        logins[logins.index(login)] = new_login
        print("Login muudatus õnnetus.")
    elif valik.lower() == 'password':
        while True:
            new_password = input("Sisesta uue salasone: ")
            if any(char.isdigit() for char in new_password) and any(char.islower() for char in new_password) and any(char.isupper() for char in new_password) and any(char in string.punctuation for char in new_password):
                break
            else:
                print("Teie parool peab sisaldama vähemalt ühte numbrit, ühte väiketähte, ühte suurtähte ja ühte erilist sümbolit.")
        passwords[logins.index(login)] = new_password
        print("Salasone muudatus õnnetus.")
    else:
        print("Viga.")

# funktsioon unustatud parooli taastamiseks
# функция восстановления пароля
def forgotpassword():
    login = input("Наберите логин: ")
    if login not in logins:
        print("Вы не зарегистрированы.")
        return
    new_password = salasõna(8)
    passwords[logins.index(login)] = new_password
    print(f"Sinu uus parool on: {new_password}")

# funktsioon välja logimiseks
# функция выхода из системы
def logout():
    print("Sa logisid välja.")
    
