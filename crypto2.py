import hashlib
m = hashlib.sha512(b"mensaje")  	
print(m)    		# Imprime el texto cifrado en binario
print(m.hexdigest())
