import os
import sys
hashseed = os.getenv('PYTHONHASHSEED')
if not hashseed:
    os.environ['PYTHONHASHSEED'] = '0'
    os.execv(sys.executable, [sys.executable] + sys.argv)

valor="Hola Mundo!"
print(hash(valor))

# Ejemplo con salt
salt= "semilla"
print(hash(valor+salt))