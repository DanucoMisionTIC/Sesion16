import hashlib
userid= "admin"
password= "mensaje"
# Opcion 1
m = hashlib.sha256(bytes(password, encoding= 'utf-8'))
# Opcion 2
passbyte= password.encode("utf-8")
n = hashlib.sha256(passbyte)
#
# Imprime el texto cifrado en binario
print(m.digest())
print(m.digest_size, m.name)
print(n.digest())
print(m.hexdigest())