from werkzeug.security import generate_password_hash, check_password_hash

def validate_pwd(in_passwd):
    # Consulta el password almacenado en el database
    password= "admin2021"
    password= str(hash(password))
    #
    boolpasswd= check_password_hash(in_passwd, password)
    return boolpasswd

if __name__=='__main__':
    forma_passwd= "admin2021"
    # Password enviado en la forma
    forma_passwd= str(hash(forma_passwd))
    forma_passwd_hashed= generate_password_hash(forma_passwd)
    # Invocando la validacion
    checkit= validate_pwd(forma_passwd_hashed)
    if checkit:
        print("Password Correcto")
    else :
        print("Error al digitar el password!!!")
