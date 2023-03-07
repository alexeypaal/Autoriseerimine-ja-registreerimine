from MyModule import register, authorize, change, forgotpassword, logout

while True:
    print("Valige:")
    print("1. Registreerima")
    print("2. Logi sisse")
    print("3. Muudata login voi salasõna")
    print("4. Unustasid salasone")
    print("5. Logi välja")
    valik = input("Sisesta number (1-5): ")
    if valik == '1':
        register()
    elif valik == '2':
        authorize()
    elif valik == '3':
        change()
    elif valik == '4':
        forgotpassword()
    elif valik == '5':
        logout()
        exit()
    else:
        print("Viga! Palun andke number 1st kuni 5ni.")
