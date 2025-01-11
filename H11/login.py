login_pass = "kohane123"
login_user = "fgb123"

def login():
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    if username == login_user and password == login_pass:
        print("Login Berhasil")
    else:
        print("Username Atau Password Salah")

login()